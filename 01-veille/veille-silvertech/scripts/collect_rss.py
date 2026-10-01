"""Collecte des flux RSS : Google Alerts, médias, Reddit.

Affiche un bilan JSON {origine: nb_nouveaux, ..., "erreurs": [...]} sur la dernière ligne.
"""
import json
import time

import feedparser

from add_items import inserer
from common import connexion, regles, sources

AGENT = "Mozilla/5.0 (veille-silvertech; projet etudiant Ynov)"


def lire_flux(url: str, essais: int = 3):
    for i in range(essais):
        d = feedparser.parse(url, agent=AGENT)
        statut = getattr(d, "status", None)
        if statut == 429 and i < essais - 1:  # Reddit : limitation de débit
            time.sleep(15 * (i + 1))
            continue
        return d, statut
    return d, statut


def main():
    r, s = regles(), sources()
    limite = r["collecte"]["max_par_flux"]
    flux = []
    for a in s.get("google_alerts") or []:
        if a.get("url") and a["url"] != "REMPLACER":
            flux.append((f"rss:{a['nom']}", a["nom"], a["url"], a.get("code")))
    for m in s.get("medias") or []:
        flux.append((f"rss:{m['nom']}", m["nom"], m["url"], None))
    for rd in s.get("reddit") or []:
        flux.append(("reddit", rd["nom"], rd["url"], None))

    bilan, erreurs = {}, []
    with connexion() as cx:
        for origine, nom, url, code in flux:
            d, statut = lire_flux(url)
            if not d.entries:
                erreurs.append(f"{nom} : aucun élément (HTTP {statut})")
                continue
            items = [{
                "url": e.get("link"),
                "titre": e.get("title"),
                "extrait": e.get("summary"),
                "source_nom": nom,
                "origine": origine,
                "code_vise": code,
                "publie_le": e.get("published_parsed") or e.get("updated_parsed"),
            } for e in d.entries[:limite]]
            n = inserer(cx, items)
            cle = "reddit" if origine == "reddit" else "rss"
            bilan[cle] = bilan.get(cle, 0) + n
            print(f"{nom:22} {n:3} nouveaux / {len(items)} lus")
            cx.commit()
            if origine == "reddit":
                time.sleep(3)
    bilan["erreurs"] = erreurs
    for e in erreurs:
        print("ATTENTION", e)
    print(json.dumps(bilan, ensure_ascii=False))


if __name__ == "__main__":
    main()

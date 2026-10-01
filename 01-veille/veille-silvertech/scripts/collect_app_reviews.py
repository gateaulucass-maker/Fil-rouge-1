"""Collecte des avis App Store via le flux public d'Apple.

Aucune donnée personnelle n'est stockée : ni auteur, ni pseudo. Seuls la note,
le titre et le texte de l'avis sont gardés (le texte sera anonymisé à la qualification).
"""
import json
import urllib.request

from add_items import inserer
from common import connexion, regles, sources

FLUX = "https://itunes.apple.com/{pays}/rss/customerreviews/id={app_id}/sortBy=mostRecent/json"


def lire_avis(pays: str, app_id: str) -> list[dict]:
    req = urllib.request.Request(FLUX.format(pays=pays, app_id=app_id),
                                 headers={"User-Agent": "veille-silvertech"})
    with urllib.request.urlopen(req, timeout=20) as rep:
        data = json.load(rep)
    entrees = data.get("feed", {}).get("entry", [])
    if isinstance(entrees, dict):
        entrees = [entrees]
    return [e for e in entrees if "im:rating" in e]  # la 1re entrée peut décrire l'app


def main():
    r, s = regles(), sources()
    conf = s["app_store"]
    limite = r["collecte"]["max_avis_par_app"]
    total, erreurs = 0, []
    with connexion() as cx:
        for app in conf["apps"]:
            try:
                avis = lire_avis(conf["pays"], app["app_id"])[:limite]
            except Exception as exc:  # flux indisponible : on le signale, on continue
                erreurs.append(f"{app['nom']} : {exc}")
                continue
            items = []
            for a in avis:
                avis_id = a["id"]["label"]
                note = a["im:rating"]["label"]
                items.append({
                    # URL stable par avis (pas de nom d'auteur)
                    "url": f"https://apps.apple.com/{conf['pays']}/app/id{app['app_id']}#avis-{avis_id}",
                    "titre": f"[{app['nom']} · {note}/5] {a['title']['label']}",
                    "extrait": a["content"]["label"],
                    "source_nom": f"App Store · {app['nom']}",
                    "origine": "avis_app",
                    "publie_le": a.get("updated", {}).get("label"),
                })
            n = inserer(cx, items)
            total += n
            print(f"{app['nom']:16} {n:3} nouveaux / {len(items)} lus")
    for e in erreurs:
        print("ATTENTION", e)
    print(json.dumps({"avis_app": total, "erreurs": erreurs}, ensure_ascii=False))


if __name__ == "__main__":
    main()

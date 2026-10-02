"""Collecte des flux de la veille (mêmes sources que le pipeline /veille) pour la veille du jeudi.

Lit 01-veille/veille-silvertech/config/sources.yaml : 13 Google Alerts, médias (Silvereco,
Maddyness, FrenchWeb, CNIL), Reddit (3 communautés), avis App Store (4 applications).
N'écrit rien en base : affiche une liste JSON de candidats datés sur la sortie standard.

  python3 automatisation/collecte_flux.py --depuis 2026-09-25 > /tmp/candidats.json

Chaque candidat : source, type (alerte, media, reddit, avis_app), titre, url, date (AAAA-MM-JJ
ou null), extrait (sans pseudo ni e-mail). Les flux en erreur sont listés dans « erreurs ».
"""
import argparse
import json
import re
import subprocess
import sys
import time
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from datetime import date, datetime, timedelta
from email.utils import parsedate_to_datetime
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
PIPELINE = RACINE / "01-veille" / "veille-silvertech"
sys.path.insert(0, str(PIPELINE / "scripts"))

try:
    import yaml  # noqa: F401
except ImportError:  # environnement cloud sans PyYAML
    subprocess.run([sys.executable, "-m", "pip", "install", "-q", "pyyaml"], check=False)

from common import deredirect, nettoyer_html, retirer_pseudos  # noqa: E402
import yaml  # noqa: E402

AGENT = "Mozilla/5.0 (veille-silvertech; projet etudiant Ynov)"
ATOM = "{http://www.w3.org/2005/Atom}"


def lire(url: str, essais: int = 3) -> bytes:
    for i in range(essais):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": AGENT})
            with urllib.request.urlopen(req, timeout=25) as rep:
                return rep.read()
        except urllib.error.HTTPError as exc:  # Reddit limite le débit (429) : on patiente
            if exc.code == 429 and i < essais - 1:
                time.sleep(20 * (i + 1))
                continue
            raise


def date_iso(texte):
    if not texte:
        return None
    texte = texte.strip()
    try:
        return datetime.fromisoformat(texte.replace("Z", "+00:00")).date().isoformat()
    except ValueError:
        pass
    try:
        return parsedate_to_datetime(texte).date().isoformat()
    except (TypeError, ValueError):
        return None


def entrees_flux(xml: bytes):
    """Renvoie [(titre, lien, date, extrait)] pour un flux RSS 2.0 ou Atom."""
    try:
        racine = ET.fromstring(xml)
    except ET.ParseError:  # flux mal formé (ex. texte après la balise de fin) : on coupe après </rss> ou </feed>
        m = re.search(rb"</(rss|feed)>", xml)
        racine = ET.fromstring(xml[: m.end()] if m else xml)
    sortie = []
    for it in racine.iter("item"):  # RSS 2.0
        sortie.append((it.findtext("title"), it.findtext("link"),
                       date_iso(it.findtext("pubDate")), it.findtext("description")))
    for it in racine.iter(f"{ATOM}entry"):  # Atom (Google Alerts, Reddit)
        lien = it.find(f"{ATOM}link")
        sortie.append((it.findtext(f"{ATOM}title"), lien.get("href") if lien is not None else None,
                       date_iso(it.findtext(f"{ATOM}published") or it.findtext(f"{ATOM}updated")),
                       it.findtext(f"{ATOM}content") or it.findtext(f"{ATOM}summary")))
    return sortie


def candidat(source, type_, titre, url, jour, extrait):
    return {"source": source, "type": type_, "titre": retirer_pseudos(nettoyer_html(titre, 300)),
            "url": deredirect((url or "").strip()), "date": jour,
            "extrait": retirer_pseudos(nettoyer_html(extrait, 500))}


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--depuis", help="date AAAA-MM-JJ (défaut : il y a 7 jours)")
    a = p.parse_args()
    depuis = a.depuis or (date.today() - timedelta(days=7)).isoformat()
    s = yaml.safe_load((PIPELINE / "config" / "sources.yaml").read_text(encoding="utf-8"))

    flux = [(f["nom"], "alerte", f["url"]) for f in s.get("google_alerts") or []
            if f.get("url") and f["url"] != "REMPLACER"]
    flux += [(f["nom"], "media", f["url"]) for f in s.get("medias") or []]
    flux += [(f["nom"], "reddit", f["url"]) for f in s.get("reddit") or []]

    candidats, erreurs = [], []
    for nom, type_, url in flux:
        try:
            for titre, lien, jour, extrait in entrees_flux(lire(url)):
                if lien and titre and (jour is None or jour >= depuis):
                    candidats.append(candidat(nom, type_, titre, lien, jour, extrait))
        except Exception as exc:  # un flux en panne ne bloque pas les autres
            erreurs.append(f"{nom} : {exc}")
        if type_ == "reddit":
            time.sleep(3)

    conf = s.get("app_store") or {}
    for app in conf.get("apps") or []:
        url = f"https://itunes.apple.com/{conf.get('pays', 'fr')}/rss/customerreviews/id={app['app_id']}/sortBy=mostRecent/json"
        try:
            entrees = json.loads(lire(url)).get("feed", {}).get("entry", [])
            for e in entrees if isinstance(entrees, list) else [entrees]:
                if "im:rating" not in e:
                    continue
                jour = date_iso(e.get("updated", {}).get("label"))
                if jour and jour >= depuis:
                    candidats.append(candidat(
                        f"App Store · {app['nom']}", "avis_app",
                        f"[{app['nom']} · {e['im:rating']['label']}/5] {e['title']['label']}",
                        f"https://apps.apple.com/{conf.get('pays', 'fr')}/app/id{app['app_id']}#avis-{e['id']['label']}",
                        jour, e["content"]["label"]))
        except Exception as exc:
            erreurs.append(f"App Store {app['nom']} : {exc}")

    vus, uniques = set(), []
    for c in candidats:  # dédoublonnage par URL
        if c["url"] not in vus:
            vus.add(c["url"])
            uniques.append(c)
    print(json.dumps({"depuis": depuis, "nb": len(uniques), "candidats": uniques, "erreurs": erreurs},
                     ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()

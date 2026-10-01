"""Ajoute des éléments bruts dans raw_items. Dédoublonnage par URL.

Usage (agent collecteur, saisie manuelle Google Play) :
  echo '[{"url": "...", "titre": "...", "extrait": "...", "source_nom": "...",
          "origine": "web_search", "code_vise": "M1", "publie_le": "2026-05-01"}]' \
    | python scripts/add_items.py
"""
from common import connexion, deredirect, domaine, lire_json_stdin, nettoyer_html, retirer_pseudos, vers_date


def inserer(cx, items: list[dict]) -> int:
    """Insère les éléments ; renvoie le nombre de nouveaux (les URL connues sont ignorées)."""
    nouveaux = 0
    with cx.cursor() as cur:
        for it in items:
            url = deredirect((it.get("url") or "").strip())
            titre = retirer_pseudos(nettoyer_html(it.get("titre"), 300))
            if not url or not titre:
                continue
            cur.execute(
                """INSERT INTO raw_items (url, domaine, source_nom, titre, extrait, origine, code_vise, publie_le)
                   VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                   ON CONFLICT (url) DO NOTHING""",
                (url, domaine(url), it.get("source_nom"), titre, retirer_pseudos(nettoyer_html(it.get("extrait"))),
                 it.get("origine", "web_search"), it.get("code_vise") or None, vers_date(it.get("publie_le"))),
            )
            nouveaux += cur.rowcount
    return nouveaux


def main():
    items = lire_json_stdin()
    with connexion() as cx:
        n = inserer(cx, items)
    print(f"{n} nouveaux éléments sur {len(items)} reçus.")


if __name__ == "__main__":
    main()

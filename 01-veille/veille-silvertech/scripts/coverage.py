"""Couverture du catalogue : nombre d'éléments validés (et à revoir) par code.

  python scripts/coverage.py          # tableau texte
  python scripts/coverage.py --json   # pour le rapport et les agents
"""
import argparse
import json

from common import connexion

REQ = """SELECT c.code, c.axe, c.libelle, c.statut,
                count(v.id) FILTER (WHERE v.statut = 'valide')   AS valides,
                count(v.id) FILTER (WHERE v.statut = 'a_revoir') AS a_revoir
         FROM catalogue c LEFT JOIN veille_items v ON v.code_info = c.code
         GROUP BY c.code, c.axe, c.libelle, c.statut
         ORDER BY array_position(ARRAY['marche','concurrence','usagers','techno','reglementaire'], c.axe),
                  substring(c.code, 2)::int"""


def couverture(cx) -> list[dict]:
    cles = ("code", "axe", "libelle", "statut", "valides", "a_revoir")
    return [dict(zip(cles, l)) for l in cx.execute(REQ).fetchall()]


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--json", action="store_true")
    a = p.parse_args()
    with connexion() as cx:
        lignes = couverture(cx)
    if a.json:
        print(json.dumps(lignes, ensure_ascii=False))
        return
    print(f"{'Code':5} {'Statut':7} {'Validés':>7} {'À revoir':>8}  Libellé")
    for l in lignes:
        trou = "  ← TROU" if l["statut"] == "requis" and l["valides"] == 0 else ""
        print(f"{l['code']:5} {l['statut']:7} {l['valides']:>7} {l['a_revoir']:>8}  {l['libelle']}{trou}")
    trous = [l["code"] for l in lignes if l["statut"] == "requis" and l["valides"] == 0]
    print(f"\nCodes requis sans élément validé : {len(trous)} ({', '.join(trous) or 'aucun'})")


if __name__ == "__main__":
    main()

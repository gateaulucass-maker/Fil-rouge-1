"""Liste les éléments à qualifier en JSON (pour l'agent qualificateur).

Usage : python scripts/pending.py [--limite 10] [--tranche 2/5]
  --tranche k/n : seulement les id tels que id % n == k-1 (qualificateurs en parallèle sur des lots disjoints)
"""
import argparse
import json

from common import connexion


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--limite", type=int, default=10)
    p.add_argument("--compter", action="store_true", help="affiche seulement le nombre restant")
    p.add_argument("--tranche", help="k/n")
    a = p.parse_args()
    k, n = (int(x) for x in a.tranche.split("/")) if a.tranche else (1, 1)
    with connexion() as cx:
        if a.compter:
            print(cx.execute("SELECT count(*) FROM raw_items WHERE etat = 'a_qualifier' AND id %% %s = %s",
                             (n, k - 1)).fetchone()[0])
            return
        lignes = cx.execute(
            """SELECT id, url, source_nom, titre, extrait, origine, code_vise, publie_le
               FROM raw_items WHERE etat = 'a_qualifier' AND id %% %s = %s
               ORDER BY id LIMIT %s""", (n, k - 1, a.limite)).fetchall()
    cles = ("raw_id", "url", "source_nom", "titre", "extrait", "origine", "code_vise", "publie_le")
    print(json.dumps([dict(zip(cles, l)) for l in lignes], ensure_ascii=False, default=str, indent=1))


if __name__ == "__main__":
    main()

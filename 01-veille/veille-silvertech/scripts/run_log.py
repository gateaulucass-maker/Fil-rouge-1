"""Journal des exécutions (table runs) : preuve du dispositif et déclaration d'usage IA.

  python scripts/run_log.py debut                       # affiche l'id du run
  python scripts/run_log.py fin 3 --collectes '{"rss": 12, "avis_app": 40}' \
         --filtres 20 --qualifies 15 --hors-sujet 5 [--notes "..."]
"""
import argparse
import json
import os

from common import connexion


def main():
    p = argparse.ArgumentParser()
    sp = p.add_subparsers(dest="cmd", required=True)
    sp.add_parser("debut")
    f = sp.add_parser("fin")
    f.add_argument("run_id", type=int)
    f.add_argument("--collectes", default="{}")
    f.add_argument("--filtres", type=int, default=0)
    f.add_argument("--qualifies", type=int, default=0)
    f.add_argument("--hors-sujet", type=int, default=0)
    f.add_argument("--notes")
    a = p.parse_args()
    with connexion() as cx:
        if a.cmd == "debut":
            print(cx.execute("INSERT INTO runs (modele) VALUES (%s) RETURNING id",
                             (os.environ.get("VEILLE_MODELE", "non déclaré"),)).fetchone()[0])
        else:
            cx.execute(
                """UPDATE runs SET termine_le = now(), collectes = %s, nb_filtres = %s, nb_qualifies = %s,
                       nb_hors_sujet = %s, notes = %s,
                       duree_secondes = extract(epoch FROM now() - demarre_le)::int
                   WHERE id = %s""",
                (json.dumps(json.loads(a.collectes)), a.filtres, a.qualifies, a.hors_sujet, a.notes, a.run_id))
            print(f"run {a.run_id} clôturé")


if __name__ == "__main__":
    main()

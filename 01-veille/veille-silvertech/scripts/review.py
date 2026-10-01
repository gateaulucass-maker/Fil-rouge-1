"""Revue humaine des éléments qualifiés.

  python scripts/review.py liste [--axe usagers]            # éléments à revoir
  python scripts/review.py valider 12 --pertinence 3 --par Lucas [--commentaire "..."]
  python scripts/review.py rejeter 12 --par Lucas [--commentaire "..."]
  python scripts/review.py interactif --par Lucas            # un par un, au clavier
"""
import argparse

from common import AXES, connexion, niveau, regles

REQ_LISTE = """SELECT id, axe, code_info, flux, score_fiabilite, pertinence_proposee, titre, url, resume,
                      pourquoi_important, sensible, ethique, irritant
               FROM veille_items WHERE statut = 'a_revoir' {filtre}
               ORDER BY axe, score_fiabilite DESC NULLS LAST, pertinence_proposee DESC NULLS LAST, id"""


def lister(cx, axe=None):
    filtre, params = ("AND axe = %s", (axe,)) if axe else ("", ())
    return cx.execute(REQ_LISTE.format(filtre=filtre), params).fetchall()


def afficher(l, r):
    (id_, axe, code, flux, score, pp, titre, url, resume, pourquoi, sensible, ethique, irritant) = l
    badge = f"score {score}/7 ({niveau(score, r)})" if flux == "fait" else f"signal · {irritant or '-'}"
    marques = " ".join(m for m, v in (("[SENSIBLE]", sensible), ("[ÉTHIQUE]", ethique)) if v)
    print(f"\n#{id_}  {axe} · {code or '-'} · {badge} · pertinence proposée {pp or '-'} {marques}")
    print(f"  {titre}\n  {url}")
    if resume:
        print(f"  Résumé : {resume}")
    if pourquoi:
        print(f"  Pourquoi : {pourquoi}")


def decider(cx, id_, statut, par, pertinence=None, commentaire=None):
    n = cx.execute(
        """UPDATE veille_items SET statut = %s, pertinence = COALESCE(%s, pertinence_proposee),
               valide_par = %s, commentaire = COALESCE(%s, commentaire), revu_le = now()
           WHERE id = %s""",
        (statut, pertinence if statut == "valide" else None, par, commentaire, id_)).rowcount
    print(f"#{id_} → {statut}" if n else f"#{id_} introuvable")


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = p.add_subparsers(dest="cmd", required=True)
    l = sp.add_parser("liste"); l.add_argument("--axe", choices=AXES)
    for nom in ("valider", "rejeter"):
        s = sp.add_parser(nom)
        s.add_argument("id", type=int)
        s.add_argument("--par", required=True, help="prénom de la personne qui décide")
        s.add_argument("--commentaire")
        if nom == "valider":
            s.add_argument("--pertinence", type=int, choices=(1, 2, 3))
    i = sp.add_parser("interactif"); i.add_argument("--par", required=True); i.add_argument("--axe", choices=AXES)
    a = p.parse_args()
    r = regles()

    with connexion() as cx:
        if a.cmd == "liste":
            lignes = lister(cx, a.axe)
            for ligne in lignes:
                afficher(ligne, r)
            print(f"\n{len(lignes)} élément(s) à revoir.")
        elif a.cmd == "valider":
            decider(cx, a.id, "valide", a.par, a.pertinence, a.commentaire)
        elif a.cmd == "rejeter":
            decider(cx, a.id, "rejete", a.par, None, a.commentaire)
        else:
            for ligne in lister(cx, a.axe):
                afficher(ligne, r)
                rep = input("  [v]alider [1-3] / [r]ejeter / [s]auter / [q]uitter > ").strip().lower()
                if rep.startswith("q"):
                    break
                if rep.startswith("v") or rep[:1] in "123" and rep:
                    pert = int(rep[-1]) if rep[-1] in "123" else None
                    decider(cx, ligne[0], "valide", a.par, pert)
                elif rep.startswith("r"):
                    decider(cx, ligne[0], "rejete", a.par, None, input("  motif (facultatif) > ") or None)
                cx.commit()


if __name__ == "__main__":
    main()

"""Recalcule le score de fiabilité de tous les faits avec les règles actuelles (config/regles.yaml).

À lancer après toute modification des listes de domaines ou des seuils.
  python scripts/rescore.py
"""
from collections import Counter

from common import connexion, regles, score_fiabilite


def main():
    r = regles()
    avant, apres = Counter(), Counter()
    with connexion() as cx:
        lignes = cx.execute("""SELECT id, url, publie_le, axe, source_primaire_url, score_fiabilite
                               FROM veille_items WHERE flux = 'fait'""").fetchall()
        for id_, url, publie, axe, sp, ancien in lignes:
            sc = score_fiabilite(url, publie, axe, sp, r)
            avant[ancien] += 1
            apres[sc["score_fiabilite"]] += 1
            cx.execute("""UPDATE veille_items SET score_fiabilite = %s, autorite = %s, fraicheur = %s,
                              bonus_source_primaire = %s WHERE id = %s""",
                       (sc["score_fiabilite"], sc["autorite"], sc["fraicheur"], sc["bonus_source_primaire"], id_))
    print(f"{len(lignes)} faits recalculés")
    print("avant :", dict(sorted(avant.items(), key=lambda kv: (kv[0] is None, kv[0] or 0))))
    print("après :", dict(sorted(apres.items(), key=lambda kv: (kv[0] is None, kv[0] or 0))))


if __name__ == "__main__":
    main()

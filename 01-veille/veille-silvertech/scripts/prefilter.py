"""Filtrage SANS IA des éléments « nouveau ».

Règles (config/regles.yaml) : domaine exclu, hors mots-clés, doublon de titre
sur 30 jours, publication de plus de 36 mois (sauf réglementaire).
Les éléments retenus passent à « a_qualifier », les autres à « filtre » avec leur motif.
"""
import json
from collections import Counter

from common import connexion, motif_rejet, regles, titre_normalise


def main():
    r = regles()
    jours = r["doublons"]["fenetre_jours"]
    with connexion() as cx:
        recents = {titre_normalise(t) for (t,) in cx.execute(
            """SELECT titre FROM raw_items
               WHERE etat IN ('a_qualifier', 'qualifie') AND collecte_le > now() - make_interval(days => %s)""",
            (jours,))}
        nouveaux = cx.execute(
            """SELECT id, domaine, titre, extrait, origine, code_vise, publie_le
               FROM raw_items WHERE etat = 'nouveau' ORDER BY id""").fetchall()
        motifs = Counter()
        with cx.cursor() as cur:
            for (id_, dom, titre, extrait, origine, code, publie) in nouveaux:
                item = {"domaine": dom, "titre": titre, "extrait": extrait, "origine": origine,
                        "code_vise": code, "publie_le": publie}
                motif = motif_rejet(item, r, recents)
                if motif:
                    cur.execute("UPDATE raw_items SET etat = 'filtre', motif_filtre = %s WHERE id = %s",
                                (motif, id_))
                    motifs[motif] += 1
                else:
                    cur.execute("UPDATE raw_items SET etat = 'a_qualifier' WHERE id = %s", (id_,))
                    recents.add(titre_normalise(titre))
                    motifs["retenu"] += 1
    retenus = motifs.pop("retenu", 0)
    print(f"{len(nouveaux)} examinés : {retenus} retenus, {sum(motifs.values())} filtrés {dict(motifs)}")
    print(json.dumps({"examines": len(nouveaux), "retenus": retenus, "filtres": sum(motifs.values()),
                      "motifs": dict(motifs)}, ensure_ascii=False))


if __name__ == "__main__":
    main()

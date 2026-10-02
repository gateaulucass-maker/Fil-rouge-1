"""Export Markdown des éléments validés, par axe puis par code, avec bibliographie numérotée.

  python scripts/export_fiche.py > rapports/fiche-veille.md
"""
from common import catalogue, connexion

TITRES_AXES = {"marche": "Marché", "concurrence": "Concurrence", "usagers": "Usagers",
               "techno": "Technologie", "reglementaire": "Réglementaire"}


def main():
    libelles = {c["code"]: c["libelle"] for c in catalogue()}
    ordre = list(TITRES_AXES)
    with connexion() as cx:
        lignes = cx.execute(
            """SELECT axe, code_info, titre, resume, pourquoi_important, pertinence, score_fiabilite, flux,
                      source_nom, url, publie_le, chiffres, irritant, verbatim, valide_par
               FROM veille_items WHERE statut = 'valide'
               ORDER BY code_info, pertinence DESC NULLS LAST, score_fiabilite DESC NULLS LAST""").fetchall()
    lignes.sort(key=lambda l: (ordre.index(l[0]), l[1] or "Z"))

    biblio, sortie = [], ["# Fiche de veille — Marché & réglementation silver tech", ""]
    axe_courant = code_courant = None
    for (axe, code, titre, resume, pourquoi, pert, score, flux, source, url, publie, chiffres,
         irritant, verbatim, par) in lignes:
        if axe != axe_courant:
            sortie += [f"## {TITRES_AXES[axe]}", ""]
            axe_courant, code_courant = axe, None
        if code != code_courant:
            sortie += [f"### {code or '—'} · {libelles.get(code, 'Non classé')}", ""]
            code_courant = code
        if url not in biblio:
            biblio.append(url)
        n = biblio.index(url) + 1
        info = f"pertinence {pert}/3" + (f" · fiabilité {score}/7" if flux == "fait" else f" · signal ({irritant})")
        sortie.append(f"- **{titre}** [{n}] — {info}")
        if resume:
            sortie.append(f"  {resume}")
        if pourquoi:
            sortie.append(f"  *Pour notre projet :* {pourquoi}")
        for c in chiffres or []:
            sortie.append(f"  - {c['valeur']} — {c.get('contexte', '')} (source citée : {c['source_citee']})")
        if verbatim:
            sortie.append(f"  > « {verbatim} »")
        sortie.append("")

    sortie += ["## Bibliographie", ""]
    sources = {l[9]: (l[8], l[10]) for l in lignes}
    for i, url in enumerate(biblio, 1):
        nom, date = sources[url]
        sortie.append(f"{i}. {nom or ''}{', ' + str(date) if date else ''}. <{url}>")
    if not lignes:
        sortie.append("_Aucun élément validé pour l'instant : lancer /revue._")
    print("\n".join(sortie))


if __name__ == "__main__":
    main()

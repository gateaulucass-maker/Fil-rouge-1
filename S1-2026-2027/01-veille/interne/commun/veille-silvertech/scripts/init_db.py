"""Crée le schéma et charge le catalogue. Peut être relancé sans erreur ni doublon."""
from common import RACINE, catalogue, connexion


def main():
    schema = (RACINE / "sql" / "schema.sql").read_text(encoding="utf-8")
    entrees = catalogue()
    with connexion() as cx:
        cx.execute(schema)
        with cx.cursor() as cur:
            cur.executemany(
                """INSERT INTO catalogue (code, axe, libelle, statut, phase_cible)
                   VALUES (%(code)s, %(axe)s, %(libelle)s, %(statut)s, %(phase_cible)s)
                   ON CONFLICT (code) DO UPDATE SET axe = EXCLUDED.axe, libelle = EXCLUDED.libelle,
                       statut = EXCLUDED.statut, phase_cible = EXCLUDED.phase_cible""",
                entrees,
            )
        n = cx.execute("SELECT count(*) FROM catalogue").fetchone()[0]
    print(f"Schéma OK, catalogue : {n} codes.")


if __name__ == "__main__":
    main()

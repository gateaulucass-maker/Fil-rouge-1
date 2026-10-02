-- Schéma de la base de veille silver tech (Neon / PostgreSQL)
-- Idempotent : peut être relancé sans erreur.

CREATE TABLE IF NOT EXISTS catalogue (
    code         TEXT PRIMARY KEY,
    axe          TEXT NOT NULL CHECK (axe IN ('marche','concurrence','usagers','techno','reglementaire')),
    libelle      TEXT NOT NULL,
    statut       TEXT NOT NULL CHECK (statut IN ('requis','bonus')),
    phase_cible  TEXT
);

CREATE TABLE IF NOT EXISTS raw_items (
    id           BIGSERIAL PRIMARY KEY,
    url          TEXT NOT NULL UNIQUE,
    domaine      TEXT NOT NULL,
    source_nom   TEXT,
    titre        TEXT NOT NULL,
    extrait      TEXT,
    origine      TEXT NOT NULL CHECK (origine LIKE 'rss:%' OR origine IN ('web_search','avis_app','reddit','manuel')),
    code_vise    TEXT REFERENCES catalogue(code),
    publie_le    DATE,
    collecte_le  TIMESTAMPTZ NOT NULL DEFAULT now(),
    etat         TEXT NOT NULL DEFAULT 'nouveau' CHECK (etat IN ('nouveau','filtre','a_qualifier','qualifie')),
    motif_filtre TEXT
);
CREATE INDEX IF NOT EXISTS raw_items_etat_idx ON raw_items (etat);

CREATE TABLE IF NOT EXISTS veille_items (
    id                    BIGSERIAL PRIMARY KEY,
    -- Champs de la base de veille du cours
    titre                 TEXT NOT NULL,
    publie_le             DATE,
    source_nom            TEXT,
    url                   TEXT NOT NULL,
    axe                   TEXT NOT NULL CHECK (axe IN ('marche','concurrence','usagers','techno','reglementaire')),
    resume                TEXT,
    pourquoi_important    TEXT,
    pertinence_proposee   SMALLINT CHECK (pertinence_proposee BETWEEN 1 AND 3),
    pertinence            SMALLINT CHECK (pertinence BETWEEN 1 AND 3),
    ajoute_par            TEXT NOT NULL DEFAULT 'agent',
    -- Champs du pipeline
    raw_id                BIGINT NOT NULL UNIQUE REFERENCES raw_items(id),
    code_info             TEXT REFERENCES catalogue(code),
    flux                  TEXT NOT NULL CHECK (flux IN ('fait','signal')),
    score_fiabilite       SMALLINT CHECK (score_fiabilite BETWEEN 0 AND 7),
    autorite              SMALLINT CHECK (autorite BETWEEN 0 AND 3),
    fraicheur             SMALLINT CHECK (fraicheur BETWEEN 0 AND 2),
    bonus_source_primaire SMALLINT CHECK (bonus_source_primaire BETWEEN 0 AND 2),
    source_primaire_url   TEXT,
    chiffres              JSONB NOT NULL DEFAULT '[]'::jsonb,
    archetype             TEXT CHECK (archetype IN ('securite','capteurs','sante_quotidien','compagnon','transverse')),
    ethique               BOOLEAN NOT NULL DEFAULT false,
    sensible              BOOLEAN NOT NULL DEFAULT false,
    irritant              TEXT CHECK (irritant IN ('stigmatisation','complexite','fausses_alertes','prix_abonnement',
                                                   'intrusion_vie_privee','fiabilite_technique','service_client','autre')),
    verbatim              TEXT CHECK (char_length(verbatim) <= 300),
    statut                TEXT NOT NULL DEFAULT 'a_revoir' CHECK (statut IN ('a_revoir','valide','rejete','hors_sujet')),
    valide_par            TEXT,
    commentaire           TEXT,
    revu_le               TIMESTAMPTZ,
    cree_le               TIMESTAMPTZ NOT NULL DEFAULT now()
);
CREATE INDEX IF NOT EXISTS veille_items_statut_axe_idx ON veille_items (statut, axe);

CREATE TABLE IF NOT EXISTS runs (
    id               BIGSERIAL PRIMARY KEY,
    demarre_le       TIMESTAMPTZ NOT NULL DEFAULT now(),
    termine_le       TIMESTAMPTZ,
    collectes        JSONB NOT NULL DEFAULT '{}'::jsonb,  -- nb collectés par origine
    nb_filtres       INTEGER NOT NULL DEFAULT 0,
    nb_qualifies     INTEGER NOT NULL DEFAULT 0,
    nb_hors_sujet    INTEGER NOT NULL DEFAULT 0,
    modele           TEXT,
    duree_secondes   INTEGER,
    notes            TEXT
);

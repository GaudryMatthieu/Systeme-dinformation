CREATE TABLE achats (
  PRIMARY KEY (client_id, jeu_de_societe_id, magasin_id),
  client_id         SERIAL NOT NULL,
  jeu_de_societe_id SERIAL NOT NULL,
  magasin_id        SERIAL NOT NULL,
  date_achat        TIMESTAMP
);

CREATE TABLE client (
  PRIMARY KEY (client_id),
  client_id SERIAL,
  age       INT CHECK(age >= 18),
  email     VARCHAR(42) CHECK(regexp_like(email, '[a-zA-Z0-9_]+?@[a-z0-9]+\.[a-z0-9]')),
  nom       VARCHAR(42)
);

CREATE TABLE editeur (
  PRIMARY KEY (editeur_id),
  editeur_id     SERIAL,
  raison_sociale VARCHAR(42),
  siege_social   VARCHAR(42)
);

CREATE TABLE jeu_de_societe (
  PRIMARY KEY (jeu_de_societe_id),
  jeu_de_societe_id SERIAL NOT NULL,
  type              VARCHAR(42) CHECK(type in('RPG', 'PUZZLE')),
  age               INT CHECK(age > 0),
  titre             VARCHAR(42),
  nb_joueurs        INT CHECK(nb_joueurs > 0),
  editeur_id        SERIAL NOT NULL
);

CREATE TABLE magasin (
  PRIMARY KEY (magasin_id),
  magasin_id SERIAL NOT NULL,
  website    VARCHAR(42)
);

CREATE TABLE vend (
  PRIMARY KEY (magasin_id, jeu_de_societe_id),
  magasin_id        SERIAL NOT NULL,
  jeu_de_societe_id SERIAL NOT NULL,
  prix              INT CHECK(prix >= 0)
);

ALTER TABLE achats ADD FOREIGN KEY (magasin_id) REFERENCES magasin (magasin_id);
ALTER TABLE achats ADD FOREIGN KEY (jeu_de_societe_id) REFERENCES jeu_de_societe (jeu_de_societe_id);
ALTER TABLE achats ADD FOREIGN KEY (client_id) REFERENCES client (client_id);

ALTER TABLE jeu_de_societe ADD FOREIGN KEY (editeur_id) REFERENCES editeur (editeur_id);

ALTER TABLE vend ADD FOREIGN KEY (jeu_de_societe_id) REFERENCES jeu_de_societe (jeu_de_societe_id);
ALTER TABLE vend ADD FOREIGN KEY (magasin_id) REFERENCES magasin (magasin_id);
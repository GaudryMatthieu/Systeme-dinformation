magasin(**magasin_id**,website)

éditeur(**editeur_id**,raison sociale,siège social)

jeu de société(**jeu_de_societe_id**,type, age, titre, nb_joueurs,*editeur_id*)

magasin_vend_jeu_de_societe(*magasin_id*,*jeu_de_societe_id*, prix)

client(**client_id**, age, email)

achats(*client_id*, *jeu_de_societe_id*, *magasin_id*, date_achat)
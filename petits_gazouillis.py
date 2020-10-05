from app import app, db, modeles
from app.modeles import Utilisateur, Publication
import os, csv


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'U': Utilisateur, 'P': Publication}


print("Denarrage petit gazouillis")

@app.before_first_request
def initialisation():
    print("initialisation")
    tables= app.config['BD_TABLES_EFFACER']
    for table in tables:
        requete = "delete from {}".format(table)
        print(requete)
        db.session.execute(requete)
    db.session.commit()

    tables = app.config['BD_TABLES_CREER']
    racine = os.path.abspath(os.path.dirname(__file__))
    for table in tables:
        fichier = 'csv/' + table + '.csv'
        if os.path.exists(racine + '/' + fichier):
            source = os.path.join(racine, fichier)

            print("===" + table + "===")
            with open(source) as fichier_csv:
                lecteur_csv = csv.reader(fichier_csv, delimiter=',')
                for ligne in lecteur_csv:
                    element = modeles.get_modele(table, ligne, racine)
                    print (element)

                    if element is not None:
                        db.session.add(element)
                    db.session.commit()

    u1 = Utilisateur.query.filter_by(nom='Harry').first_or_404()
    u2 = Utilisateur.query.filter_by(nom='Hermione').first_or_404()
    u3 = Utilisateur.query.filter_by(nom='Ron').first_or_404()
    u1.devenir_partisan(u2)
    u1.devenir_partisan(u3)
    u2.devenir_partisan(u1)
    db.session.commit()
    print("Liste des publications suivies par {} (incluant ses propres publications)".format(u1.nom))
    for p in u1.liste_publications_dont_je_suis_partisan():
        print("auteur: {} corps: {}".format(p.auteur.nom, p.corps))
    u1.devenir_partisan(u3)
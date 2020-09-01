from flask import render_template, flash, redirect
from app import app
from app.formulaires import FormulaireEtablirSession

@app.route('/')
@app.route('/index')
def index():
    user = {'nom': 'Ankit'}
    publications = [
        {
            'auteur': {'nom': 'Jean'},
            'corps': "J'aime rien!"
        },
        {
            'auteur': {'nom': 'John'},
            'corps': "J'hais tout!"
        }
    ]
    return render_template('index.html', titre='Acceuil', utilisateur=user, publications=publications)


@app.route('/etablir_session', methods=['GET', 'POST'])
def etablir_session():
    formulaire = FormulaireEtablirSession()
    if formulaire.validate_on_submit():
            flash('Etablir une session par utilisateur {}, se_souvenir_de_moi ={}'.format(formulaire.nom.data, formulaire.se_souvenir_de_moi.data))
            return redirect('/index')
    return render_template('etablir_session.html', titre='Etablir une session', formulaire=formulaire)

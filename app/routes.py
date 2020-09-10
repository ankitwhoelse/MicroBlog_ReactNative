from flask import render_template, flash, redirect
from app import app
from app.formulaires import FormulaireEtablirSession
from app.modeles import Utilisateur

@app.route('/')
@app.route('/index')
def index():
    
    utilisateurs = Utilisateur.query.all()

    return render_template('index.html', titre='Acceuil', utilisateurs=utilisateurs)



@app.route('/etablir_session', methods=['GET', 'POST'])
def etablir_session():

    formulaire = FormulaireEtablirSession()
    if formulaire.validate_on_submit():
            flash('Etablir une session par utilisateur {}, se_souvenir_de_moi ={}'.format(formulaire.nom.data, formulaire.se_souvenir_de_moi.data))
            return redirect('/index')
    return render_template('etablir_session.html', titre='Etablir une session', formulaire=formulaire)

from flask import render_template
from app import app

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
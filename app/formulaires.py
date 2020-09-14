from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo
from app.modeles import Utilisateur

class FormulaireEtablirSession(FlaskForm):
    nom = StringField('Nom', validators=[DataRequired(message="Nom est un champ oubligatoire")])
    mot_de_passe = PasswordField('Mot de passe', validators=[DataRequired(message="Mot de passe est un champ oubligatoire")])
    se_souvenir_de_moi = BooleanField('Se souvenir de moi')
    soumettre = SubmitField('Etablir une session')

class FormulaireEnregistrement(FlaskForm):
    nom = StringField('Nom', validators=[DataRequired()])
    courriel = StringField('Courriel', validators=[DataRequired(), Email()])
    mot_de_passe = PasswordField('Mot de passe', validators=[DataRequired()])
    mot_de_passe2 = PasswordField('Mot de passe (entrer a nouveau)', validators=[DataRequired(), EqualTo('mot_de_passe')])
    soumettre = SubmitField('Enregistrer')

    def validate_nom(self, nom):
        utilisateur = Utilisateur.query.filter_by(nom=nom.data).first()
        if utilisateur is not None:
            raise ValidationError('Ce nom existe deja.')

    def validate_courriel(self, courriel):
        utilisateur = Utilisateur.query.filter_by(courriel=courriel.data).first()
        if utilisateur is not None:
            raise ValidationError('Ce courriel existe deja.')
from app.api import bp
from app.modeles import Utilisateur, PaginatedAPIMixin
from flask import jsonify
from flask import request

@bp.route('/utilisateurs2', methods=['GET'])
def get_utilisateurs2():
    return "utilisateurs2"

# CRUD: Create, Read, Update, Delete

# Lire un utilisateur
@bp.route('/utilisateurs/<int:id>', methods=['GET'])
def get_utilisateur(id):
    return jsonify(Utilisateur.query.get_or_404(id).to_dict())

# Lire tous les utilisateurs
@bp.route('/utilisateurs', methods=['GET'])
def get_utilisateurs():
    page = request.args.get('page', 1, type=int)
    par_page = min(request.args.get('par_page', 10, type=int), 100)
    data = Utilisateur.to_collection_dict(Utilisateur.query, page, par_page, 'api.get_publications')

    return jsonify(data)

# Creer
@bp.route('/utilisateurs', methods=['POST'])
def creer_utilisateur():
    return "Creer"

# Modifier
@bp.route('/utilisateurs/<int:id>', methods=['PUT'])
def modifier_utilisateur(id):
    return "Modifier"

# Supprimer
@bp.route('/utilisateurs/<int:id>', methods=['DELETE'])
def supprimer_utilisateur(id):
    return "Supprimer"

    

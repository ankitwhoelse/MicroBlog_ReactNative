from app.api import bp
from flask import jsonify
from app import db
from app.api.auth import basic_auth
from app.api.auth import token_auth

@bp.route('/jeton2', methods=['GET'])
def get_jeton2():
    return 'jeton2'

@bp.route('/jeton', methods=['GET'])
@basic_auth.login_required
def get_jeton():
    print('get_jeton')
    jeton = basic_auth.current_user().get_jeton()
    db.session.commit()
    return jsonify({'jeton': jeton})

@bp.route('/jeton', methods=['DELETE'])
@token_auth.login_required
def effacer_jeton():
    token_auth.current_user().revoquer_jeton()
    db.session.commit()
    return '', 204
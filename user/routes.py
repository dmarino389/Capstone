from flask import Blueprint, request, jsonify, abort
from .models import User, db
from flask_jwt_extended import jwt_required, get_jwt_identity

user_bp = Blueprint('user', __name__)

# Endpoint to get the current user's profile
@user_bp.route('/profile', methods=['GET'])
@jwt_required()
def get_user_profile():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if user:
        return jsonify(user.to_dict()), 200
    else:
        abort(404, description="User not found.")

# Endpoint to update the current user's profile
@user_bp.route('/profile', methods=['PUT'])
@jwt_required()
def update_user_profile():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    
    if user:
        data = request.get_json()
        # Assuming you have fields like username and email in your user model
        user.username = data.get('username', user.username)
        user.email = data.get('email', user.email)
        
        db.session.commit()
        return jsonify(user.to_dict()), 200
    else:
        abort(404, description="User not found.")

# You might have other routes like changing password, deleting account, etc.

from flask import Blueprint, request, jsonify, abort
from ..models import Hotel, DestinationPost, Like
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db

hotel_bp = Blueprint('hotel', __name__, url_prefix='/api/hotel')

# Endpoint to get all destination posts
@hotel_bp.route('/destinations', methods=['GET'])
def get_destinations():
    destinations = DestinationPost.query.all()
    return jsonify([dest.to_dict() for dest in destinations]), 200

# Endpoint to post a new destination
@hotel_bp.route('/destinations', methods=['POST'])
@jwt_required()
def post_destination():
    user_id = get_jwt_identity()
    data = request.get_json()

    destination = DestinationPost(
        title=data['title'],
        description=data['description'],
        location=data['location'],
        user_id=user_id
    )

    db.session.add(destination)
    db.session.commit()

    return jsonify(destination.to_dict()), 201

# Other endpoints like update, delete, like, etc. will go here


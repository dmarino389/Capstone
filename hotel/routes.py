from flask import Blueprint, request, jsonify, abort
from .models import db, DestinationPost, Like
from flask_jwt_extended import jwt_required, get_jwt_identity

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

# Endpoint to like a destination post
@hotel_bp.route('/destinations/<int:post_id>/like', methods=['POST'])
@jwt_required()
def like_destination(post_id):
    user_id = get_jwt_identity()
    like = Like(user_id=user_id, post_id=post_id)
    
    db.session.add(like)
    db.session.commit()

    return jsonify(message="Liked successfully"), 200

# Endpoint to update a destination post
@hotel_bp.route('/destinations/<int:post_id>', methods=['PUT'])
@jwt_required()
def update_destination(post_id):
    user_id = get_jwt_identity()
    data = request.get_json()

    post = DestinationPost.query.get_or_404(post_id)
    if post.user_id != user_id:
        abort(403)

    post.title = data.get('title', post.title)
    post.description = data.get('description', post.description)
    post.location = data.get('location', post.location)

    db.session.commit()
    return jsonify(post.to_dict()), 200

# Endpoint

from datetime import datetime
from app import db
from sqlalchemy.orm import relationship

class DestinationPost(db.Model):
    __tablename__ = 'destination_posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    location = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)  # Assuming your user table is named 'users'
    likes = relationship('Like', backref='destination_post', lazy=True)
    # other fields such as images, dates, etc.

class Like(db.Model):
    __tablename__ = 'likes'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)  # Assuming your user table is named 'users'
    post_id = db.Column(db.Integer, db.ForeignKey('destination_posts.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# You might also have other models, such as Comment, Image, etc.

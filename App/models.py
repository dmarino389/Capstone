from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from werkzeug.security import generate_password_hash

db = SQLAlchemy()

followers = db.Table('followers', 
    db.Column('follower_id', db.Integer, db.ForeignKey('user.id'), nullable=False),
    db.Column('followed_id', db.Integer, db.ForeignKey('user.id'), nullable=False)
    )


class Product(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), nullable = False)
  description = db.Column(db.String(500))
  img_url = db.Column(db.String, nullable = False)


  def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'img_url': self.img_url
        }
  
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(45), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    first_name = db.Column(db.String(45))
    
    posts = db.relationship("Post", backref='author')
    following = db.relationship(
        'User',
        backref='followers',
        secondary='followers',
        primaryjoin=(followers.c.follower_id == id),
        secondaryjoin=(followers.c.followed_id == id)
    )

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    img_url = db.Column(db.String, nullable=False)
    caption = db.Column(db.String(500))
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    last_updated = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    likers = db.relationship("User", backref='liked_posts', secondary='like')

    def __init__(self, title, img_url, caption, user_id):
        self.title = title
        self.img_url = img_url
        self.caption = caption
        self.user_id = user_id

    def like_count(self):
        return len(self.likers)
    
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'caption': self.caption,
            'img_url': self.img_url,
            'user_id': self.user_id,
            'author': self.author.username,
            'date_created': self.date_created,
            'last_updated': self.last_updated,
            'like_count': self.like_count(),
        }

like = db.Table('like',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), nullable=False, primary_key=True),
    db.Column('post_id', db.Integer, db.ForeignKey('post.id'), nullable=False, primary_key=True),
)

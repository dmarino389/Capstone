from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

# Initialize extensions
db = SQLAlchemy()
jwt = JWTManager()

def create_app(config_name):
    app = Flask(__name__)

    # Load configurations
    app.config.from_object(config_name)

    # Initialize extensions with app
    db.init_app(app)
    jwt.init_app(app)

    # Register blueprints
    from ..auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/api/auth')

    from ..hotel import hotel as hotel_blueprint
    app.register_blueprint(hotel_blueprint, url_prefix='/api/hotel')

    from ..models import user as user_blueprint
    app.register_blueprint(user_blueprint, url_prefix='/api/user')

    return app

from flask import Flask
from config import Config
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_moment import Moment

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Extensions
    from .models import db, User  # Ensure your models are imported correctly
    db.init_app(app)
    migrate = Migrate(app, db)  # Handles database migrations
    login = LoginManager(app)  # Manages user login sessions
    login.login_view = 'login'  # Specifies the login view
    moment = Moment(app)  # Manages date and time

    # Register Blueprints
    from app.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    from app.hotel import hotel as hotel_blueprint
    app.register_blueprint(hotel_blueprint, url_prefix='/hotel')

    from app.user import user as user_blueprint
    app.register_blueprint(user_blueprint, url_prefix='/user')

    return app

# Outside the create_app function, you instantiate the app
app = create_app()

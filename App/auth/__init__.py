from flask import Flask
from ..auth import auth as auth_blueprint

def create_app():
    app = Flask(__name__)
    
    # Register the auth Blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    
    return app

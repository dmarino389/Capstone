from flask import Flask
from ..hotel import hotel as hotel_blueprint

def create_app():
    app = Flask(__name__)
    
    # Register the hotel Blueprint
    app.register_blueprint(hotel_blueprint, url_prefix='/hotel')
    
    return app

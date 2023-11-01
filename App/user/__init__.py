from flask import Blueprint

# Initialize the user Blueprint with the name 'user' and a URL prefix of '/user'
user = Blueprint('user', __name__)

# Import the routes module to make the routes available to the application
from . import routes

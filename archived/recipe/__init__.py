from flask import Blueprint

# Create the Blueprint instance
recipe_bp = Blueprint('recipe', __name__)

# Import the routes to register them with the Blueprint
from . import recipe_route

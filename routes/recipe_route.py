from flask import request, jsonify, Blueprint
from controllers import recipe_controller


recipe_bp = Blueprint('recipe', __name__)

# GET handler for /weather
@recipe_bp.route('/recipe', methods=['GET'])
def get_recipe():
    return recipe_controller.get_recipe(request.get_json())

# POST handler for /weather
@recipe_bp.route('/recipe', methods=['POST'])
def add_recipe():
    return recipe_controller.post_recipe(request.get_json())

# PUT handler for /weather
@recipe_bp.route('/recipe', methods=['PUT'])
def update_recipe():
    return recipe_controller.update_recipe(request.get_json())

# DELETE handler for /weather
@recipe_bp.route('/recipe', methods=['DELETE'])
def delete_recipe():
    return recipe_controller.delete_recipe(request.get_json())


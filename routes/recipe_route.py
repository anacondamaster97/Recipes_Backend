from flask import request, jsonify, Blueprint
from controllers import recipe_controller


recipe_bp = Blueprint('recipe', __name__)

# GET handler for /weather
@recipe_bp.route('/recipe', methods=['GET'])
def get_recipe():
    print(recipe_controller.get_all_recipes())
    return recipe_controller.get_recipe(request.get_json())

# POST handler for /weather
@recipe_bp.route('/recipe', methods=['POST'])
def add_recipe():
    return recipe_controller.post_recipe(request.get_json())

# PUT handler for /weather
@recipe_bp.route('/recipe', methods=['PUT'])
def update_recipe():
    data = request.get_json()
    return recipe_controller.update_recipe(data)

# DELETE handler for /weather
@recipe_bp.route('/recipe', methods=['DELETE'])
def delete_recipe():
    data = request.get_json()
    return recipe_controller.delete_recipe(data)


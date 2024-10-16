from flask import request, jsonify, Blueprint
from controllers.recipe import recipe_controller


recipe_bp = Blueprint('recipe', __name__)

@recipe_bp.route('/recipe', methods=['GET'])
def get_recipe():
    return recipe_controller.get_recipe(request.get_json())

@recipe_bp.route('/recipe/all', methods=['GET'])
def get_all_recipes():
    return recipe_controller.get_all_recipes()

@recipe_bp.route('/recipe', methods=['POST'])
def add_recipe():
    return recipe_controller.post_recipe(request.get_json())

@recipe_bp.route('/recipe', methods=['PUT'])
def update_recipe():
    return recipe_controller.update_recipe(request.get_json())

@recipe_bp.route('/recipe', methods=['DELETE'])
def delete_recipe():
    return recipe_controller.delete_recipe(request.get_json())


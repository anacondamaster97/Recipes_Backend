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
    data = request.get_json()
    return recipe_controller.post_recipe(data)

# PUT handler for /weather
@recipe_bp.route('/recipe', methods=['PUT'])
def update_recipe():
    data = request.get_json()
    city = data.get('city')
    weather = data.get('weather')

    if not city or not weather:
        return jsonify({"error": "City and weather information are required"}), 400

    if city not in recipe_data:
        return jsonify({"error": "City not found"}), 404

    recipe_data[city] = weather
    return jsonify({"message": f"Weather for {city} updated"}), 200

# DELETE handler for /weather
@recipe_bp.route('/recipe', methods=['DELETE'])
def delete_recipe():
    data = request.get_json()
    city = data.get('city')

    if not city:
        return jsonify({"error": "City is required"}), 400

    if city in recipe_data:
        del recipe_data[city]
        return jsonify({"message": f"Weather for {city} deleted"}), 200
    else:
        return jsonify({"error": "City not found"}), 404

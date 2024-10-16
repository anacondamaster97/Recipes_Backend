from flask import request, jsonify
from . import recipe_bp
#from ../controllers/recipes_contollers import get_recipe

# In-memory data store for demonstration purposes
recipe_data = {
"recipes": [{
    "Name":"Alfredo Pasta", "Ingredients":"Cheese, Creme, Pasta, Salt", "Country":"Italy"
}]
}

# GET handler for /weather
@recipe_bp.route('/recipe', methods=['GET'])
def get_recipe():
    data = request.get_json()
    recipes = recipe_data["recipes"]
    for recipe in recipes:
        if recipe["Name"] == data["Name"]:
            return jsonify(recipe_data), 200
    
    return jsonify({"error": "Recipe not found"}), 404

# POST handler for /weather
@recipe_bp.route('/recipe', methods=['POST'])
def add_recipe():
    data = request.get_json()
    city = data.get('city')
    weather = data.get('weather')

    if not city or not weather:
        return jsonify({"error": "City and weather information are required"}), 400

    recipe_data[city] = weather
    return jsonify({"message": f"Weather for {city} added"}), 201

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

from flask import jsonify
from pony.orm import *
from models import recipe_model

"""
{
    "user":"Subha","name":"Alfredo Pasta"
}
"""
@db_session
def get_recipe(data):

    if 'user' not in data or 'name' not in data: return jsonify({"error": "User or Name not recieved"}), 404

    user, name = data['user'], data['name']
    recipes = select(recipe for recipe in recipe_model.Recipe if recipe.name == name and recipe.user == user)[:]

    if not recipes: return jsonify({"error": "Recipe not found"}), 404
    
    return jsonify({"user":recipes[0].user,"name":recipes[0].name, "ingredients":recipes[0].ingredients, "country":recipes[0].country}), 200 
    
"""
{
    "user":"Uppili","name":"Alfredo Pasta", "ingredients":"Cheese, Pasta, Salt", "country":"Italy"
}
"""
@db_session
def post_recipe(data):

    required = ["user","name","ingredients","country"]
    inside = []
    for elems in required:
        if elems not in data:
            inside.append(elems)
    if inside: return jsonify({"error": ''.join(inside) + " required"}), 400

    name = data.get('name')
    user = data.get('user')
    ingredients = data.get('ingredients')
    country = data.get('country')

    recipes = select(recipe for recipe in recipe_model.Recipe if recipe.name == name and recipe.user == user)[:]
    if recipes:
        return jsonify({"error": "Recipe and User already exists"}), 400

    recipe = recipe_model.Recipe(user=user,name=name,ingredients=ingredients,country=country)
    commit()
    return jsonify({"message": f"Recipe for {name} created by {user}"}), 200
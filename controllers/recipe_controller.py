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
    recipes = select(recipe for recipe in recipe_model.Recipe if recipe.name == name and recipe.user.user == user)[:]

    if not recipes: return jsonify({"error": "Recipe not found"}), 404
    
    return jsonify({"user":recipes[0].user.user,"name":recipes[0].name, "ingredients":recipes[0].ingredients, "country":recipes[0].country}), 200 
    
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

    recipes = select(recipe for recipe in recipe_model.Recipe if recipe.name == name and recipe.user.user == user)[:]
    if recipes:
        return jsonify({"error": "Recipe and User already exists"}), 400
    if not recipe_model.Creator.get(user=user):
        return jsonify({"error": "User does not exist"}), 400
    recipe = recipe_model.Recipe(user=recipe_model.Creator.get(user=user),name=name,ingredients=ingredients,country=country)
    commit()
    return jsonify({"message": f"Recipe for {name} created by {user}"}), 200

@db_session
def update_recipe(data):

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

    recipes = select(recipe for recipe in recipe_model.Recipe if recipe.name == name and recipe.user.user == user)[:]
    print(recipes)
    if not recipes:
        return jsonify({"error": "Recipe and User does not exists"}), 400
    if not recipe_model.Creator.get(user=user):
        return jsonify({"error": "User does not exist"}), 400
    recipe = recipe_model.Recipe.get(user=recipe_model.Creator.get(user=user),name=name)
    recipe.ingredients, recipe.country = ingredients, country
    commit()
    return jsonify({"message": f"Recipe for {name} created by {user} updated"}), 200

@db_session
def delete_recipe(data):

    required = ["user","name"]
    inside = []
    for elems in required:
        if elems not in data:
            inside.append(elems)
    if inside: return jsonify({"error": ''.join(inside) + " required"}), 400

    name = data.get('name')
    user = data.get('user')

    recipes = select(recipe for recipe in recipe_model.Recipe if recipe.name == name and recipe.user.user == user)[:]
    if not recipes:
        return jsonify({"error": "Recipe and User does not exist in database"}), 400

    recipe = recipe_model.Recipe.get(user=recipe_model.Creator.get(user=user),name=name)
    recipe.delete()
    commit()
    return jsonify({"message": f"Recipe for {name} created by {user} deleted"}), 200

@db_session
def get_all_recipes():

    data = select(recipe for recipe in recipe_model.Recipe)[:]
    data = [(recipe.name, recipe.user, recipe.ingredients, recipe.country) for recipe in data]
    return {"data":data}

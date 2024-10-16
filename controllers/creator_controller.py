from flask import jsonify
from pony.orm import *
from models import recipe_model

"""
{
    "user":"Subha","name":"Alfredo Pasta"
}
"""
@db_session
def get_creator(data):
    
    if 'user' not in data or 'name' not in data: return jsonify({"error": "User or Name not recieved"}), 404

    user = data['user']
    creators = select(creator for creator in recipe_model.Creator if creator.user == user)[:]

    if not creators: return jsonify({"error": "Creator not found"}), 404
    
    return jsonify({"user":creators[0].user}), 200 
    
"""
{
    "user":"Uppili","name":"Alfredo Pasta", "ingredients":"Cheese, Pasta, Salt", "country":"Italy"
}
"""
@db_session
def post_creator(data):

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

    creators = select(creator for creator in recipe_model.Creator if creator.user == user)[:]
    if creators:
        return jsonify({"error": "Creator already exists"}), 400
    
    creator = recipe_model.Creator(user=user)
    commit()
    return jsonify({"message": f"Recipe for {name} created by {user}"}), 200

@db_session
def update_creator(data):

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

    creators = select(creator for creator in recipe_model.Creator if creator.user == user)[:]
    print(creators)
    if not creators:
        return jsonify({"error": "User does not exists"}), 400
              
    creator = recipe_model.Creator.get(user=user)
    creator.ingredients, creator.country = ingredients, country
    commit()
    return jsonify({"message": f"{user} updated"}), 200

@db_session
def delete_creator(data):

    required = ["user","name"]
    inside = []
    for elems in required:
        if elems not in data:
            inside.append(elems)
    if inside: return jsonify({"error": ''.join(inside) + " required"}), 400

    name = data.get('name')
    user = data.get('user')

    creators = select(creator for creator in recipe_model.Creator if creator.user == user)[:]
    if not creators:
        return jsonify({"error": "Creator does not exist in database"}), 400

    creator = recipe_model.Creator.get(user=user)
    creator.delete()
    commit()
    return jsonify({"message": f"{user} deleted"}), 200

@db_session
def get_all_creators():

    data = select(creator for creator in recipe_model.Creator)[:]
    data = [(creator.user) for creator in data]
    return {"data":data}

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

    required = ["user"]
    inside = []
    for elems in required:
        if elems not in data:
            inside.append(elems)
    if inside: return jsonify({"error": ''.join(inside) + " required"}), 400

    user = data.get('user')


    creators = select(creator for creator in recipe_model.Creator if creator.user == user)[:]
    if creators:
        return jsonify({"error": "Creator already exists"}), 400
    
    creator = recipe_model.Creator(user=user)
    commit()
    return jsonify({"message": f"{user} created"}), 200

@db_session
def update_creator(data):

    required = ["user"]
    inside = []
    for elems in required:
        if elems not in data:
            inside.append(elems)
    if inside: return jsonify({"error": ''.join(inside) + " required"}), 400

    user = data.get('user')


    creators = select(creator for creator in recipe_model.Creator if creator.user == user)[:]
    print(creators)
    if not creators:
        return jsonify({"error": "User does not exists"}), 400
              
    creator = recipe_model.Creator.get(user=user)
    commit()
    return jsonify({"message": f"{user} updated"}), 200

@db_session
def delete_creator(data):

    required = ["user"]
    inside = []
    for elems in required:
        if elems not in data:
            inside.append(elems)
    if inside: return jsonify({"error": ''.join(inside) + " required"}), 400

    user = data.get('user')

    creators = select(creator for creator in recipe_model.Creator if creator.user == user)[:]
    if not creators:
        return jsonify({"error": "Creator does not exist in database"}), 400

    creator = recipe_model.Creator.get(user=user)
    creator.delete()
    commit()
    return jsonify({"message": f"{user} deleted"}), 200

@db_session
def get_all_creator_recipes(json_data):
    if 'user' not in json_data: return jsonify({"error": "user required"}), 400
    user = json_data['user']
    data = select(creator for creator in recipe_model.Creator if creator.user == user)[:]
    data = [(recipe) for recipe in data[0].recipes]

    data = [{"user":user,"name":recipe.name, "ingredients":recipe.ingredients, "country":recipe.country} for recipe in data]
    return {"data":data}

@db_session
def get_all_creators():

    data = select(creator for creator in recipe_model.Creator)[:]
    data = [(creator.user) for creator in data]
    return {"data":data}

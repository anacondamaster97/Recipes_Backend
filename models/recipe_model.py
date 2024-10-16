from pony.orm import *

db = Database()

class Creator(db.Entity):
    user = Required(str, unique=True)
    recipes = Set('Recipe')
    followers = Set('Creator', reverse='following')
    following = Set('Creator', reverse='followers')
    

class Recipe(db.Entity):
    user = Required(Creator)
    name = Required(str)
    ingredients = Required(str)
    country = Required(str)

db.bind(provider='sqlite', filename='../database.sqlite', create_db=True)
db.generate_mapping(create_tables=True)

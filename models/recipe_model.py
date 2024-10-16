from pony.orm import *

db = Database()

class Recipe(db.Entity):
	user = Required(str)
	name = Required(str)
	ingredients = Required(str)
	country = Required(str)

db.bind(provider='sqlite', filename='../database.sqlite', create_db=True)

db.generate_mapping(create_tables=True)

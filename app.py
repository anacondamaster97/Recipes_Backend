from flask import Flask

# Blueprints
from routes.recipe_route import recipe_bp

app = Flask(__name__)

# Register blueprints
app.register_blueprint(recipe_bp)

if __name__ == '__main__':
    app.run(debug=True)

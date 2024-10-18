from flask import Flask

# Blueprints
from routes.recipe.recipe_route import recipe_bp
from routes.creator.creator_route import creator_bp
from routes.deletion.deletion_route import deletion_bp

app = Flask(__name__)

# Register blueprints
app.register_blueprint(recipe_bp)
app.register_blueprint(creator_bp)
app.register_blueprint(deletion_bp)

if __name__ == '__main__':
    app.run(debug=True)
"""
if __name__ == '__main__':
    # When running the app locally (not using Gunicorn), use this block
    # Gunicorn will directly run 'app' without calling this block
    app.run(host='0.0.0.0', port=8000, debug=False)
"""
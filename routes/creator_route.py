from flask import request, jsonify, Blueprint
from controllers import creator_controller


creator_bp = Blueprint('creator', __name__)

# GET handler for /weather
@creator_bp.route('/creator', methods=['GET'])
def get_creator():
    return creator_controller.get_all_creators()
    #return creator_controller.get_creator(request.get_json())


# POST handler for /weather
@creator_bp.route('/creator', methods=['POST'])
def add_creator():
    return creator_controller.post_creator(request.get_json())

# PUT handler for /weather
@creator_bp.route('/creator', methods=['PUT'])
def update_creator():
    return creator_controller.update_creator(request.get_json())

# DELETE handler for /weather
@creator_bp.route('/creator', methods=['DELETE'])
def delete_creator():
    return creator_controller.delete_creator(request.get_json())


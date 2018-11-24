from flask import jsonify
from flask_restful import Resource
from controllers.user_controller import UserController

class UserResource(Resource):
    """
    Check API Endpoints
    """
    def post(self, auth_id):
        UserController.create(auth_id)

    def get(self, auth_id):
        return jsonify({
            'data': {
                'user': UserController.get_auth_id(auth_id)
            }
        })
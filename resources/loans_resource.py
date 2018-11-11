from flask import jsonify
from flask_restful import Resource, reqparse

class LoansResource(Resource):
    """
    Users API Endpoints
    """
    def post(self):
        """
        Create loan object
        :return response: JSON. Ie, jsonify
        """
        return {}, 200

    def get(self):
        """
        Return loan object
        :return:
        """
        loans = [
            'Elemento 1 de la lista',
            'Elemento 2 de la lista',
            'Elemento 3 de la lista',
            'Elemento 4 de la lista'
        ]
        return jsonify({
            'data': {
                'loans': loans
            }
        })
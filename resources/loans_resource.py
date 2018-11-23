from flask import jsonify
from flask_restful import Resource, reqparse
from controllers.loans_controller import LoanController

class LoansResource(Resource):
    def post(self):
        args = self.__get_request_parameters()
        LoanController.create(args)
        return {}, 200

    def get(self):
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

    @staticmethod
    def __get_request_parameters():
        parser = reqparse.RequestParser()
        parser.add_argument('value', type=str, required=False, help='send_email')
        parser.add_argument('interest', type=int, required=False, help='send_email')
        parser.add_argument('sold_percent', type=int, required=False, help='send_email')
        parser.add_argument('investor', type=str, required=False, help='send_email')
        parser.add_argument('product_type', type=str, required=False, help='send_email')

        return parser.parse_args()
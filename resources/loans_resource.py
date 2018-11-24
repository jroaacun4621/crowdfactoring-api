from flask import jsonify
from flask_restful import Resource, reqparse
from controllers.loans_controller import LoanController

class LoansResource(Resource):
    def post(self, user_id):
        args = self.__get_request_parameters()
        LoanController.create(args, user_id)
        return {}, 200

    def get(self, user_id):
        return jsonify({
            'data': {
                'loans': LoanController.get_all(user_id)
            }
        })

    @staticmethod
    def __get_request_parameters():
        parser = reqparse.RequestParser()
        parser.add_argument('value', type=str, required=False, help='value')
        parser.add_argument('interest', type=int, required=False, help='interest')
        parser.add_argument('sold_percent', type=int, required=False, help='sold percent')
        parser.add_argument('investor', type=str, required=False, help='investor')
        parser.add_argument('product_type', type=str, required=False, help='product type')

        return parser.parse_args()
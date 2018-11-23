from flask_restful import Resource
from controllers.loans_controller import LoanController

class CheckResource(Resource):
    """
    Check API Endpoints
    """
    def get(self):
        return "It's working."
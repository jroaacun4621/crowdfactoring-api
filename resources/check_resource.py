from flask_restful import Resource

class CheckResource(Resource):
    """
    Check API Endpoints
    """
    def get(self):
        return "It's working."
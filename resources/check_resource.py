from flask_restful import Resource

class CheckResource(Resource):
    """
    Check API Endpoints
    """
    def get(self):
        from managers.user_manager import UserManager
        UserManager.create('a')
        print(UserManager.get_auth_id('a'))
        return "It's working."
from managers.user_manager import UserManager

class UserController(object):
    @staticmethod
    def create(auth_id):
        UserManager.create(auth_id)

    @staticmethod
    def get_auth_id(auth_id):
        return UserManager.get_auth_id(auth_id)
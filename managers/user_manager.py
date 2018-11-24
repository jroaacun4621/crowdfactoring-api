from models import db, User
from utils.db_utils import create_autocommit_session
from schemas.UserSchema import UserSchema

class UserManager(object):
    @staticmethod
    def create(auth_id):
        try:
            session = create_autocommit_session(db)
            with session.begin():
                obj = User(
                    auth_id=auth_id
                )
                session.add(obj)
        except Exception as e:
            raise

    @staticmethod
    def get_auth_id(auth_id):
        try:
            session = create_autocommit_session(db)
            with session.begin():
                user = session.query(User).filter_by(auth_id=auth_id).first()
                user_fields = ('id', 'auth_id')
                user_schema = UserSchema(many=False, only=user_fields)
            return user_schema.dump(user).data
        except Exception as e:
            raise
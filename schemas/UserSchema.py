from marshmallow import Schema
from models import User

class UserSchema(Schema):
    class Meta:
        Model = User
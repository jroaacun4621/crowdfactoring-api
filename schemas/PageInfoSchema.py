from marshmallow import Schema
from models import PageInfo

class PageInfoSchema(Schema):
    class Meta:
        Model = PageInfo
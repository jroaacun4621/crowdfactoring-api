from marshmallow import Schema, fields, pprint
from models import db, PageInfo
from datetime import date

class PageInfoSchema(Schema):
    class Meta:
        Model = PageInfo
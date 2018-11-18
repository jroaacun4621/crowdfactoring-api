from marshmallow import Schema, fields, pprint
from models import db, PageInfo
from datetime import date

class ApplicantsSchema(Schema):
    class Meta:
        Model = PageInfo
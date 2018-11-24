from marshmallow import Schema
from models import Loans

class LoanSchema(Schema):
    class Meta:
        Model = Loans
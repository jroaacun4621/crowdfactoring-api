from app import db
from datetime import datetime
import uuid

def uuid_generator():
    return str(uuid.uuid4())

class PageInfo(db.Model):
    __tablename__ = 'page_info'

    id = db.Column(db.String, primary_key=True)
    visits = db.Column(db.Integer)

class Loans(db.Model):
    __tablename__ = 'loans'

    id = db.Column(db.String, primary_key=True, default=uuid_generator)

    count_id = db.Column(db.Text)
    value = db.Column(db.Text)
    interest = db.Column(db.Integer)
    sold_percent = db.Column(db.Integer)
    investor = db.Column(db.Text)
    product_type = db.Column(db.Text)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

from app import db

class PageInfo(db.Model):
    __tablename__ = 'page_info'

    id = db.Column(db.String, primary_key=True)
    visits = db.Column(db.Integer)
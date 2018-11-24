from models import db, PageInfo
from schemas.PageInfoSchema import PageInfoSchema
from utils.db_utils import create_autocommit_session

class PageInfoManager(object):
    @staticmethod
    def get_id(id):
        try:
            session = create_autocommit_session(db)
            with session.begin():
                page_info = session.query(PageInfo).filter_by(id=id).first()
                page_info_fields = ('id', 'visits')
                page_info_schema = PageInfoSchema(many=False, only=page_info_fields)
            return page_info_schema.dump(page_info).data
        except Exception as e:
            raise

    @staticmethod
    def update(id, new_visits):
        try:
            session = create_autocommit_session(db)
            with session.begin():
                page_info = session.query(PageInfo).filter_by(id=id).first()
                page_info.visits = new_visits
        except Exception as e:
            raise
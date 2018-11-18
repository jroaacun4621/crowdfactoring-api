from models import db, PageInfo
from schemas.PageInfoSchema import PageInfoSchema
from utils.db_utils import create_autocommit_session

class PageInfoManager(object):
    @staticmethod
    def get_id(id):
        """
        Call model and get item
        :param applicant_id: str, unique id db for applicant. Ie, 'a055d5a6-741d-4551-b536-157be0737832'
        """
        try:
            session = create_autocommit_session(db)
            with session.begin():
                filter_answers = session.query(PageInfo).filter_by(id=id).first()
                filter_answers_fields = ('id', 'visits')
                filter_answers_schema = PageInfoSchema(many=False, only=filter_answers_fields)
            return filter_answers_schema.dump(filter_answers).data
        except Exception as e:
            raise
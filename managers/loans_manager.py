from models import db, Loans
from utils.db_utils import create_autocommit_session
from sqlalchemy import func

class LoanManager(object):
    @staticmethod
    def __get_max_code():
        try:
            max_code_list = db.session.query(func.max(Loans.count_id)).all()
            if max_code_list[0][0] is None:
                max_code = 1
            else:
                print(max_code_list[0][0])
                max_code = int(max_code_list[0][0]) + 1
            return str(max_code)
        except Exception as e:
            raise

    @staticmethod
    def create(loan_data):
        try:
            session = create_autocommit_session(db)
            with session.begin():
                obj = Loans(
                    count_id=LoanManager.__get_max_code(),
                    value = loan_data['value'],
                    interest = loan_data['interest'],
                    sold_percent = loan_data['sold_percent'],
                    investor = loan_data['investor'],
                    product_type = loan_data['product_type']
                )
                session.add(obj)
        except Exception as e:
            raise
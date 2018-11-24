from managers.loans_manager import LoanManager

class LoanController:
    @staticmethod
    def create(loan_data, user_id):
        LoanManager.create(loan_data, user_id)

    @staticmethod
    def get_all(user_id):
        return LoanManager.get_all(user_id)
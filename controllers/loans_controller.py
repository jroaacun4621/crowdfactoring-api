from managers.loans_manager import LoanManager

class LoanController:
    @staticmethod
    def create(loan_data):
        LoanManager.create(loan_data)

    @staticmethod
    def get_all():
        return LoanManager.get_all()
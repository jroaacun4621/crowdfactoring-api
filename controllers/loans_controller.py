from managers.loans_manager import LoanManager

class LoanController:
    @staticmethod
    def create(loan_data):
        LoanManager.create(loan_data)
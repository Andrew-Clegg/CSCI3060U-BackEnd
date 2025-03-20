from scripts.AccountManager import AccountManager
from scripts.ErrorLogger import ErrorLogger

class TransactionProcessor:
    account_manager: AccountManager
    error_logger: ErrorLogger

    def __init__(self, account_manager: AccountManager, error_logger: ErrorLogger):
        self.account_manager = account_manager
        self.error_logger = error_logger

    def process_transaction(self):
        return

    def process_withdrawal(self):
        return

    def process_transfer(self):
        return

    def process_paybill(self):
        return

    def process_deposit(self):
        return

    def process_create(self):
        return

    def process_delete(self):
        return

    def process_disable(self):
        return

    def process_changeplan(self):
        return
from scripts.AccountManager import AccountManager
from scripts.TransactionProcessor import TransactionProcessor
from scripts.FileHandler import FileHandler

class BankingBackEndController:
    account_manager : AccountManager
    transaction_processor: TransactionProcessor
    file_handler: FileHandler

    def __init__(self, master_account_path: str, transaction_file_path: str,
                 new_master_path: str, new_current_accounts_path: str):
        self.master_file_path = master_account_path
        self.transaction_file_path = transaction_file_path
        self.new_master_path = new_master_path
        self.new_current_accounts_path = new_current_accounts_path

    def run(self):
        return

    def process_transaction(self):
        return
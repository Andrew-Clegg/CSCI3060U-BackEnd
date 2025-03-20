from scripts.read import read_old_bank_accounts
from scripts.write import write_new_current_accounts
from typing import List, Dict

class FileHandler:

    def __init__(self):
        return

    def read_old_bank_accounts(self, file_path) -> List[Dict[str, str]]:
        return read_old_bank_accounts(file_path)

    def read_transaction_file(self):
        return

    def write_master_accounts(self):
        return

    def write_new_current_accounts(self, accounts, file_path):
        return write_new_current_accounts(accounts, file_path)

    def format_master_account_line(self, line) -> str:
        return ''

    def format_current_account_line(self, line) -> str:
        return ''
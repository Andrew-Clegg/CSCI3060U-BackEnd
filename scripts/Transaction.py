class Transaction:
    code: str
    name: str
    account_number: str
    amount: float
    misc: str

    def __init__(self, code, name, account_number, amount, misc):
        self.code = code
        self.name = name
        self.account_number = account_number
        self.amount = amount
        self.misc = misc

    def __str__(self) -> str:
        return ('' + self.code + ' ' + self.name + ' ' + self.account_number + ' ' +
                str(self.amount) + ' ' + self.misc)
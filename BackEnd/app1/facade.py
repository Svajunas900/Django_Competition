class BankCard():
    def __init__(self, card_number, amount):
        self.card_number = card_number
        self.amount = amount

    def __str__(self):
        return f"Bank Card {self.card_number}, Amount: {self.amount}"


class Crypto():
    def __init__(self, account_number, amount):
        self.account_number = account_number
        self.amount = amount

    def __str__(self):
        return f"Crypto account: {self.account_number}, Amount: {self.amount}"


class VirtualAccount():
    def __init__(self, account_number, amount):
        self.account_number = account_number
        self.amount = amount

    def __str__(self):
        return f"Virtual Account {self.account_number}, Amount: {self.amount}"


class PaymentFacade():
    def __init__(self, account_number, method, amount):
        if method == "Crypto":
            self.crypto = Crypto(account_number, amount)
        if method == "VirtualAccount":
            self.virtual_account = VirtualAccount(account_number, amount)
        if method == "BankCard":
            self.bank_card = BankCard(account_number, amount)
    
    def deposit(self, method, amount):
        if method == "Crypto":
            self.crypto.amount += amount
        if method == "VirtualAccount":
            self.virtual_account.amount += amount
        if method == "BankCard":
            self.bank_card.amount += amount
    

    def withdraw(self, method, amount):
        if method == "Crypto":
            self.crypto.amount -= amount
        if method == "VirtualAccount":
            self.virtual_account.amount -= amount
        if method == "BankCard":
            self.bank_card.amount -= amount
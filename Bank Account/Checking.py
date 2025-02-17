from BankAccount import BankAccount

class Checking(BankAccount):
    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number, transaction_limit):
        super().__init__(customer_name, current_balance, minimum_balance, account_number, routing_number)
        self.transaction_limit = transaction_limit
        self.transactions_today = 0

    def withdraw(self, amount):
        if self.transactions_today >= self.transaction_limit:
            print("Transaction limit reached for today.")
        else:
            super().withdraw(amount)
            self.transactions_today += 1


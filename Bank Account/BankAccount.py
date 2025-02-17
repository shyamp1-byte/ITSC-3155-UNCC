class BankAccount:
    bank_title = "Global Trust Bank"
    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number):
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance
        self._account_number = account_number
        self.__routing_number = routing_number

    def deposit(self, amount):
        self.current_balance += amount
        print(f"You deposited ${amount}, your current balance is ${self.current_balance}.")

    def withdraw(self, amount):
        if self.current_balance - amount < self.minimum_balance:
            print(f"You tried withdrawing ${amount}, your transaction has been denied. You must maintain a minimum balance of ${self.minimum_balance}!")
        else:
            self.current_balance -= amount
            print(f"You withdrew ${amount}, your current balance is ${self.current_balance}.")

    def print_customer_information(self):
        print(f"Bank Title: {self.bank_title}")
        print(f"Customer Name: {self.customer_name}")
        print(f"Current Balance: {self.current_balance}")
        print(f"Minimum Balance: {self.minimum_balance}")
        print(f"Account Number: {self._account_number}")
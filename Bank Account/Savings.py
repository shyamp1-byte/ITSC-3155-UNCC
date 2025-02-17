from BankAccount import BankAccount

class Savings(BankAccount):
    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number, interest_rate):
        super().__init__(customer_name, current_balance, minimum_balance, account_number, routing_number)
        self.interest_rate = interest_rate

    def apply_interest_rate(self):
        interest = self.current_balance * self.interest_rate/100
        self.current_balance += interest
        print(f"Interest applied is: ${interest}. New balance: ${self.current_balance}")

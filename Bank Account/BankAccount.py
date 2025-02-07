class BankAccount:
    bank_title = "Global Trust Bank"
    def __init__(self, customer_name, current_balance, minimum_balance):
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance

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

account1 = BankAccount("Shyam Pedibhotla", 1000, 200)
account2 = BankAccount("Srian Pedibhotla", 500, 100)

print("\nAccount 1:")
account1.deposit(300)
account1.withdraw(1200)
account1.withdraw(100)
account1.print_customer_information()

print("\nAccount 2:")
account2.deposit(200)
account2.withdraw(600)
account2.withdraw(400)
account2.print_customer_information()
from Savings import Savings
from Checking import Checking

print("\n *** SAVINGS ACCOUNT *** ")
savings_account = Savings("Shyam Pedibhotla", 2000, 500, "123456789", "987654321", 2.5)
savings_account.deposit(500)
savings_account.apply_interest_rate()
savings_account.withdraw(1000)
savings_account.print_customer_information()

print("\n *** CHECKING ACCOUNT *** ")
checking_account = Checking("Srian Pedibhotla", 1500, 200, "987654321", "123456789", 3)
checking_account.deposit(300)
checking_account.withdraw(100)
checking_account.withdraw(200)
checking_account.withdraw(50)
checking_account.print_customer_information()


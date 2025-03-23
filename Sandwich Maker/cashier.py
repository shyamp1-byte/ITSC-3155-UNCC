class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        print("Insert coins:")
        quarters = int(input("How many quarters? ")) * 0.25
        dimes = int(input("How many dimes? ")) * 0.10
        nickles = int(input("How many nickles? ")) * 0.05
        pennies = int(input("How many pennies? ")) * 0.01
        return quarters + dimes + nickles + pennies

    def transaction_result(self, coins, cost):
        if coins < cost:
            print("Sorry, not enough money. Money refunded.")
            return False
        elif coins > cost:
            change = round((cost - coins), 2)
            print(f"Here is your change: {change}")
        print("Payment Successful!")
        return True
import data
from sandwich_maker import SandwichMaker
from cashier import Cashier

def main():
    machine = SandwichMaker(data.resources)
    cashier = Cashier()

    while True:
        choice = input("What size sandwich would you like? (small/medium/large/report/off): ").lower()
        if choice == "off":
            print("Shutting down.")
            break
        elif choice == "report":
            print("Current resources:")
            for item, amount in machine.machine_resources.items():
                print(f"{item}: {amount}")
        elif choice in data.recipes:
            sandwich = data.recipes[choice]
            if machine.check_resources(sandwich["ingredients"]):
                print(f"The cost is ${sandwich['cost']}")
                total_money = cashier.process_coins()
                if cashier.transaction_result(total_money, sandwich["cost"]):
                    machine.make_sandwich(choice, sandwich["ingredients"])
        else:
            print("Invalid choice, please try again.")
if __name__ == "__main__":
    main()
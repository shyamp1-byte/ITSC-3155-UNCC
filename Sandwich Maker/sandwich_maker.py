class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources

    def check_resources(self, ingredients):
        for item, amount in ingredients.items():
            if self.machine_resources[item] < amount:
                print(f"Sorry, not enough for {item}.")
                return False
        return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        for item, amount in order_ingredients.items():
            self.machine_resources[item] -= amount
        print(f"Here is your {sandwich_size} ham sandwich.")
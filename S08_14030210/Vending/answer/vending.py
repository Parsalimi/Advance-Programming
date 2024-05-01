class Vending:
    def __init__(self, coffee):
        self.coffee = coffee
        self.price = 0
        self.sugar_price = 5
        self.milk_price = 10
        
    def coffee_type(self):
        if self.coffee == "latte":
            self.price += 40
        elif self.coffee == "mocha":
            self.price += 45
        elif self.coffee == "espresso":
            self.price += 30
        elif self.coffee == "americano":
            self.price += 35
        elif self.coffee == "cappuccino":
            self.price += 40
        elif self.coffee == "caramel macchiato":
            self.price += 45
        else:
            return 0
        return self.price
        
    def extras(self, milk_percent, sugar_percent):
        if milk_percent > 5 or sugar_percent > 5 or milk_percent < 0 or sugar_percent < 0:
            return "please choose your extra (milk/sugar) between 0 and 5"
        else:
            if self.coffee_type() == 0:
                return f"sorry we can't provide you with '{self.coffee}'"
            else:
                self.coffee_type()
                self.price += milk_percent*self.milk_price + sugar_percent*self.sugar_price
                return self.price

processing = True
while processing:
    coffee_type = input("choose your coffee (between latte, mocha, espresso, americano, cappuccino and caramel macchiato)\n").lower()
    sugar_amount = int(input("how much sugar do you want with that? (between 0, 5)\n"))
    milk_amount = int(input("how much milk do you want with that? (between 0, 5)\n"))

    coffee = Vending(coffee_type)
    order = coffee.extras(milk_amount, sugar_amount)
    if isinstance(order, int):
        processing = False
        print(order)
    else:
        print(order)
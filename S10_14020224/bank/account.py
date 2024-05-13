from user import Users

class Account(Users):
    def __init__(self, name, cardNumber, balace):
        super().__init__(name)
        self.name = name
        self.cardNumber = cardNumber
        self.balance = balace
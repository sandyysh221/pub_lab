class Customer:
    def __init__(self, get_name, get_wallet, get_age):
        self.name = get_name
        self.wallet = get_wallet
        self.age = get_age
        self.drunkenness = 0

    def sufficient_funds(self, item):
        return self.wallet >= item.price

    def decrease_wallet(self, drink):
        if self.sufficient_funds(drink):
            self.wallet -= drink.price

    def increase_drunk(self, alcohol):
        drunkenness += alcohol


# buy drink reduce wallet, increase till
# age param
# alcohol count

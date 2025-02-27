class Pub:
    def __init__(self, get_name, get_till):
        self.name = get_name
        self.till = get_till
        self.drinks = []

    def increase_till(self, cash_in):
        self.till += cash_in

    def check_enough_cash(self, customer, drink_price):
        return customer.wallet >= drink_price

    def confirmed_age(self, customer):
        return customer.age >= 18

    def add_drink_to_customer(self, drink):
        self.drinks.append(drink)

    def sell_drink(self, drink, customer):
        if not self.confirmed_age(customer):
            return False
        if not self.cst_can_afford(customer, drink):
            return False
        if self.cst_too_drunk(customer):
            return False
        else:
            customer.wallet -= drink.price
            self.till += drink.price

    def cst_can_afford(self, customer, drink):
        return customer.sufficient_funds(drink)

    def cst_too_drunk(self, customer):
        return customer.drunkenness >= 50


# check drunk
# stock value ie.value of all drinks

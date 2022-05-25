class Pub:
    def __init__(self, get_name, get_till):
        self.name = get_name
        self.till = get_till
        self.drinks = []

    def increase_till(self, cash_in):
        self.till += cash_in

    def check_enough_cash(self, customer, drink_price):
        if customer.wallet >= drink_price:
            return True
        return False

    def confirmed_age(self, customer):
        return customer.age >= 18

    def add_drink_to_customer(self, drink):
        self.drinks.append(drink)

    def sell_drink(self, drink, customer):
        if not self.confirmed_age(customer):
            return False
        else:
            customer.wallet -= drink.price
            self.till += drink.price


# check customer age
# check drunk
# stock value ie.value of all drinks

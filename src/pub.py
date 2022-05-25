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
        if customer.wallet <= drink.price:
            return False
        else:
            customer.wallet -= drink.price
            self.till += drink.price

    def cst_can_afford(self, customer, drink):
        return customer.sufficient_funds(drink)


# check drunk
# stock value ie.value of all drinks

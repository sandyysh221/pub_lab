from src.customer import Customer


class Pub:
    def __init__(self, get_name, get_till):
        self.name = get_name
        self.till = get_till

    def increase_till(self, cash_in):
        self.till += cash_in

    def check_enough_cash(self, customer, drink_price):
        if customer.wallet >= drink_price:
            return True
        return False

    def check_age(self, customer):
        if customer.age >= 18:
            return True
        return False

    def sell_drink(self, drink_price, customer):
        if (
            self.check_enough_cash(customer, drink_price) == True
            and customer.age == True
        ):

            self.increase_till(drink_price)
            customer.decrease_wallet(drink_price)

        return False


# check customer age
# check drunk
# stock value ie.value of all drinks

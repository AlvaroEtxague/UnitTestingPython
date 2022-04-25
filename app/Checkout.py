class Checkout:
    class Discount:
        def __init__(self, nbr_of_items, price):
            self.nbr_of_items = nbr_of_items
            self.price = price

    def __init__(self):
        self.prices = {}
        self.discounts = {}
        self.items = {}

    def add_discount(self, item, nbr_of_items, price):
        discount = self.Discount(nbr_of_items, price)
        self.discounts[item] = discount

    def add_item_price(self, item, price):
        self.prices[item] = price

    def add_item(self, item):
        if item not in self.items:
            raise Exception("Bad Item")

        if item in self.items:
            self.items[item] += 1
        else:
            self.items[item] = 1

    def calculate_total(self):
        total = 0
        for item, count in self.items.items():
            total += self.calculate_item_total(item, count)
        return total

    def calculate_item_total(self, item, count):
        total = 0
        if item in self.discounts:
            discount = self.discounts[item]
            if count >= discount.nbr_of_items:
                total += self.calculate_item_discount(item, count, discount)
            else:
                total += self.prices[item] * count
        else:
            total += self.prices[item] * count

        return total

    def calculate_item_discount(self, item, count, discount):
        total = 0
        nbr_of_discounts = count / discount.nbr_of_items
        total += nbr_of_discounts * discount.price
        remaining = count % discount.nbr_of_items
        total += remaining * self.prices[item]
        return total

from datetime import datetime


class Cinema:
    def __init__(self):
        self.price = 0
        self.start_from = datetime(2021, 7, 1)
        self.closed_from = datetime(2021, 8, 31)
        self.start_with_new_price = datetime(2021, 8, 10)

    def get_price(self, year, month, day):
        date = datetime(year, month, day)
        if self.start_from <= date <= self.closed_from:
            if date <= self.start_with_new_price:
                self.price = 250
                return self.price
            else:
                self.price = 180
                return self.price
        else:
            return "Cinema is closed"


test = Cinema().get_price(2021, 9, 24)
print(test)

from datetime import datetime


class Cinema:
    def __init__(self):
        self.price = 0
        self.start_from = datetime(2021, 7, 1)
        self.closed_from = datetime(2021, 8, 31)
        self.start_with_new_price = datetime(2021, 8, 10)

    def get_price(self, visit_date):
        if self.start_from <= visit_date <= self.closed_from:
            if visit_date <= self.start_with_new_price:
                self.price = 250
            else:
                self.price = 180
        else:
            print("Cinema is closed")
        return self.price


date = datetime.strptime(input("Enter visit date in format dd.mm.yyyy: "), "%d.%m.%Y")
test = Cinema().get_price(date)
print(f"Prise is: {test}")

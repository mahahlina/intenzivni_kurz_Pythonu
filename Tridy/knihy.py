class Book:
    def __init__(self, title, pages, price, velikost_slevy_v_procentech):
        self.title = title
        self.pages = pages
        self.price = price
        self.velikost_slevy_v_procentech =velikost_slevy_v_procentech

    def getInfo(self):
        print(f"Kniha {self.title} obsahuje {self.pages} stranky a stoji {self.price}")

    def discount(self):
        self.price -= self.price / 100 * self.velikost_slevy_v_procentech
        print("Mate slevu")


test = Book("BookName", 55, 100, 10)
print(test.discount())
print(test.getInfo())

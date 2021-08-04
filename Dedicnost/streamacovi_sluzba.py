class Polozka:
    def __init__(self, nazev, zanr):
        self.nazev = nazev
        self.zanr = zanr

    def get_info(self):
        return f"Název: {self.nazev}, žánr: {self.zanr}"


class Film(Polozka):
    def __init__(self, nazev, zanr, delka):
        super().__init__(nazev, zanr)
        self.delka = str(delka)

    def get_info_about_film(self):
        return self.get_info() + f" délka: {self.delka} "


class Serial(Polozka):
    def __init__(self, nazev, zanr, pocet_epizod, delka_epizody):
        super().__init__(nazev, zanr)
        self.pocet_epizod = str(pocet_epizod)
        self.delka_epizody = str(delka_epizody)

    def get_info_about_serial(self):
        return self.get_info() + f" délka epizody: {self.delka_epizody}, počet epizod: {self.pocet_epizod}"


test_film = Film("IT", "Horor", 55)
print(test_film.get_info_about_film())

test_serial = Serial("Friends", "Comedy", 123, 20)
print(test_serial.get_info_about_serial())

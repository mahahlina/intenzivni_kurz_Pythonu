from abc import ABC, abstractmethod


class Polozka(ABC):
    def __init__(self, nazev, zanr):
        self.nazev = nazev
        self.zanr = zanr

    @abstractmethod
    def get_info(self):
        pass


class Film(Polozka):
    def __init__(self, nazev, zanr, delka):
        super().__init__(nazev, zanr)
        self.delka = str(delka)

    def get_info(self):
        return f"Název: {self.nazev}, žánr: {self.zanr} délka: {self.delka}"

    def get_celkova_delka(self):
        return self.delka


class Serial(Polozka):
    def __init__(self, nazev, zanr, pocet_epizod, delka_epizody):
        super().__init__(nazev, zanr)
        self.pocet_epizod = pocet_epizod
        self.delka_epizody = delka_epizody

    def get_info(self):
        return f"Název: {self.nazev}, žánr: {self.zanr}, délka epizody: {str(self.delka_epizody)}, " \
            f"počet epizod: {str(self.pocet_epizod)}"

    def get_celkova_delka(self):
        return self.delka_epizody * self.pocet_epizod


class Uzivatel:
    def __init__(self, uzivatelske_jmeno):
        self.uzivatelske_jmeno = uzivatelske_jmeno
        self.delka_sledovani = 0

    def pripocti_zhlednuti(self, delka_sledovani):
        return f"Uživatel {self.uzivatelske_jmeno} zhlédl(a) {delka_sledovani} minut videa"


test_film = Film("IT", "Horor", 55)
print(test_film.get_info())

test_serial = Serial("Friends", "Comedy", 123, 0.2)
print(test_serial.get_info())

test_celkova_delka = int(test_serial.get_celkova_delka()) + int(test_film.get_celkova_delka())
print(Uzivatel("Marina").pripocti_zhlednuti(test_celkova_delka))

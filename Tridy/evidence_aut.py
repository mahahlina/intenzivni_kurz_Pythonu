class Auto:
    def __init__(self, reg_znacka, znacka_a_typ_auta, najet, je_volne=True):
        self.reg_znacka = reg_znacka
        self.znacka_a_typ_auta = znacka_a_typ_auta
        self.najet = najet
        self.je_volne = je_volne
        self.stav_tachometru = 0
        self.dni = 0

    def getInfo(self):
        return f"Registrační značka automobilu: {self.reg_znacka} /n Značka a typ vozidla: {self.znacka_a_typ_auta} /n" \
            f"Počet najetých kilometrů: {self.najet} /n"

    def pujc_auto(self):
        if self.je_volne:
            self.je_volne = False
            return "Potvrzuji zapůjčení vozidla"
        else:
            return "Vozidlo není k dispozici"

    def vrat_auto(self, stav_tachometru, dni):
        self.stav_tachometru = stav_tachometru
        self.dni = dni
        self.je_volne = True
        if int(self.dni) < 7:
            price = int(self.dni) * 400
        else:
            price = int(self.dni) * 300
        return f"Cena: {price} Kc"


pegout = Auto("4A2 3020", "Peugeot 403 Cabrio", 47534)
skoda = Auto("1P3 4747", "Škoda Octavia", 41253, False)

znacka = input("jakou značku si přeje půjčit ")
if znacka == "Peugeot":
    auto = pegout
    print(pegout.getInfo())
    print(pegout.pujc_auto())

else:
    print(skoda.getInfo())
    print(skoda.pujc_auto())
    auto = skoda

stav_tachometru = input("Kolik kilometrů jsi ujel? ")
pocet_dni = input("Jak dlouho ho měl půjčené? ")
print(auto.vrat_auto(stav_tachometru, pocet_dni))

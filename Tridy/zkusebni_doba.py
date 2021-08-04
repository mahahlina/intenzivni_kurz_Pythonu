class Zamestnanec:
    def cerpani_dovolene(self, days):
        if self.pocet_dni_dovolene >= days:
            self.pocet_dni_dovolene -= days
            return f"Užij si to."
        else:
            return f"Bohužel už máš nárok jen na {self.pocet_dni_dovolene} dní."

    def vypis_informace(self):
        if self.probation:
            return f"{self.jmeno} pracuje na pozici {self.pozice}. /n Je ve zkušební době"
        else:
            return f"{self.jmeno} pracuje na pozici {self.pozice}."

    def __init__(self, jmeno, pozice, probation:bool):
        self.jmeno = jmeno
        self.pozice = pozice
        self.pocet_dni_dovolene = 25
        self.probation = probation

frantisek = Zamestnanec("František Novák", "konstruktér", False)
print(frantisek.vypis_informace())
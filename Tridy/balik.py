class Package:
    def __init__(self, address, weightInKilos, delivered=False):
        self.address =address
        self.weightInKilos  = weightInKilos
        self.delivered = delivered

    def deliver(self):
        self.delivered = True

    def getInfo(self):
        print(f"Adresa: {self.address}")
        print(f"Hmotnost: {self.weightInKilos}")
        if self.delivered:
            print(f"Balik byl doručen")
        else:
            print(f"Balik jeste ne doručen")


balik_1 = Package("Praha, Vaclavske Namnesti", 5)
balik_2 = Package("Brno, Namnesty Svobody", 3, True)

balik_1.deliver()
print(balik_1.getInfo())
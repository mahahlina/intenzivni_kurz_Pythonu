class Package:
    def __init__(self, address, weightInKilos):
        self.address = address
        self.weightInKilos = weightInKilos
        self.delivered = False

    def deliver(self):
        self.delivered = True

    def getInfo(self):
        if self.delivered:
            return f"Adresa: {self.address} Hmotnost: {self.weightInKilos} Balik byl doručen"
        else:
            return f"Adresa: {self.address} Hmotnost: {self.weightInKilos} Balik jeste ne doručen"


class ValuablePackage(Package):
    def __init__(self, address, weightInKilos, value):
        super().__init__(address, weightInKilos)
        self.value = value


test_package = ValuablePackage("Praha, Vaclavske Namnesti", 5, 1)
print(test_package.getInfo())

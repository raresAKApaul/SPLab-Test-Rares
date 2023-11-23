class Soldat:
    def __init__(self, nume, numar_soldati):
        self.nume = nume
        self.numar_soldati = numar_soldati

    def print(self):
        print(self.numar_soldati, self.nume)


class Gnom(Soldat):
    def __init__(self, numar_soldati):
        super().__init__('gnomi', numar_soldati)


class Elf(Soldat):
    def __init__(self, numar_soldati):
        super().__init__('elfi', numar_soldati)


class ProxyEnt(Soldat):
    def __init__(self, ent):
        super().__init__('enti', 0)
        self.ent = ent

    def print(self):
        if self.ent.autorizat():
            return self.ent.print()
        else:
            return "Acces interzis"


class Ent(Soldat):
    def __init__(self, numar_soldati):
        super().__init__('enti', numar_soldati)

    def autorizat(self):
        return True


class Batalion(Soldat):
    def __init__(self):
        super().__init__('soldati', 0)
        self.soldati = []

    def adauga_soldat(self, soldat):
        self.soldati.append(soldat)
        self.numar_soldati += soldat.numar_soldati

    def print(self):
        print("Total soldati:", self.numar_soldati)
        for soldat in self.soldati:
            soldat.print()


if __name__ == "__main__":
    batalion = Batalion()
    gnomi = Gnom(10)
    elfi = Elf(15)
    enti_reali = Ent(5)
    ent_proxy = ProxyEnt(enti_reali)

    batalion.adauga_soldat(gnomi)
    batalion.adauga_soldat(elfi)
    batalion.adauga_soldat(ent_proxy)

    batalion.print()

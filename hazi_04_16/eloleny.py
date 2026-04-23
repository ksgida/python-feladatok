class Eloleny:
    def __init__(self, nev, eletkor):
        self.nev = nev
        self.eletkor = eletkor

    def __str__(self):
        return f"{self.nev} ({self.eletkor} éves)"

class Noveny(Eloleny):
    def __init__(self, nev, eletkor, vizigeny):
        super().__init__(nev, eletkor)
        self.vizigeny = vizigeny

    def __str__(self):
        return f"{self.nev} ({self.eletkor} éves, vízigény: {self.vizigeny})"

class Allat(Eloleny):
    def __init__(self, nev, eletkor, labak_szama):
        super().__init__(nev, eletkor)
        self.labak_szama = labak_szama

    def __str__(self):
        return f"{self.nev} ({self.eletkor} éves, {self.labak_szama} lábú)"

class Gomba(Eloleny):
    def __init__(self, nev, eletkor, mergezo_e):
        super().__init__(nev, eletkor)
        self.mergezo_e = mergezo_e

    def __str__(self):
        mergezo_szoveg = "mérgező" if self.mergezo_e else "nem mérgező"
        return f"{self.nev} ({self.eletkor} éves, {mergezo_szoveg})"

# Teszt
n1 = Noveny("Tulipán", 2, "magas")
a1 = Allat("Macska", 4, 4)
g1 = Gomba("Piros pöttyös gomba", 100, True)

print(n1)
print(a1)
print(g1)

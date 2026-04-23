class Konyv:
    def __init__(self, cim, szerzo):
        self.cim = cim
        self.szerzo = szerzo

    def __str__(self):
        return f"{self.cim} - {self.szerzo}"

class Konyvtar:

    def __init__(self):
        self.konyvek = []

    def hozzaad(self, konyv):
        self.konyvek.append(konyv)

    def listaz(self):
        print("Lista:")
        for konyv in self.konyvek:
            print(konyv)

    def __str__(self):
        visszater = ""
        for konyv in self.konyvek:
            visszater += str(konyv) + "\n"
        return visszater

    def __add__(self, other):
        if isinstance(other, Konyvtar):
            uj_konyvtar = Konyvtar()
            uj_konyvtar.konyvek = self.konyvek + other.konyvek
            return uj_konyvtar
        else:
            raise ValueError("Csak másik Könyvtárat lehet hozzáadni")

konyvtar = Konyvtar()
konyvtar.hozzaad(Konyv("A Gyűrűk Ura", "J.R.R. Tolkien"))
konyvtar.hozzaad(Konyv("Harry Potter és a bölcsek köve", "J.K. Rowling"))
konyvtar.hozzaad(Konyv("A szél árnyéka", "Carlos Ruiz Zafón"))

konyvtar.listaz()
print(konyvtar)

konyvtar1 = Konyvtar()
konyvtar1.hozzaad(Konyv("Egri csillagok", "Gárdonyi Géza"))
konyvtar1.hozzaad(Konyv("1984", "George Orwell"))

konyvtar2 = Konyvtar()
konyvtar2.hozzaad(Konyv("A kis herceg", "Antoine de Saint-Exupéry"))
konyvtar2.hozzaad(Konyv("Dűne", "Frank Herbert"))

uj_konyvtar = konyvtar1 + konyvtar2
print(uj_konyvtar)
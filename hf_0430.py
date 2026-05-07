# 1. feladat

try:
    eletkor = int(input("Add meg az életkorodat: "))
    ev_mulva = 100 - eletkor

    print(ev_mulva, "év múlva leszel 100 éves.")
except ValueError:
    print("Nem számot adtál meg.")


# 2. feladat

fajlnev = input("Add meg a fájl nevét: ")

try:
    fajl = open(fajlnev, "r")

    elso_sor = fajl.readline()
    fajl.close()

    try:
        szam = int(elso_sor)
        print("A szám kétszerese:", szam * 2)
    except ValueError:
        print("A fájl első sora nem szám.")

except FileNotFoundError:
    print("Nincs ilyen fájl.")


# 3. feladat

try:
    jelszo = input("Add meg a jelszót: ")

    if len(jelszo) < 8:
        raise Exception("A jelszó túl rövid.")

    print("Jelszó elfogadva.")

except Exception as hiba:
    print("Hiba:", hiba)
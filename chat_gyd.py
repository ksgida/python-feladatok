
def feldolgozas(kerdes):
    print("feldolgozas alatt: " + kerdes)

    szamjegyek = dict()
    for betu in kerdes:
        if betu in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
            if betu in szamjegyek:
                szamjegyek[betu] += 1
            else:
                szamjegyek[betu] = 1

    # Házi 1
    if kerdes.endswith("?"):
        print("Ez bizony egy kérdés")

    # Házi 3
    if len(szamjegyek) == 0:
        print("Ebben egy számjegy sem volt.")

    # Házi 4
    pontok_szama = kerdes.count(".")
    print("A kérdés " + str(pontok_szama) + " darab pontot tartalmazott.")

    return szamjegyek

    # return kerdes[::-1]


while True:
    kerdes = input("Kerdes: ")

    # Házi 2
    if kerdes == "exit" or kerdes == "quit":
        print("Bye!")
        break

    print("Ezt kerdezte: " + kerdes)

    valasz = feldolgozas(kerdes)

    print("Válasz: " + str(valasz))

print("VEGE.")

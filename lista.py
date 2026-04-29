#1. feladat

kiindulo = ["szó1", "szó2", "szó3", "szó4", "szó5", "hosszúszó"]
nagybetus = [s.upper() for s in kiindulo]
rovidnagybetus = [s.upper() for s in kiindulo if len(s) < 6]

print(kiindulo)
print(nagybetus)
print(rovidnagybetus)

#2. feladat

import random

idezetek = [
    "Az élet olyan, mint egy doboz csokoládé, sosem tudhatod, mit kapsz.",
    "A siker titka a kitartás.",
    "Ne add fel, mert sosem tudhatod, milyen közel vagy a célodhoz.",
    "Az igazi barátok mindig melletted állnak.",
    "A boldogság nem a cél, hanem az út maga."
]

def napi_idezet():
    while(True):
        yield random.choice(idezetek)

idezet_generator = napi_idezet()
print(next(idezet_generator))
print(next(idezet_generator))

for i in range(5):
    print(next(idezet_generator))

#3. feladat
szamok = [-5, -2, 0, 1, 3, 5, 8, 13, 21]

generator = (x * 10 for x in szamok if x > 0)

for szam in generator:
    print(szam)

#4. feladat
szavak = ["London", "Prága", "Szeged", "Budapest", "New York", "Ág"]
kisbetus = list(map(lambda s: s.lower(), szavak))
rovidek = list(filter(lambda s: len(s) < 3, szavak))

print(kisbetus)
print(rovidek)
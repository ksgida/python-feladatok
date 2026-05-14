import sys
import logging
import asyncio

#1. feladat
logging.basicConfig(level=logging.INFO)
logging.info("A program elindult")

#2. feladat
logging.basicConfig(level=logging.INFO)

if len(sys.argv) == 1:
    logging.error("Nincs paraméter megadva")
    print("Hiba: adj meg legalább egy számot!")
else:
    osszeg = 0

    try:
        for arg in sys.argv[1:]:
            osszeg += int(arg)

        print("Összeg:", osszeg)

    except ValueError:
        logging.error("Valamelyik paraméter nem szám")
        print("Hiba: minden paraméternek számnak kell lennie!")

#3. feladat

#4. feladat
logging.basicConfig(level=logging.DEBUG)

for szam in range(1, 6):
    logging.debug(f"Aktuális szám: {szam}")

    if szam % 2 == 0:
        logging.info(f"Páros szám: {szam}")

#5. feladat
async def feladat(x):
    print(f"Start: {x}")
    await asyncio.sleep(1)
    print(f"Kész: {x}")
    return x * 2


async def main():
    feladatok = [
        feladat(1),
        feladat(2),
        feladat(3)
    ]

    eredmenyek = await asyncio.gather(*feladatok)

    print("Eredmények:", eredmenyek)


asyncio.run(main())
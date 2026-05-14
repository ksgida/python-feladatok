import sys
import logging
import asyncio


logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)


async def feldolgoz(szam):
    logging.info("Feldolgozás: " + str(szam))
    await asyncio.sleep(1)
    return szam * 2


async def async_main(szamok):
    eredmenyek = await asyncio.gather(
        *[feldolgoz(szam) for szam in szamok]
    )

    logging.info("Eredmények: " + str(eredmenyek))


def main():
    # sys.argv[0] maga a fájlnév, ezért az első valódi paraméter a sys.argv[1]
    parameterek = sys.argv[1:]

    szamok = []

    for beolvasott in parameterek:
        try:
            szam = int(beolvasott)
            szamok.append(szam)
        except ValueError:
            logging.error(f"Hiba: a(z) '{beolvasott}' nem alakítható számmá!")
            return

    asyncio.run(async_main(szamok))


if __name__ == "__main__":
    logging.info("Program indulása")
    main()
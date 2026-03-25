import csv
import requests

url = "https://gutendex.com/books/?languages=hu"

max_oldalak = 4
aktualis_oldal = 1
talalatok = []

try:
    while url and aktualis_oldal <= max_oldalak:
        valasz = requests.get(url, timeout=30)
        valasz.raise_for_status()

        adat = valasz.json()
        books = adat.get("results", [])

        for book in books:
            title = book.get("title", "")

            authors = book.get("authors", [])
            authors_szoveg = ", ".join([a.get("name", "") for a in authors])

            summaries = book.get("summaries", [])
            summaries_szoveg = "\n".join(summaries)

            talalatok.append([title, authors_szoveg, summaries_szoveg, aktualis_oldal])

        url = adat.get("next")
        aktualis_oldal += 1

    with open("talalatok.csv", "w", encoding="utf-8-sig", newline="") as f:
        iro = csv.writer(f)
        iro.writerow(["title", "authors", "summaries", "page"])

        for sor in talalatok:
            iro.writerow(sor)

    print("A mentés elkészült: talalatok.csv")
except Exception as e:
    print("Hiba történt:", e)
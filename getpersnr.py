import requests
import random

looping = True


    #RANDOMIZER
while looping:
    slumptal = random.randint(1, 41130)
    url = f"https://skatteverket.entryscape.net/rowstore/dataset/b4de7df7-63c0-4e7e-bb59-1f156a591763/json?_offset={slumptal}&_limit=1"

    #REQUESTS

    req = requests.get(url)
    json_data = req.json()
    list_results = json_data["results"]

    print("\nHär slumpas ett giltigt personnummer från Skatteverket: \n")

    personnummer = list_results[0]["testpersonnummer"]

    print(personnummer[2:12])

    entill = input("\nVill du slumpa ett personnummer till? Ja/Nej: ")

    if (entill == "nej" or entill == "Nej"):
         break

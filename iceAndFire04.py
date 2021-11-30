#!/usr/bin/python3
"""Alta3 Research - Exploring OpenAPIs with requests"""
# documentation for this API is at
# https://anapioficeandfire.com/Documentation

import requests
import pprint

AOIF_CHAR = "https://www.anapioficeandfire.com/api/characters/"
GOT_HOUSE= "https://www.anapioficeandfire.com/api/houses/"
GOT_BOOKS = "https://www.anapioficeandfire.com/api/books/"

def main():
        ## Ask user for input
        got_charToLookup = input("Pick a number between 1 and 1000 to return info on a GoT character! " )

        ## Send HTTPS GET to the API of ICE and Fire character resource
        gotresp = requests.get(AOIF_CHAR + got_charToLookup)

        ## Decode the response
        got_dj = gotresp.json()

        houses = got_dj['allegiances']
        books = got_dj ['books']
        if got_dj['name']:
            print(f"Character Name: {got_dj['name']}")
        else:
            print(f"Character Alias: {got_dj['aliases'][0]}")
        for house in houses:
            houseresp = requests.get(house)
            gothouse = houseresp.json()
            print(f"House Name: {gothouse['name']}")
        for book in books:
            bookresp = requests.get(book)
            gotbook = bookresp.json()
            print(f"Book Name:{gotbook['name']}")

        #houseresp = requests.get(houses)
        #got_house = houseresp.json()

if __name__ == "__main__":
        main()

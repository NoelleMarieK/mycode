#!/usr/bin/python3

import requests

NASAAPI = "http://api.open-notify.org/iss-now.json"


# this is our main function
def main():

    ## make a call to NASAAPI with our key
    iss_resp = requests.get(NASAAPI).json()

    ## strip off json

    #print(iss_resp['iss_position']['longitude'])
    print(f" Current Location of the ISS: ")
    print(f"Lon: {iss_resp['iss_position']['longitude']}")
    print(f"Lon: {iss_resp['iss_position']['latitude']}")

if __name__ == "__main__":
    main()

#!/usr/bin/python3
import requests

## Define NEOW URL
NEOURL = "https://api.nasa.gov/neo/rest/v1/feed?"

# this function grabs our credentials
# it is easily recycled from our previous script
def returncreds():
    ## first I want to grab my credentials
    with open("/home/student/nasa.creds", "r") as mycreds:
        nasacreds = mycreds.read()
    ## remove any newline characters from the api_key
    nasacreds = "api_key=" + nasacreds.strip("\n")
    return nasacreds

# this is our main function
def main():
    ## first grab credentials
    nasacreds = returncreds()

    ##enter start date
    get_startdate = input("Please enter a start date time- yyyy-mm-dd. ") 

    ## update the date below, if you like
    if get_startdate:
        startdate= get_startdate
    else:
        print("No date selected, default is 2019-11-11")
        startdate = "start_date=2019-11-11"

    ## the value below is not being used in this
    ## version of the script
    # enddate = "end_date=END_DATE"

    # make a request with the request library
    neodata = requests.get(NEOURL + startdate + "&" + nasacreds).json()

    # strip off json attachment from our response
    #neodata = neowrequest.json()
    
    ## display NASAs NEOW data
    print(neodata['element_count'])

if __name__ == "__main__":
    main()

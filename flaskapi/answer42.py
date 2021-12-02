#!/usr/bin/python3

import requests

url= "http://10.8.228.56:2224/post"

answer= {
         "answ": "42"
         }

requests.post(url, json=answer)

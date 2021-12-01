#!/usr/bin/env python3

import requests

URL = "http://10.8.228.56:2224/slappy"


x = (requests.get(URL)).text
print(x)

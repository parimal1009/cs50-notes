import requests
import sys
import json
try:
    if len(sys.argv)==1:
        sys.exit("Missing command-line argument")
    else:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        a = response.json()
        b = a.get("bpi")
        c = b.get("USD")
        d = c.get("rate")
        d = d.replace(',','')
        e = float(sys.argv[1])*float(d)
        print(f"${e:,.4f}")
except ValueError:
    sys.exit("Command-line argument is not a number")

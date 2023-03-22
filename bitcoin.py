##

import requests
import json
import sys

try:
    url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    response = requests.get(url)
    data = json.loads(response.content)
    current_price = float(data['bpi']['USD']['rate'].replace(',', ''))
    sys.argv[1] = int(sys.argv[1])
    price = current_price * sys.argv[1]
    print(f"${price:,.4f}")
except requests.RequestException:
    if len(sys.argv) < 2:
        print("Missing command-line argument.")
        sys.exit()
    elif not sys.argv[1].isnumeric():
        print("Command-line argument is not a number")
        sys.exit()
except IndexError:
    print("Please input the amount of Bitcoins too")
    sys.exit() 
except ValueError:
    print("Please input the amount only in integers")
    sys.exit() 


import sys
import requests


if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")
try:
    input = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    o = response.json()
    print(f'${o["bpi"]["USD"]["rate_float"]*float(sys.argv[1]):,.4f}')
except requests.RequestException:
    sys.exit("request Error")

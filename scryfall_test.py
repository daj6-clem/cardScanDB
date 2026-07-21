import requests

card_name  = "Lightning Bolt"

url = f"https://api.scryfall.com/cards/named?exact={card_name}"

response = requests.get(url)

print(response.status_code)

card = response.json()

print(card)
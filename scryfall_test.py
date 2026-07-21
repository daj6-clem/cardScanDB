import requests


# YOU MUST HAVE A CUSTOM USER-AGENT HEADER IF YOU WANT TO USE SCRYFALL API
headers = {
    "User-Agent": "cardScanDB/0.1 (https://github.com/daj6-clem/cardScanDB; daj6@clemson.edu)"
}

# READ THE CARD NAME INTO A VAR
cardName  = "Lightning Bolt"

# PLUG CARD NAME INTO URL
url = f"https://api.scryfall.com/cards/named?exact={cardName}"

response = requests.get(
    url,
    headers = headers
)

response.raise_for_status()

#print(response.status_code)

card = response.json()

#print(card.keys())
# Returns -> dict_keys(['object', 'id', 'oracle_id', 'multiverse_ids', 'resource_id', 'mtgo_id', 'arena_id', 'tcgplayer_id', 'cardmarket_id', 'name', 'lang', 
# 'released_at', 'uri', 'scryfall_uri', 'layout', 'highres_image', 'image_status', 'image_updated_at', 'image_uris', 'mana_cost', 'cmc', 'type_line', 'oracle_text', 
# 'colors', 'color_identity', 'keywords', 'all_parts', 'legalities', 'games', 'reserved', 'game_changer','foil', 'nonfoil', 'finishes', 'oversized', 'promo', 'reprint', 
# 'variation', 'set_id', 'set', 'set_name', 'set_type', 'set_uri', 'set_search_uri', 'scryfall_set_uri', 'rulings_uri', 'prints_search_uri', 'collector_number', 
# 'digital', 'rarity', 'flavor_text', 'card_back_id', 'artist', 'artist_ids', 'illustration_id', 'border_color', 'frame', 'full_art', 'textless', 'booster', 
# 'story_spotlight', 'promo_types','edhrec_rank', 'prices', 'related_uris', 'purchase_uris'])
print(card["name"])
print(card["mana_cost"])
print(card["type_line"])
import requests

Url = "https://old.west.albion-online-data.com/api/v2/stats/prices/t4_bag"

params = {
    "locations": "Bridgewatch, Lymhurst",
    "qualities": "1,2,3,4"
}

response = requests.get(Url, params=params)

if response.status_code == 200:
    data = response.json()
    for item in data:
        print(f"Item: {item['item_id']} {item['sell_price_min']} {item['quality']}")
else:
    print(f"{response.status_code}, {response.text}")

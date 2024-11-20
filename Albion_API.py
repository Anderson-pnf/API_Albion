import requests

Url = "https://old.west.albion-online-data.com/api/v2/stats/prices/t4_bag"

params = {
    "locations": "Bridgewatch, Lymhurst",
    "qualities": "1,2,3"
}

response = requests.get(Url, params=params)

if response.status_code == 200:
    print("Dados retornados com sucesso")
    print(response.json())
else:
    print(f"{response.status_code}, {response.text}")

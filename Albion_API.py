import pandas as pd
import requests
import json

arquivo_json = 'items.json'

with open(arquivo_json, 'r') as file:
    dados_itens = json.load(file)

item_ids = [item["item_id"] for item in dados_itens["items"]]

url = f"https://old.west.albion-online-data.com/api/v2/stats/prices/{','.join(item_ids)}"

params = {
    ''
    "locations": "Bridgewatch, Lymhurst, Caerleon, Thetford, Martlock, Fort Sterling, Black Marketing",
    "qualities": "1,2,3,4"
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    print(data)

    if isinstance(data, list):

        df = pd.DataFrame(data)
        df.to_excel("Dados_Albion.xlsx", index=False)

    else:
        print("A resposta não é uma lista. Verifique a estrutura dos dados.")

else:
    print(f"{response.status_code}, {response.text}")

import pandas as pd
import requests

# Lista de URLs
urls = [
    "https://old.west.albion-online-data.com/api/v2/stats/Prices/T4_BAG%2CT4_BAG%401%2CT4_BAG%402%2CT4_BAG%403%2CT4_BAG%404",

    "https://old.west.albion-online-data.com/api/v2/stats/Prices/T5_BAG%2CT5_BAG%401%2CT5_BAG%402%2CT5_BAG%403%2CT5_BAG%404"
]



# Parâmetros para a requisição
params = {
    "locations": "Bridgewatch, Lymhurst, Caerleon, Thetford, Martlock, Fort Sterling, Black Marketing",
    "qualities": "1,2,3,4",
}

# Loop para fazer a requisição para cada URL
for url in urls:
    response = requests.get(url, params=params)

    # Verificando se a requisição foi bem-sucedida (status 200)
    if response.status_code == 200:
        data = response.json()

        # Verificando se a resposta é uma lista e imprimindo os dados
        if isinstance(data, list):
            for item in data:
                print(f"Item: {item['item_id']} | Preço mínimo de venda: {item['sell_price_min']} | Qualidade: {item['quality']}")
            
            # Convertendo os dados para um DataFrame do pandas e salvando em um arquivo Excel
            df = pd.DataFrame(data)
            df.to_excel("Dados_Albion.xlsx", index=False)
            print(f"Dados salvos com sucesso para a URL {url}.")
        else:
            print("A resposta não é uma lista. Verifique a estrutura dos dados.")
    else:
        print(f"Erro na requisição para a URL {url}: {response.status_code}, {response.text}")

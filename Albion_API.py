import pandas as pd
import requests
import json

# Defina o idioma desejado (exemplo: PT-BR)
idioma = "PT-BR"

# Carrega o arquivo JSON com as informações dos itens
arquivo_json = 'items.json'

with open(arquivo_json, 'r', encoding='utf-8') as file:
    dados_itens = json.load(file)

# Extrai 'item_id' e informações localizadas
itens_detalhados = []
item_ids = []

for item in dados_itens:
    item_id = item.get("UniqueName")
    if item_id:
        item_ids.append(item_id)

        # Busca nomes e descrições no idioma desejado
        nome_localizado = (item.get("LocalizedNames") or {}).get(idioma, "Nome não disponível")
        descricao_localizada = (item.get("LocalizedDescriptions") or {}).get(idioma, "Descrição não disponível")

        itens_detalhados.append({
            "item_id": item_id,
            "nome": nome_localizado,
            "descricao": descricao_localizada
        })

if not item_ids:
    print("Nenhum 'item_id' encontrado no arquivo JSON.")
else:
    # Faz a requisição à API com os 'item_ids'
    url = f"https://old.west.albion-online-data.com/api/v2/stats/prices/{','.join(item_ids)}"
    params = {
        "locations": "Bridgewatch, Lymhurst, Caerleon, Thetford, Martlock, Fort Sterling, Black Marketing",
        "qualities": "1,2,3,4"
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()

        # Combina as informações da API com as localizações
        if isinstance(data, list):
            df_api = pd.DataFrame(data)
            df_itens = pd.DataFrame(itens_detalhados)

            # Mescla os dados baseados no 'item_id'
            df_final = pd.merge(df_api, df_itens, left_on="item_id", right_on="item_id", how="left")

            # Salva em Excel
            df_final.to_excel("Dados_Albion_Localizados.xlsx", index=False)
            print("Arquivo salvo como 'Dados_Albion_Localizados.xlsx'.")
        else:
            print("A resposta não é uma lista. Verifique a estrutura dos dados.")
    else:
        print(f"Erro na requisição: {response.status_code}, {response.text}")

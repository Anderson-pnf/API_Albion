import pandas as pd
import requests

url = "https://old.west.albion-online-data.com/api/v2/stats/prices/t4_bag,t4_bag@1,t4_bag@2,t4_bag@3,t4_bag@4,t5_bag,t5_bag@1,t5_bag@2,t5_bag@3,t5_bag@4,t6_bag,t6_bag@1,t6_bag@2,t6_bag@3,t6_bag@4,t7_bag,t7_bag@1,t7_bag@2,t7_bag@3,t7_bag@4,t8_bag,t8_bag@1,t8_bag@2,t8_bag@3,t8_bag@4"

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

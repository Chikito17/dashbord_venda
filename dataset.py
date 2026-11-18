import json
import pandas as pd

"""
o arquivo dataset manipula os dados do arquivo json e o transforma em um dicionario

"""

file = open('dados/vendas.json')
data = json.load(file)

#print(data)

df = pd.DataFrame.from_dict(data)

#print(df)

df['Data da Compra'] = pd.to_datetime(df['Data da Compra'], format='%d/%m/%Y')

file.close()
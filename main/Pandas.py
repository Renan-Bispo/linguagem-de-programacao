from operator import index

import pandas as pd

data = [10,20,30,40,50]

#criando uma Series a partir de uma lista
series1 = pd.Series(data)
print(series1)

#criando uma Series a partir de um dicionario
data_dic = {'A': 100, 'B': 200, 'C': 300, 'D': 400, 'E': 500}

series2 = pd.Series(data_dic)
print(series2)

# url = 'https://www.fdic.gov/resources/resolutions/bank-failures/failed-bank-list/'
#
# dfs = pd.read_html(url)
#
#
#
# df_bancos = dfs[0]
# print(df_bancos.shape)

# PRÁTICA
dados = {
    'Nome':  ['Alice', 'Bob', 'Carol', 'David', 'Eve'],

    'Idade': [25,30,22,35,28]
}
#exibir dados da series
series_idades = pd.Series(dados['Idade'], index=dados['Nome'])

print("Series de idades:")
print(series_idades)
#calcular e meia entre as idades
media_idades = series_idades.mean()
print("Média de idades:\n",media_idades)

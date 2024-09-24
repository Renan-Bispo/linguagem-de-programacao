import pandas as pd
from datetime import date
from datetime import datetime as dt


# df_selic = pd.read_json('https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json')
# print(df_selic.info())
#
#
# data_extracao = date.today()
#
# df_selic['data_extracao'] = data_extracao
# df_selic['responsavel'] = "Renan"
#
#
# print(df_selic.head())
# print(df_selic.loc[3])

#PRATICA

data = {
    'nome': ['Produto A', 'Produto B', 'Produto A', 'Produto E'],
    'itens comprados': [3,1,4,3,2],
    'tipo do item': ['Eletrônico', 'Vestuário', 'Alimento', 'Eletrônico', 'Alimento'],
    'receita total': [120,80,60,120,90]
}

df = pd.DataFrame(data)



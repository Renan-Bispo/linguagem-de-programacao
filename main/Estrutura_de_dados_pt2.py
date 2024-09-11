# SET
import numpy as np

meu_conjunto = set()
meu_conjunto.add(10)
meu_conjunto.add(20)
meu_conjunto.add(30)

print("Conjunto após adicionar elementos: ", meu_conjunto)
elemento = 40

if elemento in meu_conjunto:
    print(f"{elemento} está presente no conjunto.")
else:

    print(f"{elemento} não está presente no conjunto.")

meu_conjunto.remove(20)
print("Conjunto atualizado: ", meu_conjunto)

# Exemplo 1 - Criação de um dicionário vazio, seguido de atribuição de chaves e valores
dici_1 = {}
dici_1['nome'] = "Maria"
dici_1['idade'] = 47

# Exemplo 2 - Criação de um dicionário com pares chave: valor
dici_2 = {'nome': "Maria", 'idade': 47}

# Exemplo 3 - Criação de um dicionário com uma lista de tuplas representando pares chave: valor
dici_3 = dict([('nome', "Maria"), ('idade', 47)])

# Exemplo 4 - Criação de um dicionário usando a função built-in zip() e duas listas, uma para as chaves e outra para os valores
dici_4 = dict(zip(['nome', 'idade'], ["Maria", 47]))
print(dici_1 == dici_2 == dici_3 == dici_4)  # Deve imprimir True
print(dici_4)

my_array = np.array([1, 2, 3, 4, 5])
print("Array original: ", my_array)

squared_array = my_array ** 2
print("Array ao quadrado: ", squared_array)
sum_of_elements = np.sum(my_array)
print("Soma de todos os elementos: ", sum_of_elements)

# ATIVIDADE PRÁTICA
participantes = [
    {
        'nome': "Alice",
        'localizacao': "EUA",
        'afiliacao': "Universidade A",
        'interesses': ["Física", "Astronomia"]
    },

    {
        'nome': "Bob",
        'localizacao': "Brasil",
        'afiliacao': "Instituto B",
        'interesses': ["Biologia", "Astronomia"]
    },

    {
        'nome': "Charlie",
        'localizacao': "Índia",
        'afiliacao': "Instituto C",
        'interesses': ["Química", "Engenharia"]
    }

]

# Usando sets para identificar diferentes regiões dos participantes
regioes = set(participante['localizacao'] for participante in participantes)
print("Regiões dos participantes: ", regioes)
afiliacoes = {}
for participante in participantes:
    afiliacao = participante['afiliacao']
    if afiliacao not in afiliacoes:
        afiliacoes[afiliacao] = []
    afiliacoes[afiliacao].append(participante["nome"])
print("Afiliação dos participantes:")
for afiliacao, nomes in afiliacoes.items():
    print(f"{afiliacao}: {','.join(nomes)}")

areas_de_interesse = np.array([interesse for participante in participantes for interesse in participante['interesses']])
interesses_unicos, contagem = np.unique(areas_de_interesse, return_counts=True)
area_mais_popular = interesses_unicos[np.argmax(contagem)]
print("Área de interesse mais popular: ",area_mais_popular)
texto = "Explorando a diversidade das linguagens de programação com Python"
#operações que podem ser aplicadas a sequências.
print(f"Tamanho do texto: {len(texto)}")
print(f"Palavra Python presente no texto: {'Python' in texto}")
print(f"Quantidade de E no texto: {texto.count('e')}")
print(f"As primeiras cinco letras do texto: {texto[:5]}")


#trabalhando com listas:
cores = ['Vermelho', 'Azul', 'Verde', 'Amarelo', 'Roxo']

for cor in cores:
    print(f"Posição = {cores.index(cor)}, cor = {cor}")


#as list comprehensions
linguagens = ['Python', 'Java', 'JavaScript', 'C', 'C#', 'C++','Swift', 'Go', 'Kotlin']
print("Antes de aplicar o comprehencions = ", linguagens)

linguagens = [item.lower() for item in linguagens]

print("Depois de aplicar o comprehencions = ", linguagens)

#utilizando o metodo MAP
precos_em_dolares = [120,72,12,40,360]
taxa_de_cambio = 5.25
precos_em_reais = list(map(lambda x: x * taxa_de_cambio, precos_em_dolares))
print("preços em reais", precos_em_reais)


#utilizando o metodo FILTER
numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))
print(numeros_pares)
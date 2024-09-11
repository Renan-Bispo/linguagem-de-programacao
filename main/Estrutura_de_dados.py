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

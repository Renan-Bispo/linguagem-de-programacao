# def soma(a, b):
#     resultado = a + b
#     return resultado
#
# resultado_soma = soma(5, 4)
# print(f"O resultado da soma é: {resultado_soma}")
#
# soma = lambda a,b: a+b
# resultado = soma(2,3)
# print(resultado)
#
# notas = [6.7, 8.0, 7.1, 9.4, 4.4]
# def media_alunos(notas):
#     total = sum(notas)
#     media = total / len(notas)
#     return media
#
# media_aluno = media_alunos(notas)
# print(media_aluno)

numeros = [1, 2, 3, 4, 5]

soma = 0

for numero in numeros:
    soma += numero

media = soma / len(numeros)

print(media)
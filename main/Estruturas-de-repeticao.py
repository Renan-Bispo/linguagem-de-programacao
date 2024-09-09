# numeros = [1, 2, 3, 4, 5]
#
# for num in numeros:
#     print(num)
from unicodedata import numeric

# numero = int(input("Digite um número ou digite 0 para sair: "))
# while numero != 0:
#     if numero % 2 == 0:
#         print('O número é par')
#     else:
#         print('O numero é ímpar')
#     numero = int(input("Digite um número ou digite 0 para sair: "))
#
# for y in range(2, 7):
#     print(y)

# for number in range(1, 11):
#     if number % 2 == 0:
#         print(f'O primeiro numero par : {number}')
#         break

# for numero in range(1, 11):
#     if numero == 5:
#         continue
#     print(numero)


filmes = ['Filme 1', 'Filme 2', 'Filme 3', 'Filme 4', 'Filme 5']

print("Bem-vindo a avaliação de filmes")
print("Digite 0 para sair a qualquer momento.")

for filme in filmes:
    classificacao = input(f"Dê uma nota de 1 a 5 ao filme : {filme} ou digite 0 para sair.")

    if classificacao == 0:
        print("Uma pena que não deseja avaliar nossos filmes :(")
        break

    classificacao = int(classificacao)

    if classificacao < 1 or classificacao > 5:
        print("Digite uma avaliação válida (De 1 a 5)")
        break
    else:
        print(f"Você classificou o filme {filme} com {classificacao} estrelas")


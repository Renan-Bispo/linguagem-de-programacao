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

for numero in range(1, 11):
    if numero == 5:
        continue
    print(numero)

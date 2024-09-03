nota_1 = int(input('Primeira nota: '))
nota_2 = int(input('Segunda nota: '))
nota_3 = int(input('Terceira nota: '))
nota_4 = int(input('Qaurta nota: '))
media = (nota_1 + nota_2 + nota_3 + nota_4)

if media >= 6:
    print(f"Aluno aprovado com média -> {media}")
else:
    print (f"Aluno reprovado com média {media}")



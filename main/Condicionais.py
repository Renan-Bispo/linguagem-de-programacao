idade = int(input("Ola, por favor diga sua idade: "))

if idade <= 12:
    print("Os filmes recomendados são: "
          "Filme 1 & Filme 2")
elif 12 > idade < 18:
    print("Os filmes recomendados são: "
          "Filme 3 & Filme 4")
else:
    print("Os filmes recomendados são: "
          "Filme 5 & Filme 6")

ingressos = 5

if ingressos > 0:
    print("Ainda há cadeiras disponiveis, compre seu ingresso")
else:
    print("Sinto muito, os ingressos estão esgotados")
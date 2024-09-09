
def add_nota():
    notas = []
    while True:

            nota = float(input("Adicione suas notas (ou digite -1 para sair): "))
            if nota == -1:
                break
            elif 0 <= nota <= 10:
                notas.append(nota)
            else:
                print ("nota invalida")
    return notas

def calcular_media(notas):
    if len(notas) == 0:
        return 0
    return sum(notas)/ len(notas)

def sitacao_do_aluno(media):
    if media >= 7:
        print (f"Aluno aprovado com média: {media}")
    else:
        print(f"Aluno reprovado com média: {media}")

def main ():
    print("Sistema de Gestão de Notas de Alunos")
    notas = add_nota()
    media = calcular_media(notas)
    situacao = sitacao_do_aluno(media)



if __name__ == "__main__":
    main()
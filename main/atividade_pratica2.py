import matplotlib.pyplot as plt
from fontTools.misc.cython import returns


class Livro:
    def __init__(self, titulo, autor, genero):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero


    def __repr__(self):
        return f"{self.titulo} por {self.autor} ({self.genero})"

def add_livro(lista_livro, titulo, autor, genero):
    novo_livro = Livro(titulo, autor, genero)
    lista_livro.append(novo_livro)

def remove_livro(lista_livro, titulo):
    for livro in lista_livro:
        if livro.titulo == titulo:
            lista_livro.remove(livro)
            print(f"Livro {livro.titulo} foi removido")



def listar_livros(lista_livro):
    if not lista_livro:
        print("Nenhum livro encontrado")
    else:
        print("Lista de livros:")
        for livro in lista_livro:
            print(livro)

def busca_livro_titulo(lista_livro, titulo):
    for livro in lista_livro:
        if livro.titulo == titulo:
            print(livro)
        else:
            print("Livro não encontrado")

def contagem_genero(lista_livro):
    contagens = {}

    for livro in lista_livro:
        genero = livro.genero
        if genero in contagens:
            contagens[genero] += 1
        else:
            contagens[genero] = 1

    return contagens

def plotar_livro(contagens):
    genero = list(contagens.keys())
    quantidade = list(contagens.values())
    plt.bar(genero, quantidade)
    plt.xlabel('Gêneros')
    plt.ylabel('Número de livros')
    plt.show()

livros = []

add_livro(livros,"Até que nada mais importe", "Luciano Subirá", "Religioso")
add_livro(livros,"O sermão do monte", "Aquele cara", "Religioso")
add_livro(livros,"O poder da autorresponsaiblidade", "Quem escreveu", "auto-ajuda")


busca_livro_titulo(livros, "Até que nada mais importe")
contagem = contagem_genero(livros)
plotar_livro(contagem)
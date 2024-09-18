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

livros = []

add_livro(livros,"Até que nada mais importe", "Luciano Subirá", "Religioso")
add_livro(livros,"O sermão do monte", "Aquele cara", "Religioso")
add_livro(livros,"O poder da autorresponsaiblidade", "Quem escreveu", "auto-ajuda")


busca_livro_titulo(livros, "Até que nada mais importe")
class Pessoa:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def greet(self):
        return f"Olá, eu me chamo {self.name}"

    def birthday (self):
        self.age += 1


pessoa1 = Pessoa("João", 22, "Masculino")
print(pessoa1.greet()) #usando metodo de saudação
print(pessoa1.age) #idade antes do aniversario
pessoa1.birthday() #metodo de aniversario
print(pessoa1.age) #idade depois do aniversario


#Herança
class Animal:
    def __init__(self, name):
        self.name = name
    def fazer_barulho(self):
        pass
class Cachorro(Animal):
    def fazer_barulho(self):
        return "AU AU"

class Gato(Animal):
    def fazer_barulho(self):
        return "MIAU MAIU"

rex = Cachorro("Rex")
print(f"{rex.name} faz {rex.fazer_barulho()}")
xaina = Gato("Xaina")
print(f"{xaina.name} faz {xaina.fazer_barulho()}")


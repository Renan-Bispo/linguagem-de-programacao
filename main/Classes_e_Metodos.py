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

#Atividade pratica
class Veiculo:
    def __init__(self, mark, model,year):
        self.mark = mark
        self.model = model
        self.year = year
        self.speed = 0

    def accelerate(self, increment):
        self.speed += increment

    def brake(self, decrement):
        self.speed -= decrement

    def status(self):
        return f"Marca: {self.mark}, Modelo: {self.model}, Ano: {self.year}, Velocidade: {self.speed} km/h"


class Car(Veiculo):
    def __init__(self, mark, model, year, power):
        super().__init__(mark, model, year)
        self.power = power

    def accelerate(self, increment):
        self.speed += increment + self.power

carro1 = Car("Toyta", "Supra Mk4", 2008, 130)

carro1.accelerate(80)

print(carro1.status())
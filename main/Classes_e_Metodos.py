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
print(pessoa1.greet())
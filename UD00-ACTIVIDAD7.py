import random
import string


class Car:

    def __init__(self, matricula, color):
        self.matricula = matricula
        self.color = color

    def imprimir(self):
        print("Matrícula:", self.matricula)
        print("Color:", self.color)

    def arrancar(self):
        print("El coche ha arrancado")

    def parar(self):
        print("El coche se ha parado")


n = int(input("¿Cuántos coches quieres crear? "))

colores = ["red", "white", "black", "pink", "blue"]

coches = []

for i in range(n): #dependiendo del numero de coches que hayamos decidido crear, haremos lo siguiente:

    randomMatricula=""
    for j in range(4):

        randomMatricula= randomMatricula+random.choice(string.ascii_uppercase)

    matricula = randomMatricula + str(random.randint(1,9999)) #para que la matricula empiece desde el 1

    color = random.choice(colores) #escogemos un color random

    coche = Car(matricula, color) #creamos el coche

    coches.append(coche) #y lo añadimos a la lista de coches


cantidad = min(n, 10)# mmostramos maximo 10 coches

for i in range(cantidad):

    coches[i].imprimir()
    print()
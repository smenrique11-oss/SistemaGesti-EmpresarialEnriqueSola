import sys



"""
Para poder realizar la sobrecarga de metodos, haremos dos metodos con el mismo nombre.

En Python, si definimos dos funciones con el mismo nombre, la segunda definición sustituye a la primera.
"""

def sobrecargaSuma(numeroUno, numeroDos):

    return numeroUno+numeroDos #este metodo recoge SOLAMENTE dos numeros

def sobrecargaSuma(*numeros):


    return sum(numeros) #este metodo, al tener el * en numeros, coge indefinidamente los valores. 
    #puede coger1,2,3,4,5 y hasta infinitos valores


def sobrecargaSuma2(*numeros):

    resultado=0

    for numero in numeros:

        resultado= resultado+numero

    return resultado
#este metodo lo hacemos de otra manero, utilizando un bucle para recorrer todos los numeros que hemos metido y sumarlos para dar un resultado


print(sobrecargaSuma(5,6,7,3,2,4,1))
print(sobrecargaSuma2(10,20,30))




"""
nombre = sys.argv[1]
edad = sys.argv[2]
ciudad = sys.argv[3]

print("Nombre:", nombre)
print("Edad:", edad)
print("Ciudad:", ciudad)



EN LA TERMINAL SE ESCRIBE: python3 programa.py Enrique 18 Valencia para que devuelva los datos desde la consola


"""

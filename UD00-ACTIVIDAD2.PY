

#Reva 2 números i torne la suma.

def sumaNumeros(numeroUno, numeroDos): #hacemos un metodo (def) que coja dos numeros
    resultado= numeroUno+numeroDos
    return (resultado)

primerNumero= int(input("Dame un número entero: ")) #input para coger los numeros por consola
segundoNumero= int(input("Dame otro número entero: "))

print(f"El resultado es: {sumaNumeros(primerNumero, segundoNumero)}") 


#Reva una llista i modifique eixa mateixa llista (referència) doblant els valors de tots els
#elements. No ha de retornar res.
def doblarLista(listaNumeros): #hacemos un metodo que coge la lista
        for i in range(len(listaNumeros)): #recorremos la longitud de la lista
            listaNumeros[i] = listaNumeros[i]*2 #multiplicamos todos los valores por 2
listaNumeros = [1,2,3,4]

doblarLista(listaNumeros)

print(listaNumeros)

"""Reva una llista i torne una còpia de la llista mateixa llista (referència) doblant els valors de
tots els elements. La llista original no hi ha de modificar-se."""

def copiaLista(listaNumeros):
    listaCopiada = listaNumeros.copy()
    for i in range(len(listaCopiada)):
        listaCopiada[i] = listaCopiada[i]*2
    return listaCopiada

listaOriginal = [1, 2, 3, 4]

listaNueva = copiaLista(listaOriginal)

print(listaOriginal)
print(listaNueva)







"""creamos una lista que dentro de otra lista guarda dos datos, altura y peso"""

listaAlturaPeso = [[180,70],[180,40],[177,80],[177,100],[147,30]]


"""creamos un metodo para ordenar según nos han pedido, 
de mayor a menos altura, y en caso de igualdad, 
estar delante la de menor peso, como haremos esto?"""

def ordenar(listaAlturaPeso) :

    altura= listaAlturaPeso[0] #cogemos el dato de la altura y lo definimos
    peso= listaAlturaPeso[1] #cogemos el dato del peso y lo definimos
    return -altura, peso #decimos que nos devuelva la altura de forma inversa, para que nos de el numero mas alto de altura el primero
#y el peso no lo hacemos inverso, para que nos de el mas bajo


listaAlturaPeso.sort(key=ordenar) #utilizamos el key para que sepa de que manera tenemos que ordenar la lista (de manera en la que hemos puesto en la funcion ordenar)

print (str(listaAlturaPeso))


"""

OTRO EJEMPLO

"""

def ordenar(listaAlturaPeso) :

    altura= listaAlturaPeso[0] 
    peso= listaAlturaPeso[1]
    return altura, -peso

listaAlturaPeso.sort(key=ordenar, reverse=True) #también podemos hacerlo a la inversa en el metodo, y en el key poner el reverse true)

print (str(listaAlturaPeso))
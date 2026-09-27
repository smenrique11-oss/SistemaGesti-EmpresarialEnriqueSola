# crear una lista -> [e1,e2,e3 ...]

import copy


listaEjemplo1 = ["pepino","huevo","Patata"]
listaEjemplo2 = ["Agua","CocaCola","Leche"]

print(listaEjemplo1)
print(listaEjemplo2)

#Shallow copy
#Clonar una llista.
listaShallowCopy = copy.copy(listaEjemplo1)
#Deep copy
listaDeepCopy = copy.deepcopy(listaShallowCopy[1:4])
print(f"LISTA DEEP COPY: "+str(listaDeepCopy))
print(f"LISTA SHALLOW COPY: "+str(listaShallowCopy))

"""

deep copy copia hasta los objetos que hay dentro de una lista, en cambio shallow copy, no

"""


#Afegir un element a una llista.

listaEjemplo2.append("Fanta") #append  sirve para añadir un elemento a la lista
print(f"LISTA AÑADIR 1: "+str(listaEjemplo2)) #str para pasar la lista a string

print(f'posición lista 1: {id(listaEjemplo1)}, posición lista 2: {id(listaEjemplo2)} , posición lista shallow copy: {id(listaShallowCopy)}') 
#ponemos el id para que nos diga la posicion de la lista

#Llevar un element a una llista.

listaEjemplo1.remove("huevo") #.remove para borrar un elemento de la lista, ya sea por posicion o directamente con el nombre
print(f"LISTA REMOVE 1: "+str(listaEjemplo1))

#Crear una nova llista amb els 4 últims elements d’una llista.
listaEjemploAñadiendo4 = listaEjemplo2[-4:] #el -4 significa que cogemos los ultimas 4 elementos de la lista
print(f"LISTA AÑADIENDO LOS ULTIMOS 4 DE OTRA LISTA: "+str(listaEjemploAñadiendo4))

#Convertir les paraules 
# d’una cadena (separades per espai) a una llista.

cadenaPalabras = "hola adios hasta luego hasta nunca"
listaPalabras = cadenaPalabras.split()
print(f"LISTA PALABRAS SEPARADAS: "+str(listaPalabras))


#COMENTARIOS DE UNA LINEA

"""

ESTO ES UN
COMENTARIO MULTILINEA

"""




from functools import reduce



cadena = input("Introduce números separados por espacios: ")
"""
introduces la cadena por scanner
"""
cadenaSpliteada=cadena.split()
""" la partimos """
listaNumerosSpliteados = list(map(int, cadenaSpliteada))
""" map lo que hace en este caso es convertir toda la cadena a int
pasa de por ejmplo: "12" a 12
y el list lo que hace es convertirlo a una lista, ya que el map no lo hace
"""

listaFiltradaDiez= list(filter(lambda numero:numero >= 10, listaNumerosSpliteados))
""" este filter significa que le llega un numero a la funcion,
 lo compara con los de la lista y solo se queda con los mayores de 10"""

listaFiltradaCinco= list(filter(lambda numero: "5" in str(numero), listaNumerosSpliteados))
""" este filter significa que cualquier numero que lleve el 5 en la lista lo coja"""

listaFiltradaCincoMas= list(filter(lambda numero: "5" in str(numero) and numero>=20, listaNumerosSpliteados))
""" este filter significa que cualquier numero que lleve el 5 y sea mayor de 20 en la lista lo coja"""

resultado = reduce(lambda a, b: a * b, listaFiltradaDiez, 1)
""" el reduce en este caso, reduce todos los numeros a uno solo, y en el lambda hemos puesto que multiplique todos los numeros"""

print(listaNumerosSpliteados)

print(listaFiltradaDiez)

print(listaFiltradaCinco)

print (resultado)
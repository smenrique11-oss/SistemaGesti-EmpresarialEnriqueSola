
import sys


def esPalindromo(numero):
    """
    >>> esPalindromo(5)
    True
    >>> esPalindromo(11)
    True
    >>> esPalindromo(14)
    False
    >>> esPalindromo(12321)
    True
    """

    numero = str(numero)

    return numero == numero[::-1]


def esPrimo(numero):
    """
    >>> esPrimo(2)
    True
    >>> esPrimo(7)
    True
    >>> esPrimo(11)
    True
    >>> esPrimo(14)
    False
    >>> esPrimo(15)
    False
    """

    if numero < 2:
        return False

    for i in range(2, numero):
        if numero % i == 0:
            return False

    return True


def leerFichero(nombreFichero):
    numeros = []

    with open(nombreFichero, "r") as fichero:
        for linea in fichero:
            numero = int(linea.strip())
            numeros.append(numero)

    return numeros


def procesarNumeros(numeros):
    palindromos = 0
    primos = 0
    listaPalindromosPrimos = []

    for numero in numeros:

        if esPalindromo(numero):
            palindromos += 1

        if esPrimo(numero):
            primos += 1

        if esPalindromo(numero) and esPrimo(numero):
            listaPalindromosPrimos.append(numero)

    return palindromos, primos, listaPalindromosPrimos


def escribirFichero(nombreFichero, palindromos, primos, lista):
    with open(nombreFichero, "w") as fichero:

        fichero.write("Hi han " + str(palindromos) + " numeros palíndroms.\n")
        fichero.write("Hi han " + str(primos) + " numeros cosins.\n")

        for numero in lista:
            fichero.write(str(numero) + "\n")


if len(sys.argv) != 3:
    print("Ús: programa.py fitxerEntrada fitxerEixida")
    sys.exit()


nombreEntrada = sys.argv[1]
nombreSalida = sys.argv[2]

numeros = leerFichero(nombreEntrada)

palindromos, primos, lista = procesarNumeros(numeros)

escribirFichero(nombreSalida, palindromos, primos, lista)


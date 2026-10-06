def esSudokuCorrecto(miArrayBi):

    # comprobar filas
    for fila in miArrayBi:
        """ recorremos las filas, y decimos que si la longitud no es igual a 9, que devuelva false"""
        if len(set(fila)) != 9:
            return False

    # Comprobar columnas
    for columna in range(9):
        numeros = []

        for fila in range(9):
            numeros.append(miArrayBi[fila][columna])

        if len(set(numeros)) != 9:
            return False

    # Comprobar regiones 3x3
    for filaInicio in range(0, 9, 3):
        for columnaInicio in range(0, 9, 3):

            numeros = []

            for fila in range(filaInicio, filaInicio + 3):
                for columna in range(columnaInicio, columnaInicio + 3):
                    numeros.append(miArrayBi[fila][columna])

            if len(set(numeros)) != 9:
                return False

    return True


# Abrimos el archivo
archivo = open("Sudoku.in", "r")

# Creamos el array
miArrayBi = []

# Leemos las 9 líneas
for linea in archivo:
    numeros = linea.split()
    numeros = list(map(int, numeros))
    miArrayBi.append(numeros)

archivo.close()


# Mostramos el Sudoku
for fila in miArrayBi:
    print(fila)


# Comprobamos si es correcto
if esSudokuCorrecto(miArrayBi):
    print("El Sudoku es correcto")
else:
    print("El Sudoku NO es correcto")
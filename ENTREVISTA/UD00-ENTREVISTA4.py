def contandoMinas(miCampo):

    resultado = []

    filas = len(miCampo)
    columnas = len(miCampo[0])

    for fila in range(filas):

        nuevaFila = []

        for columna in range(columnas):

            if miCampo[fila][columna] == -1:
                nuevaFila.append(-1)

            else:

                minas = 0

                for i in range(fila - 1, fila + 2):
                    for j in range(columna - 1, columna + 2):

                        if i >= 0 and i < filas and j >= 0 and j < columnas:

                            if miCampo[i][j] == -1:
                                minas += 1

                nuevaFila.append(minas)

        resultado.append(nuevaFila)

    return resultado


miCampo = [
    [0, 0, -1, 0],
    [0, 0, 0, 0],
    [-1, 0, 0, 0],
    [0, 0, 0, -1]
]

resultado = contandoMinas(miCampo)

for fila in resultado:
    print(fila)
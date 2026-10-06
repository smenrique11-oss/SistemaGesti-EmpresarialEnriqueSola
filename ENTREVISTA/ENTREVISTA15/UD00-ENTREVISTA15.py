
import sys
import time
import os
import re
import pyperclip


# carga las palabras prohibidas que hay dentro del archivo
def cargarPalabras(ruta):

    # comprobamos que el archivo indicado exista
    if not os.path.isfile(ruta):
        raise FileNotFoundError("no se encuentra el archivo.")

    # lista donde iremos almacenando las palabras
    palabras = []

    # abrimos el archivo para leer una palabra en cada linea
    with open(ruta, "r", encoding="utf-8") as fichero:

        # recorremos todas las lineas del archivo
        for linea in fichero:

            # quitamos espacios y saltos de linea
            palabra = linea.strip()

            # solamente guardamos las lineas que tengan contenido
            if palabra != "":
                palabras.append(palabra)

    # devolvemos la lista completa
    return palabras


# busca y sustituye las palabras prohibidas del texto
def filtrarTexto(texto, palabras):

    # comprobamos una por una las palabras de la lista
    for palabra in palabras:

        # preparamos la palabra para utilizarla dentro de una expresion regular
        patron = re.escape(palabra)

        # sustituimos cada coincidencia por tantos asteriscos como caracteres tenga
        texto = re.sub(
            patron,
            lambda coincidencia: "*" * len(coincidencia.group()),
            texto,
            flags=re.IGNORECASE
        )

    # devolvemos el texto despues de aplicar todos los filtros
    return texto


# se queda comprobando continuamente lo que hay en el portapapeles
def supervisarPortapapeles(palabras):

    # guardamos lo que habia inicialmente para poder detectar cambios
    ultimoTexto = pyperclip.paste()

    print("programa iniciado.")
    print("copia un texto para comprobar las palabras prohibidas.")
    print("pulsa ctrl+c para terminar.")

    try:

        # mantenemos el programa funcionando hasta que el usuario lo cierre
        while True:

            # obtenemos el contenido actual del portapapeles
            textoActual = pyperclip.paste()

            # solamente actuamos si el contenido ha cambiado
            if textoActual != ultimoTexto:

                # pasamos el texto por el filtro
                textoNuevo = filtrarTexto(textoActual, palabras)

                # si el filtro ha encontrado alguna palabra, actualizamos el portapapeles
                if textoNuevo != textoActual:
                    pyperclip.copy(textoNuevo)
                    print("texto filtrado:", textoNuevo)

                # guardamos el texto que acabamos de procesar
                ultimoTexto = textoNuevo

            # esperamos medio segundo antes de volver a comprobar
            time.sleep(0.5)

    except KeyboardInterrupt:

        # permite cerrar el programa utilizando ctrl+c
        print("\nprograma finalizado.")


if __name__ == "__main__":

    # comprobamos que se haya indicado el archivo con las palabras
    if len(sys.argv) != 2:
        print("uso: python UD00-ENTREVISTA15.py lista.txt")
        sys.exit(1)

    try:

        # cargamos las palabras prohibidas del archivo
        palabras = cargarPalabras(sys.argv[1])

        # comprobamos que el archivo tenga alguna palabra
        if not palabras:
            print("el archivo no contiene palabras prohibidas.")
        else:

            # comenzamos a controlar el portapapeles
            supervisarPortapapeles(palabras)

    except FileNotFoundError as error:

        # mostramos el problema si no se encuentra el archivo
        print("error:", error)

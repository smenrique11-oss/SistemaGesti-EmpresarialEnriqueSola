
import csv
import sys
import os
import barcode
from barcode.writer import ImageWriter


def generarCodigos(archivoCSV):

    # comprobamos primero si el archivo indicado existe
    if not os.path.isfile(archivoCSV):
        print("error: el archivo csv no existe.")
        return

    # abrimos el archivo para poder leer sus datos
    with open(archivoCSV, "r", encoding="utf-8-sig", newline="") as fichero:

        # convertimos las filas del csv en datos que podemos utilizar
        lector = csv.DictReader(fichero)

        # comprobamos que el archivo tenga las columnas necesarias
        if lector.fieldnames is None:
            print("error: el csv no tiene columnas.")
            return

        if "nombre" not in lector.fieldnames or "ID" not in lector.fieldnames:
            print("error: el csv debe tener las columnas nombre e ID.")
            return

        # recorremos cada alumno que aparece en el archivo
        for alumno in lector:

            # obtenemos el nombre y el identificador del alumno
            nombre = alumno["nombre"].strip()
            identificador = alumno["ID"].strip()

            # comprobamos que ambos datos tengan contenido
            if nombre == "" or identificador == "":
                print("alumno con datos incompletos. se omite.")
                continue

            # comprobamos que el id este formado solamente por numeros
            if not identificador.isdigit():
                print("id no valido para:", nombre)
                continue

            # ean 13 utiliza 12 numeros para calcular el ultimo digito
            if len(identificador) > 12:
                print("id demasiado largo para:", nombre)
                continue

            # añadimos ceros delante hasta tener 12 numeros
            codigo = identificador.zfill(12)

            # preparamos el codigo de barras con formato ean13
            ean = barcode.get("ean13", codigo, writer=ImageWriter())

            # cambiamos los caracteres que no sean validos para un nombre de archivo
            nombreArchivo = ""

            for caracter in nombre:
                if caracter.isalnum() or caracter in " _-":
                    nombreArchivo += caracter
                else:
                    nombreArchivo += "_"

            # guardamos el codigo generado en formato png
            ean.save(nombreArchivo)

            print("codigo generado:", nombreArchivo + ".png")


if __name__ == "__main__":

    # comprobamos que se haya indicado un archivo al ejecutar el programa
    if len(sys.argv) != 2:
        print("uso: python Act9Parte2.py alumnos.csv")
        sys.exit(1)

    # enviamos el nombre del csv a la funcion principal
    generarCodigos(sys.argv[1])


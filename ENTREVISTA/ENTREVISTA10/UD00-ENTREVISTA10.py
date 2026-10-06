
import os
import sys
import cv2
from pyzbar.pyzbar import decode


def leerCodigos(directorio):

    # comprobamos que la carpeta indicada exista
    if not os.path.isdir(directorio):
        print("error: el directorio no existe.")
        return

    # obtenemos todos los elementos que hay dentro de la carpeta
    archivos = os.listdir(directorio)

    # recorremos cada elemento encontrado
    for archivo in archivos:

        # nos quedamos solamente con los archivos que terminan en png
        if archivo.lower().endswith(".png"):

            # juntamos la carpeta y el nombre del archivo para obtener su ruta
            ruta = os.path.join(directorio, archivo)

            # cargamos la imagen usando opencv
            imagen = cv2.imread(ruta)

            # comprobamos que la imagen se haya podido abrir correctamente
            if imagen is None:
                print("no se puede leer:", archivo)
                continue

            # intentamos encontrar un codigo de barras dentro de la imagen
            codigos = decode(imagen)

            # obtenemos el nombre del alumno quitando la extension png
            nombreAlumno = os.path.splitext(archivo)[0]

            # comprobamos si se ha encontrado algun codigo de barras
            if not codigos:
                print(nombreAlumno, "- no se ha encontrado ningun codigo.")
                continue

            # recorremos los codigos que haya encontrado la libreria
            for codigo in codigos:

                # obtenemos los datos del codigo y los convertimos a texto
                identificador = codigo.data.decode("utf-8")

                # mostramos la informacion del alumno
                print("alumno:", nombreAlumno)
                print("id:", identificador)
                print("--------------------")


if __name__ == "__main__":

    # comprobamos que se haya pasado una carpeta como argumento
    if len(sys.argv) != 2:
        print("uso: python UD00-ENTREVISTA10.py imagenes")
        sys.exit(1)

    # llamamos a la funcion utilizando el directorio recibido
    leerCodigos(sys.argv[1])

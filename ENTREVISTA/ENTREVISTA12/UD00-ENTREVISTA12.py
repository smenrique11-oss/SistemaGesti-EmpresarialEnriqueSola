import sys
import pytesseract
from PIL import Image, ImageFilter, ImageOps


def reconocerTexto(rutaImagen):

    # cargamos la imagen que hemos recibido por parametro
    imagen = Image.open(rutaImagen)

    # pasamos la imagen a blanco y negro para facilitar el reconocimiento
    imagen = ImageOps.grayscale(imagen)

    # aplicamos un filtro para mejorar la definicion del texto
    imagen = imagen.filter(ImageFilter.SHARPEN)

    # utilizamos tesseract para intentar detectar las palabras de la imagen
    texto = pytesseract.image_to_string(
        imagen,
        lang="spa",
        config="--psm 6"
    )

    # devolvemos todo el texto que haya encontrado
    return texto


if __name__ == "__main__":

    # comprobamos que el usuario haya indicado una imagen
    if len(sys.argv) != 2:
        print("uso: python UD00-ENTREVISTA12.py imagen.png")
        sys.exit(1)

    try:

        # llamamos a la funcion pasando la ruta de la imagen
        resultado = reconocerTexto(sys.argv[1])

        # mostramos por pantalla el texto detectado
        print("texto reconocido:")
        print(resultado)

    except FileNotFoundError:

        # mostramos un aviso si la imagen no existe
        print("error: no se encuentra la imagen.")

    except pytesseract.TesseractNotFoundError:

        # este error aparece si tesseract no esta instalado o no se encuentra
        print("error: no se encuentra tesseract ocr.")


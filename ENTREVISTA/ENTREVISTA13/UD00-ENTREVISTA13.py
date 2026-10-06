
import requests


def buscarPersonajes(especie):

    # guardamos la direccion donde se encuentra la api
    url = "https://rickandmortyapi.com/api/character/"

    # preparamos los datos que enviaremos para hacer la busqueda
    parametros = {
        "species": especie,
        "page": 1
    }

    # aqui iremos contando todos los personajes encontrados
    total = 0

    try:

        # hacemos una peticion a la api utilizando el metodo get
        respuesta = requests.get(
            url,
            params=parametros,
            timeout=10
        )

        # comprobamos si el servidor ha respondido correctamente
        respuesta.raise_for_status()

        # convertimos la respuesta recibida en formato json
        datos = respuesta.json()

        # si no hay resultados, terminamos la funcion
        if datos["info"]["count"] == 0:
            print("no se han encontrado personajes.")
            return

        # seguimos buscando mientras la api tenga mas paginas
        while True:

            # mostramos los personajes que aparecen en la pagina actual
            for personaje in datos["results"]:

                print("nombre:", personaje["name"])
                print("especie:", personaje["species"])
                print("estado:", personaje["status"])
                print("--------------------")

                # aumentamos el contador de personajes
                total += 1

            # obtenemos la direccion de la siguiente pagina
            siguiente = datos["info"]["next"]

            # si no hay otra pagina, terminamos el bucle
            if siguiente is None:
                break

            # hacemos otra peticion utilizando la url de la siguiente pagina
            respuesta = requests.get(siguiente, timeout=10)
            respuesta.raise_for_status()

            # guardamos los datos de la nueva pagina
            datos = respuesta.json()

        # mostramos cuantos personajes hemos encontrado en total
        print("total de personajes:", total)

    except requests.exceptions.Timeout:

        # se ejecuta si la respuesta tarda demasiado
        print("error: la peticion ha tardado demasiado.")

    except requests.exceptions.ConnectionError:

        # se ejecuta cuando no podemos conectar con el servidor
        print("error: no se ha podido conectar con la api.")

    except requests.exceptions.HTTPError as error:

        # mostramos el codigo de error enviado por el servidor
        print("error http:", error)

    except requests.exceptions.RequestException as error:

        # capturamos cualquier otro problema relacionado con requests
        print("error en la peticion:", error)


if __name__ == "__main__":

    # pedimos al usuario la especie que quiere buscar
    especie = input("introduce una especie: ").strip()

    # comprobamos que no haya dejado el campo vacio
    if especie == "":
        print("debes introducir una especie.")
    else:

        # llamamos a la funcion para buscar los personajes
        buscarPersonajes(especie)


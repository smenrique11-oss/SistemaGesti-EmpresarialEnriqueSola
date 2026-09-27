import hashlib

listaUsuarios = []
usuariosDiccionario={}

#OJO, no se crea de la misma forma un diccionario y una lista

"""

creamos usuarios y contraseñas NORMALES

"""
usuario1= "Pepetonto"
contraseña1="1234"


usuario2= "Jose"
contraseña2="hola34"


usuario3= "Pedrotonto"
contraseña3="adios67"


usuario4= "Marcos"
contraseña4="contraseñaSegura"

usuario5= "Xavi"
contraseña5="xaviEl_mejor"


"""
aqui las pasamos a hashcode como nos han pedido, utilizando sha256
"""
contraseña_hash1= hashlib.sha256(contraseña1.encode()).hexdigest() #encode convierte el texto a datos que hashlib pueda procesar
contraseña_hash2= hashlib.sha256(contraseña2.encode()).hexdigest() #hexdigest convierte el hashcode en texto que podemos utilizar
contraseña_hash3= hashlib.sha256(contraseña3.encode()).hexdigest()
contraseña_hash4= hashlib.sha256(contraseña4.encode()).hexdigest()
contraseña_hash5= hashlib.sha256(contraseña5.encode()).hexdigest()

listaUsuarios.append([usuario1,contraseña_hash1]) #añadimos los usuarios y contraseñas a la lista
listaUsuarios.append([usuario2,contraseña_hash2])
listaUsuarios.append([usuario3,contraseña_hash3])
listaUsuarios.append([usuario4,contraseña_hash4])
listaUsuarios.append([usuario5,contraseña_hash5])

print(listaUsuarios)


"""
AHORA VAMOS A HACERLO CON DICCIONARIO
"""

usuariosDiccionario [usuario1]=contraseña_hash1 
usuariosDiccionario [usuario2]=contraseña_hash2 
usuariosDiccionario [usuario3]=contraseña_hash3 
usuariosDiccionario [usuario4]=contraseña_hash4 
usuariosDiccionario [usuario5]=contraseña_hash5 

"""

de esta forma, no tenemos que utilizar el append, ya que es un diccionario y no una lista

y para cada usuario le podemos asignar su contraseña de forma mas sencilla

"""
print(usuariosDiccionario)

def comprobarContraseñas(usuario, contraseñaHash, listaUsuarios) :

    print(f"Buscando el perfil con usuario: "+usuario+ " y contraseña: "+contraseñaHash)
    for usuarioLista in listaUsuarios:
        if usuarioLista[0] == usuario and usuarioLista[1]== contraseñaHash:
            print("El usuario y la contraseña existen y coinciden")

            return True
        else:
            return print("Ha habido un error, el usuario y la contraseña introducidos no estan en la base de datos o no coinciden")


            """
            aqui lo que he hecho es hacer una consulta para ver si la contraseña y el usuario coinciden
            correctamente con uno de los perfiles creados en la lista, si no, indica que esta mal puesto o que no existe
            """

def comprobarPalabrasOfensivas(usuario) :
    palabrasOfensivas = ["tonto","idiota","gilipollas"]

    for palabra in palabrasOfensivas:
        if palabra in usuario:
            return True
        else:
            return False

        """
        esta funcion busca en el usuario que le demos si hay algun nombre ofensivo
        """

def comprobarUsuarioOfensivo(usuariosDiccionario):

    for usuario in usuariosDiccionario:
        if comprobarPalabrasOfensivas(usuario) == True:
            print("El usuario "+usuario+" contiene palabras ofensivas")

            """
            aqui recorremos la lista en busca de usuarios con nombres ofensivos
            """
            

comprobarContraseñas(usuario1,contraseña_hash1, listaUsuarios)
comprobarContraseñas(usuario1,contraseña_hash2, listaUsuarios)
comprobarContraseñas("juanito","9999", listaUsuarios)

comprobarUsuarioOfensivo(usuariosDiccionario)



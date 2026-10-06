
import csv
import hashlib
import os

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class VentanaLogin(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # configuramos la ventana para colocar los elementos uno debajo de otro
        self.orientation = "vertical"

        # dejamos un margen entre el contenido y los bordes
        self.padding = 30

        # definimos la distancia entre los diferentes elementos
        self.spacing = 15

        # aqui guardaremos los usuarios junto con su contraseña cifrada
        self.usuarios = {}

        # buscamos los usuarios guardados en el archivo csv
        self.cargarUsuarios()

        # añadimos un texto como titulo de la aplicacion
        self.titulo = Label(
            text="INICIO DE SESION",
            font_size=24
        )
        self.add_widget(self.titulo)

        # creamos el campo donde se escribira el nombre del usuario
        self.campoUsuario = TextInput(
            hint_text="Usuario",
            multiline=False
        )
        self.add_widget(self.campoUsuario)

        # creamos el campo para introducir la contraseña
        self.campoContrasena = TextInput(
            hint_text="Contrasena",
            password=True,
            multiline=False
        )
        self.add_widget(self.campoContrasena)

        # creamos el boton que iniciara la comprobacion
        self.boton = Button(
            text="Comprobar",
            size_hint=(1, 0.5)
        )

        # relacionamos el boton con la funcion que comprobara el login
        self.boton.bind(on_press=self.comprobarLogin)

        self.add_widget(self.boton)

        # etiqueta que utilizaremos para mostrar si el acceso es correcto
        self.mensaje = Label(text="")
        self.add_widget(self.mensaje)

    def cargarUsuarios(self):

        # buscamos users.csv en la misma carpeta que este programa
        ruta = os.path.join(os.path.dirname(__file__), "users.csv")

        # si no encontramos el archivo, avisamos y terminamos la funcion
        if not os.path.isfile(ruta):
            print("no se encuentra users.csv")
            return

        # abrimos el csv para obtener los usuarios almacenados
        with open(ruta, "r", encoding="utf-8", newline="") as fichero:

            # convertimos las filas del archivo en datos que podemos utilizar
            lector = csv.DictReader(fichero)

            # recorremos todos los usuarios del archivo
            for fila in lector:

                # guardamos el nombre y el hash de cada usuario
                usuario = fila["usuario"].strip()
                hashContrasena = fila["hash"].strip()

                # asociamos el usuario con su contraseña cifrada
                self.usuarios[usuario] = hashContrasena

    def comprobarLogin(self, boton):

        # recogemos lo que ha escrito el usuario en los campos
        usuario = self.campoUsuario.text.strip()
        contrasena = self.campoContrasena.text

        # convertimos la contraseña introducida a SHA1
        hashIntroducido = hashlib.sha1(
            contrasena.encode("utf-8")
        ).hexdigest()

        # primero comprobamos que el usuario este registrado
        if usuario in self.usuarios:

            # comparamos el hash guardado con el que acabamos de calcular
            if hashIntroducido == self.usuarios[usuario]:
                self.mensaje.text = "OK"
                self.mensaje.color = (0, 0.7, 0, 1)
                return

        # si alguna de las comprobaciones falla, mostramos un error
        self.mensaje.text = "ERROR"
        self.mensaje.color = (1, 0, 0, 1)


class AplicacionLogin(App):

    def build(self):

        # indicamos a kivy cual sera la interfaz principal
        return VentanaLogin()


if __name__ == "__main__":

    # iniciamos la aplicacion
    AplicacionLogin().run()

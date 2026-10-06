
from ENTREVISTA6 import Escuela, Profesor, Alumno, Session


# abrimos una sesion para trabajar con la base de datos
with Session() as session:

    # buscamos una escuela que tenga el nombre indicado
    escuela = session.query(Escuela).filter_by(nombre="IES Fausti").first()

    # comprobamos si la escuela no existe
    if escuela is None:

        # creamos una nueva escuela
        escuela = Escuela(nombre="IES Fausti")
        session.add(escuela)

        # creamos un profesor para la escuela
        profesor = Profesor(
            nombre="Pepe",
            dni="123233B",
            especialidad="Python"
        )

        # creamos un alumno para la escuela
        alumno = Alumno(
            nombre="Pedro",
            dni="333A",
            curso="DAM"
        )

        # añadimos el profesor a la lista de profesores de la escuela
        escuela.profesores.append(profesor)

        # añadimos el alumno a la lista de alumnos de la escuela
        escuela.alumnos.append(alumno)

        # guardamos todos los cambios en la base de datos
        session.commit()

    # mostramos el nombre de la escuela
    print("Escuela:", escuela.nombre)

    # recorremos todos los profesores de la escuela
    for profesor in escuela.profesores:
        print(profesor.nombre, profesor.dni, profesor.especialidad)

    # recorremos todos los alumnos de la escuela
    for alumno in escuela.alumnos:
        print(alumno.nombre, alumno.dni, alumno.curso)


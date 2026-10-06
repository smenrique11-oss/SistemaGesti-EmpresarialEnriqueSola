from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from ENTREVISTA5BASE import Base
from ENTREVISTA5ESCOLA import ENTREVISTA5ESCOLA
from ENTREVISTA5PROFESOR import ENTREVISTA5PROFESOR
from ENTREVISTA5ALUMNE import ENTREVISTA5ALUMNE


# Creamos la conexión con SQLite
engine = create_engine("sqlite:///escola.db")

# Creamos las tablas
Base.metadata.create_all(engine)

# Creamos una sesión
Session = sessionmaker(bind=engine)
session = Session()


# CREAR OBJETOS

escola1 = ENTREVISTA5ESCOLA(
    nom="IES Faustí Barberà",
    localitat="Aldaia",
    responsable="Director"
)

professor1 = ENTREVISTA5PROFESOR(
    nom="Joan",
    tipus="Ciències"
)

professor2 = ENTREVISTA5PROFESOR(
    nom="Maria",
    tipus="Lletres"
)


alumne1 = ENTREVISTA5ALUMNE(
    nom="Enrique",
    curs="2 DAM",
    professor=professor1
)

alumne2 = ENTREVISTA5ALUMNE(
    nom="Alex",
    curs="2 DAM",
    professor=professor2
)


# RELACIONES

escola1.professors.append(professor1)
escola1.professors.append(professor2)

escola1.alumnes.append(alumne1)
escola1.alumnes.append(alumne2)


# GUARDAMOS LOS OBJETOS EN LA BASE DE DATOS

session.add(escola1)
session.commit()

Base.metadata.create_all(engine)


# ==========================================================
# PRUEBA DE PERSISTENCIA
# ==========================================================
# Cierra el programa y vuelve a ejecutarlo.
# Los datos seguirán estando en escola.db.
#
# Para comprobarlo, puedes comentar/eliminar la parte
# donde creamos los objetos y utilizar una consulta:
#
# alumnes = session.query(ENTREVISTA5ALUMNE).all()
#
# for alumne in alumnes:
#     print(alumne)
# ==========================================================
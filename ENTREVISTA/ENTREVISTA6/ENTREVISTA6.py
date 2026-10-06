
from sqlalchemy import create_engine, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, sessionmaker


# creamos la clase base de la que heredaran las clases de la base de datos
class Base(DeclarativeBase):
    pass


# creamos la clase escuela
class Escuela(Base):
    __tablename__ = "escuelas"

    # creamos los campos de la tabla escuelas
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100))

    # relacionamos una escuela con sus profesores
    profesores: Mapped[list["Profesor"]] = relationship(
        back_populates="escuela",
        cascade="all, delete-orphan"
    )

    # relacionamos una escuela con sus alumnos
    alumnos: Mapped[list["Alumno"]] = relationship(
        back_populates="escuela",
        cascade="all, delete-orphan"
    )


# creamos la clase profesor
class Profesor(Base):
    __tablename__ = "profesores"

    # creamos los datos que tendra cada profesor
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100))
    dni: Mapped[str] = mapped_column(String(20), unique=True)
    especialidad: Mapped[str] = mapped_column(String(100))
    escuela_id: Mapped[int] = mapped_column(ForeignKey("escuelas.id"))

    # relacionamos el profesor con una escuela
    escuela: Mapped["Escuela"] = relationship(back_populates="profesores")


# creamos la clase alumno
class Alumno(Base):
    __tablename__ = "alumnos"

    # creamos los datos que tendra cada alumno
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100))
    dni: Mapped[str] = mapped_column(String(20), unique=True)
    curso: Mapped[str] = mapped_column(String(50))
    escuela_id: Mapped[int] = mapped_column(ForeignKey("escuelas.id"))

    # relacionamos el alumno con una escuela
    escuela: Mapped["Escuela"] = relationship(back_populates="alumnos")


# indicamos que vamos a utilizar una base de datos sqlite
engine = create_engine("sqlite:///escuela.db")


# creamos las tablas de la base de datos si no existen
Base.metadata.create_all(engine)


# creamos el sistema que utilizaremos para abrir sesiones
Session = sessionmaker(bind=engine)


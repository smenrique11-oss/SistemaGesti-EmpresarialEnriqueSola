from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from ENTREVISTA5BASE import Base


class ENTREVISTA5ALUMNE(Base):

    __tablename__ = "alumnes"

    id = Column(Integer, primary_key=True)
    nom = Column(String)
    curs = Column(String)

    professor_id = Column(Integer, ForeignKey("professors.id"))

    professor = relationship("ENTREVISTA5PROFESOR", back_populates="alumnes")

    def __str__(self):
        return self.nom + " - " + self.curs + " - Professor: " + self.professor.nom
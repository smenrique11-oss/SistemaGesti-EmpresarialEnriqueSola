from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from ENTREVISTA5BASE import Base


class ENTREVISTA5PROFESOR(Base):

    __tablename__ = "professors"

    id = Column(Integer, primary_key=True)
    nom = Column(String)
    tipus = Column(String)

    alumnes = relationship("ENTREVISTA5ALUMNE", back_populates="professor")

    def __str__(self):
        return self.nom + " - " + self.tipus
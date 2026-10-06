from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from ENTREVISTA5BASE import Base


class ENTREVISTA5ESCOLA(Base):

    __tablename__ = "escoles"

    id = Column(Integer, primary_key=True)
    nom = Column(String)
    localitat = Column(String)
    responsable = Column(String)

    professors = relationship("ENTREVISTA5PROFESOR")
    alumnes = relationship("ENTREVISTA5ALUMNE")
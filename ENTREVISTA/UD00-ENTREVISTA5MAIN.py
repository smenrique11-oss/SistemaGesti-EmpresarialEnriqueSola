from UD00-ENTREVISTA import Escola
from Professor import Professor
from Alumne import Alumne

escola1 = Escola("IES Faustí Barberà", "Aldaia", "Director")

professor1 = Professor("Joan", "Ciències")
professor2 = Professor("Maria", "Lletres")

escola1.afegir_professor(professor1)
escola1.afegir_professor(professor2)

alumne1 = Alumne("Enrique", "2 DAM", professor1)
alumne2 = Alumne("Alex", "2 DAM", professor2)

escola1.afegir_alumne(alumne1)
escola1.afegir_alumne(alumne2)
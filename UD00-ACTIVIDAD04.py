


comidas= ["Pepino","Pizza","Hamburguesa","Kebab","Zanahoria"]
comidasNoSaludables= ["Calabaza","Pizza","Hamburguesa","Pepe"] 
comidasNadaSaludables= ["Pizza","Hamburguesa"]


def buscarComida(comidas):
        if "Zanahoria" in comidas: #Estamos diciendo que si hay zanahorias dentro de la lista haga el print de lo siguiente
            print ("En esta lista hay comida saludable")

        if "Kebab" or "Hamburguesa" or "Pizza" in comidas: #Estamos diciendo que si hay Hamburguesa o Pizza dentro de la lista haga el print de lo siguiente
            print ("En esta lista hay comida basura")    

        if "Kebab" in comidas:  #Estamos diciendo que si hay Kebab dentro de la lista haga el print de lo siguiente
            print ("En esta lista hay kebab")     

        if "Kebab" not in comidas : #Estamos diciendo que si no hay Kebab dentro de la lista haga el print de lo siguiente
            print ("En esta lista no hay kebab")

        if comidas[0] is "Pepino": #Estamos diciendo que si un elemento de la lista es exactamente lo mismo que "Pepino" haga el print de lo siguiente
            print ("El primer elemento de la lista es el pepino")
            
        if comidas[0] is not "Pepino": #Estamos diciendo que si un elemento de la lista no es exactamente lo mismo que "Pepino" haga el print de lo siguiente
            print ("El primer elemento de la lista no es el pepino")



        

        
print(comidas)
print(buscarComida(comidas))
print(comidasNoSaludables)
print(buscarComida(comidasNoSaludables))
print(comidasNadaSaludables)
print(buscarComida(comidasNadaSaludables))

#Hacemos varios ejemplos para que se vea que funcionan los if con los in, is, not y or
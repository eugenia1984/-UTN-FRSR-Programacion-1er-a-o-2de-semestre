# Funciones
def mi_funcion():
  print('Saludos!')

mi_funcion() #invoco la funcion 
mi_funcion() #invoco la funcion por segunda vez   

## Desempaquetado de listas

def show(name, lastName):
  print(name + " " + lastName)

person = ["Maria Eugenia", "Costa"]
show(person[0], person[1]) # pasamos uno por uno los datos de la lista a la función

# otro modo de hacerlo
show(*person) # esto es lo mismo que lo anterior pero lo pasamos todo junto

person2 = ("Maria Eugenia", "Costa") # desempaquetamos a través de tupla
show(*person2)

persona3 = {"lastName": "Costa", "name": "Maria Eugenia"}
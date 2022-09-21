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

# Paso de argumentos
def mi_funcion2(name, lastName): # le paso parametros
  print(f"Hola {name} {lastName}")

mi_funcion2("Euge", "Costa") # invoco la funcion con los argumentos
mi_funcion2("Juan", "Rodriguez")

# La palabra return en funciones
def sumar(a, b):
  return a+b

resultado = sumar(2,3)
print(f"EL resultado de la suma de 2 + 3 es: {resultado}")

# Valores por default en funciones
def sumar2(a=0, b=0):
  return a+b

resultado = sumar2()
print(f"Resultado de la suma: {resultado}") # da 0

resultado = sumar2(print(f"Resultado de la suma: {sumar2(1,1)}")) # da 2

# Argumentos, variables en funciones
def listarNombres(*nombres):
  for nombre in nombres: # Se va a convertir en una tupla
    print(nombre)

listarNombres(["Maria", "Analia", "Carlos"])    

# Tarea
# Defino la funcion
def sumar_valor(*args): #recibimos una cantidad de parametros indefinidos
  resultado = 0
  for valor in args: # iteramos los elementos
    rasultado += valor
  return resultado

print(sumar_valor(3, 5, 9)) # Invocamos a la funcion


# Ejercicio con funciones con *args para multiplicar
# Crear una funcion para multiplicar los valores recibidos de tipo numerico, utilizando argumentos variables *args como parametro de la funcion y regresar como resultado la multiplicacion de todos los valores pasados como argumentos

# Definimos la funcion
def multiplicar_valores(*numeros): # es mas utilizado *args
  resultado = 1 # el 0 no nos ayuda a multiplicar
  for numero in numeros:
    resultado *= numero
  return resultado

# invocamos a la funcion
print(multiplicar_valores(3,5,15)) # le pasamos argumentos
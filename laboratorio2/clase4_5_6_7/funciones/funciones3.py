#  Funciones recursivas con factorial 
def factorial(numero): # se envia cmo argumento y se recibe como parametro
  if numero == 1: # caso base
    return 1
  else:
    return numero * factorial(numero-1) # caso recursivo

resultado = factorial(5)
print(f"El factorial de 5 es:  {resultado}")

factorialACalcular = int(input("Ingrese un numero para calcular su factorial: "))
print(f"El factorail de {factorialACalcular} es {factorial(factorialACalcular)}")
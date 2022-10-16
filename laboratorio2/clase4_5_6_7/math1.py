import math # importo la clase math para utilizar sus metodos

# Ejercicio 1 : 
# Sacar la raíz cuadrada de un número positivo

numero = int(input("Ingrese un numero positivo: "))

while numero < 0:
  print("Error -> Debería ser un númeor positivo")
  numero = int(input("Ingrese un numero positivo: "))

print(f"Su raiz cuadrada es: {math.sqrt(numero):.2f}")
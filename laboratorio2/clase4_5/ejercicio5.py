# Ejercicio 5
# Hacer un programa para calcular el factorial de un numero positivo
numero = int(input("Ingrese un numero: "))

while numero < 0: # es un numero negativo
  print("Error -> El número tiene que ser positivo")
  numero = int(input("Ingrese un numero: "))

factorial = 1 # la variable para calcular el factorial

for i in range(1, numero+1):
  factorial *= i
print(f"El factorial de {numero} es: {factorial}")

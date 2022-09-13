# Ejercicio 4
# Sumar numeros pares dentro de in rango
# Hacer un programa para sumar los numeros pares dentro de un rango
# por ej.: sume de numeros pares del 2 al 30
# suma = 240
comienzoDeSuma = int(input("Ingrese de donde va a comenzar a sumar: "))
finDeLaSuma = int(input("Ingrese hasta donde quiere llegar a sumar"))
suma = 0
for i in range(comienzoDeSuma, finDeLaSuma+1):
  if i % 2 == 0:
    suma += i
print(f"La suma de los numeros pares es: {suma}")
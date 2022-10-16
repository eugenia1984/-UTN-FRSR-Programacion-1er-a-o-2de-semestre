# Ejercicio 3
# Pedir numeros y meterlos en una lista, cuando el usuario 
# introduzca un numero 0, muestro: programa dejaria de insertar.
# Por último, mostrar los números ordenados de menor a mayor.

lista= []
salir = False

while not salir: # mientras salir sea verdadero
  numero = int(input("Ingrese un numero : "))
  if numero == 0:
    salir = True
  else:
    lista.append(numero)
    
# con sort ordenamos
lista.sort()
print(f"Mi lista ordenada: {lista}")

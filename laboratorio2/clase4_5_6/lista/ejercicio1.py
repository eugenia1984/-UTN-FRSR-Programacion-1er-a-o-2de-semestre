# Ejercicio 1 : Llenar una lista
# Llenar una lista con los numeros del 1 al 50# Luego mostrar la lista con el bucle for
# Los elementos deben mostrarse de la sigueinte forma:
# 1 - 2 - 3 - 4 - 5 - .. - 50

lista = []
iterador = 1

while iterador <= 50:
  lista.append()
  iterador += 1
  
for elemento in lista:
  print(elemento, end="-")
  
# Otro modo de hacer la primer parte
lista = list(range(1, 51))
# Ahora imprimo lista
print(lista)

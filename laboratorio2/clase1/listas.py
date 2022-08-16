# LISTAs, van entre [], si los elementos son String se pueden unas comillas simples o dobles
# Una lista puede tener variables de distinto tipo de datos
nombres = ['Naty', 'Osvaldo', 'Lily', 'Ariel']
print(nombres)
# Las listas comienzan con el indice 0 para el primer elemento
print(nombres[0])
print(nombres[1])
# Para acceder al ultimo elemento, sin saber cuantos elementos tenemos utilizamos el -1
print(nombres[-1])
# Para acceder al penultimo accedemos con -2, lo recorremos a la inversa a la lista, de atras hacia adelante
print(nombres[-2])
# Para imprmir solo los elementos con indice 0 y 1 de la lista
# Le doy un rango, el segundo numero del rango no lo incluye
print(nombres[0:2])
# Para ir del inicio de la lista hasta un indice, sin incluirlo
print(nombres[ :3])
# Desde el indice indicado hasta el fnal
print(nombres[1: ])
# Para modificar un valor de la lista
nombres[2] = 'Liliana'
nombres[1] = 'Natalia'
print(nombres)
# Iterar una lista
for nombre in nombres:
  print(nombre)
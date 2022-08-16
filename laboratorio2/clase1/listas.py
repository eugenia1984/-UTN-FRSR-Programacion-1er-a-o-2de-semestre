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
# len() retorna la cantidad de elementos que tiene una lista  
print(len(nombres))
# Agregar un elemento AL FINAL -> .append()
nombres.append('Marcelo')
# Agregar un elemento en un indice especifico -> .insert()
# 1er param : el indice, que es un numero entero
# 2do param: el elemento# lo que va a hacer es desplazar un lugar hacia la derecha a los elementos que estan luego dle ingresado
nombres.insert(1, 'Alberto')
# Eliminar un elemento -> .remove()
nombres.remove('Alberto')
# Eliminar el ULTIMO elemento -> .pop()
nombres.pop()
# Eliminar con un indice especifico -> del lista[indice_elemento]
del nombres[2]
# Eliminar, borrar o limpiar todos lo elementos -> .clear()
nombres.clear()
# Eliminar la lista -> del lista
del nombres
"""
RANGE

The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.

STAR -> Optional. An integer number specifying at which position to start. Default is 0
STOP -> Required. An integer number specifying at which position to stop (not included).
STEP -> Optional. An integer number specifying the incrementation. Default is 1

x = range(6)
for n in x:
  print(n)
"""
#range(<inicio>, <fin>, <incremento>)






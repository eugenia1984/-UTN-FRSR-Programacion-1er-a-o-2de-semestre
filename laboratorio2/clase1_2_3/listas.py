# LISTAs, van entre [], si los elementos son String se pueden unas comillas simples o dobles
# En otros lenguajes se les dice array, arreglos, vectores
# Una lista puede tener variables de distinto tipo de datos

nombres = ['Naty', 'Osvaldo', 'Lily', 'Ariel']
print(nombres)

print(nombres[0]) # Las listas comienzan con el indice 0 para el primer elemento
print(nombres[1])
print(nombres[-1]) # Para acceder al ultimo elemento, sin saber cuantos elementos tenemos utilizamos el -1
print(nombres[-2]) # Para acceder al penultimo accedemos con -2, lo recorremos a la inversa a la lista, de atras hacia adelante
print(nombres[0:2]) # Para imprmir solo los elementos con indice 0 y 1 de la lista, le doy un rango, el segundo numero del rango no lo incluye
print(nombres[ :3]) # Para ir del inicio de la lista hasta un indice, sin incluirlo
print(nombres[1: ]) # Desde el indice indicado hasta el fnal

nombres[2] = 'Liliana' # Para modificar un valor de la lista
nombres[1] = 'Natalia'
print(nombres)

# Iterar una lista
for nombre in nombres:
  print(nombre)

print(len(nombres)) # len() retorna la cantidad de elementos que tiene una lista  

nombres.append('Marcelo') # Agregar un elemento AL FINAL -> .append()

# Agregar un elemento en un indice especifico -> .insert()
# 1er param : el indice, que es un numero entero
# 2do param: el elemento# lo que va a hacer es desplazar un lugar hacia la derecha a los elementos que estan luego dle ingresado
nombres.insert(1, 'Alberto')

nombres.remove('Alberto') # Eliminar un elemento -> .remove()

nombres.pop() # Eliminar el ULTIMO elemento -> .pop()

del nombres[2] # Eliminar con un indice especifico -> del lista[indice_elemento]

nombres.clear() # Eliminar, borrar o limpiar todos lo elementos -> .clear()

del nombres # Eliminar la lista -> del lista

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

# Dentro de una lista pueden haber distintos tipos de datos, inclusive otra lista
names = ['Ana', 'Maria']
names.append('Marcelo')
names.append([1, 2, 3])
names.append(True)
names.append(10.45)
names.append(6)
print(f"Lista names: {names}") # Lista names: ['Ana', 'Maria', 'Marcelo', [1, 2, 3], True, 10.45, 6]

# Concatenacion de listas
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista3 = lista1+lista2
print(lista3) # [1, 2, 3, 4, 5, 6]

# Para agregar varios elementos a una lista con .extend(), se agregan al final
lista3.extend( [7, 8, 9])
print(lista3) # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Para saber en que indice esta un elemento con .index()
# Si paso por parametro un valor que no esta en la lista me arroja un error de que no esta en la lista (... is not in list)
print(f"El quinto elemento es: {lista3.index(5)}") # El quinto elemento es: 4

# En una lista puede haber varios valores repetidos, para saber cuantos hay repetidos con .count()
lista3.extend([1, 1])
print(lista3.count(1)) # 3

# Pra poner una lista al reves con .reverse()
lista3.reverse()
print(lista3) # [1, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# Para que una lista se multiplique repitiendo sus elementos
lista = [1, 2, 3] * 2
print(lista) # [1, 2, 3, 1, 2, 3]

# Metodo de ordenamiento que en Python se convirtio en funcion, por default los ordena en modo ascendente: .sort()
lista.sort()
print(f"Lista ordenada con sort: {lista}") # Lista ordenada con sort: [1, 1, 2, 2, 3, 3]

# Para ordenarla de manera descendiente
lista.sort(reverse=True)
print(f"Lista ordenada de mayor a menor con sort y reverse: {lista}") # Lista ordenada de mayor a menor con sort y reverse: [3, 3, 2, 2, 1, 1]


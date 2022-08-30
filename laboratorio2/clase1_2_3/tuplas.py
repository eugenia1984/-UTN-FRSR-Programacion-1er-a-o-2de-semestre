# A diferencia de la lista, las tuplas son INMODIFICABLES
# Las tuplas se declaran entre ()
# Las tuplas permiten elementos repetidos
# Puede guardar distitnots tipos de datos

cocina = ('cuchara', 'cuchillo', 'tenedor')
print(cocina)

print(len(cocina)) # len() para ver cuantos elementos hay

print(cocina[0]) # para acceder a un elemento utilizo []
print(cocina[-1]) # para acceder al ultimo elemento [-1]
print(cocina[0:1]) # para acceder a un rango [inicio:fin] el fin no lo incluye

verdura = ('papa') # es un String no una tupla porque le falta la coma
verduras = ('papa',) # es una tupla porque tiene la coma

# Recorremos los elementos de la tupla con un ciclo for
for elemento in cocina:
  print(elemento, end=' ') # Asi modificamos el \n que tiene print
# cocina[0] = 'plato' no puedo hacerlo porque las tuplas no son mutables

del cocina # para eliminar la tupla

# Los elementos de las tuplas pueden ser de distintos tipos de datos
tupla = (4, 'Hola', 6.78, [1, 2, 3], 4, 'Hola')
print(f"tupla: {tupla}") # Muestra todos los elementos

# Se puede transformar una lista en tupla y una tupala en lista, pero no es aconsejable

print(4 in tupla) # Para buscar si un elemento esta en la tupla

print(4 not in tupla) # Para buscar si un elemento no esta en la tupla
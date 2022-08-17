# A difernecia de la lista las tuplas son INMODIFICABLES
# Las tuplas se declaran entre ()
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
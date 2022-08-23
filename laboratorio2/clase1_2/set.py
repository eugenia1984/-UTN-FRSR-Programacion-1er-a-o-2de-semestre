# SET, no tiene un orden y no permite almacenar elementos duplicado ni repetidos. 
# No se puede modificar, pero si se puede agregar o eliminar, no es completamente mutable ni completamente inmutable.
# Set no mantiene ningún indice, el orden es aleatorio al mandar a imprimir
# Set es una colección sin nombre ni indices
# Van entre {}
planetas = {'Marte', 'Júpiter', 'Venus'}
print(planetas) # si lo imprmimo mas de una vez voy a ver que el orden es aleatorio
print(len(planetas)) # para ver la cantidad de elementos que tiene el conjunto / set
print('Marte' in planetas) # Para saber si un elemento existe en el set
planetas.add('Tierra') # Para agregar un elemento al set
planetas.add('Tierra') # Al imprimir voy a er una sola vez Tierra ya que no puede tener elementos repetidos
print(planetas)
planetas.remove('Júpiter') # Para eliminar un elemento, si quiero eliminar un elemento que o esta en el set voy a tener error (key error)
print(planetas)
planetas.discard('Tierra') # Para eliminar un elemento, en este caso si el elemento no esta en el set no tenemos error
print(planetas)
planetas.clear() # para limpiar el set, dejarlo vacio
del planetas # para eliminar el set, si lo imprimo me da error, ya que no existe
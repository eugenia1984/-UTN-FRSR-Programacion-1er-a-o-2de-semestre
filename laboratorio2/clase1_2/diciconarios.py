# DICCIONARIOS
# Es una coleccion de datos organizados en key:value
# Los diccionarios van entre {} y sus key:value se separan entre coma
diccionario = {
  'IDE': 'Integrated Development Enviroment',
  'POO': 'Programación Orientada a Objetos',
  'SABD': 'Sistema de Adminsitración de Base de Datos'
}
print(diccionario)
# Como key puede ser: int, float, boolean, string, etc
print(len(diccionario)) # para saber la cantidad de elementos
print(diccionario['IDE']) # para acceder a un elemento se hace por la key y se muestra el value
print(diccionario.get('POO')) # Otra forma de ver el value, mediante la key
diccionario['IDE'] = 'Entorno de Desarrollo Integrado'# Modificamos un elemento
print(diccionario['IDE'])
for termino in diccionario: # Para recorrer lo elemento con un bucle for  imprimir los key
  print(termino)
for termino, valor in diccionario.items(): # con la funcion .items() podemos ver tanto el value del elemento
  print(termino, valor)
# Otras maneras de acceder a un diccionario  
for termino in diccionario.keys(): # con la funcion .keys() podemos ver las key del elemento
  print(termino) 
for valor in diccionario.values(): # con lafuncion .values() muestra los valores sin las {}
  print(valor)
print('IDE' in diccionario) # Para comprobar la existencia de algun elemento  
print('IDE' not in diccionario) # Para comprobar si no existe un determinado elemento 
diccionario['PK'] = 'Primary Key' # Para agregar un elemento
# Recordar que los diccionarios no aceptan tener key duplicadas, deben ser únicas, si quiero agregar otro elemento con una key ya evistente me va a sobreescribir el value
print(diccionario)
diccionario.pop('SABD') # Para eliminar un elemento, nombro a la key pero elimina key y value
print(diccionario)
diccionario.clear() # Para borrar todos los elementos del diciconario
print(diccionario)
del diccionario # para borrar el diccionario
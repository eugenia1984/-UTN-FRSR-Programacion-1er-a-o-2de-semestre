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

# Los diccionarios pueden almacenar distinto tipo de datos

diccionario2 = { 
  'Ariel': {'Edad': 40, 'Altura': 1.83},
  'Osvaldo': [45, 1.85],
  'Natalia': [35, 1.67]
}
print(diccionario2)

seleccionArgentina = {
  10: {'Nombre':'Lionel Messi','Edad': 35,'Altura': 1.70,'Precio': '50 millones','Posicion':'Extremo derecho'},
  11: {'Nombre': 'Angel Di Maria','Edad': 34,'Altura': 1.80,'Precio': '12 millones','Posicion': 'Extremo derecho'},
  24: {'Nombre': 'Paulo Dybala','Edad': 28,'Altura': 1.77,'Precio': '35 millones','Posicion': 'Media Punta'},
  19: {'Nombre': 'Nicolas Otamendi','Edad': 34,'Altura': 1.83,'Precio': '3.5 millones','Posicion': 'Defensa Central'},
  1: {'Nombre':'Franco Armani','Edad':35,'Altura':1.89,'Precio':'3.5 millones','Posicion':'Portero'}
}

for llave, valor in seleccionArgentina.items():
  print(llave, valor)
# Tarea: agregar por lo menos 4 jugaadores mas en el diccionario: seleecionArgentina
# Agrego un jugador
seleccionArgentina['25'] = {'Nombre': 'Lisandro Martínez', 'Edad': 24, 'Altura': 1.75, 'Precio': '54 Millones', 'Posicion': 'Defensa'}
# Agrego un segundo jugador
seleccionArgentina['18'] = {'Nombre': 'Guido Rodríguez', 'Edad': 28, 'Altura': 1.85, 'Precio': '80 Millones', 'Posicion': 'Centrocampista'}
# Agrego un tercer jugador
seleccionArgentina['27'] =  {'Nombre': 'Julian Alvarez', 'Edad': 22, 'Altura': 1.73, 'Precio': '51 Millones', 'Posicion': 'Delantero'}
# Agrego un cuarto jugador
seleccionArgentina['8'] = {'Nombre': 'Marcos Javier Acuña',  'Edad': 30, 'Altura': 1.72, 'Precio': '15 Millones', 'Posicion': 'Defensa'}
# Imprimo de nuevo el diccionario con todos los jugadores
print("El diccionario con los 4 jugadores agregados")
for llave, valor in seleccionArgentina.items():
  print(llave, valor)
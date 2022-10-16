# Ejercicio 3 : 
# Escriba un programa donde cree una lista con los sigueintes personajes del señor de los anillos
#  Nombre: Aragon
# Clase : Guerrero 
# Raza: Dunadan del norte

# Nombre: Gandalf
# Clase: Mago
# Raza: Istar

# Nombre: Legolas
# Clase ; Arquero
# Raza : Elfo Sindar

personajes = [] # creamos una lista vacia
# creamos el diccionario de Aragon
personaje1 = {"Nombre": "Aragon", "Clase": "Guerrero", "Raza": "Dunadan del norte"}
# Y lo agregamos a la lista
personajes.append(personaje1)
# creamos el diccionario de Gandal
personaje2 = {"Nombre": "Gandalf", "Clase": "Mago", "Raza": "Istar"}
# Y lo agregamos a la lista
personajes.append(personaje2)
# creamos el diccionario de Legolas
personaje3 = {"Nombre": "Legolas", "Clase": "Arquero", "Raza": "Elfo Sindar"}
# Y lo agregamos a la lista
personajes.append(personaje3)
print(f"Mi lista de personajes: {personajes}")


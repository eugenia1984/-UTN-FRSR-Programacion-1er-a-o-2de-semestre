# Ejercicio 1: Eliminar duplicados de una lista
# Escriba un programa donde tenga una lista y que a continuación 
# elimine los elemento repetidos, por ultimo mostrar los elementos de la lista
lista =  [ 1, 2, 1, 3, "Eugenia", 7, 7, 3, "Analia", 5, "Eugenia"]; # Creamos una lista
conjunto = set(lista) #  convierto de lista a set (porque los set no tienen elementos repetidos)
print(f"Mi conjunto: {conjunto}") #  Se ve por consola: {1, 2, 3, 5, 7, 'Analia', 'Eugenia'}
lista1 = list(conjunto) # lo volvo a pasar a lista
print(f"Mi lista sin repetir: {lista1}") # Imprimo la lista
# Se ve por consola: Mi lista sin repetir: [1, 2, 3, 5, 7, 'Eugenia', 'Analia']
# Haciendo lo mismo pero todo junto en un solo renglon
lista2 = list(set(lista))
print(f"Mi lista pasada a set y a lista, todo junto: {lista2}")
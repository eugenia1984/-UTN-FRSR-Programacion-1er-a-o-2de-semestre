# Ejercicio 2
# Llenar una lista con los numeros del 1 al 10, 
# luego modificar los elementos de la lista 
# multiplicandolos por un valor ingresado por el usuario

lista  = list(range(1,11)) #con la funcion range arma la lista dle 1 al 10
print("Lista original:")
for i in lista:
  print(i, end="-")
  
valor = int(input("Ingrese un valor a multiplicar: "))

# multiplicamos toods los elementos de la lista
# el iterador solo recorre los elementos
# necesitamos trabajar con los indices, por eso agregamos enumerate
for indice, i in enumerate(lista):
  lista[indice] *= valor
  
print(f"Lista final con los elementos multiplicados por: {valor}")

for i in lista:
  print(i, end="-")

# Ejercicio 10
# Hacer un programa que pida una cadena por teclado, luego meter los caracteres en una lista sin repetir caracteres.
cadenaIngresada = input("Ingrese una frase: ")
lista = [] # creo una lista

for i in cadenaIngresada: # recorro la cadena ingresada y la asigno a la lista
  if (i not in cadenaIngresada): # si el caracter aun no esta en la lista
    lista.append(i) # lo agrego

conjunto = set(lista) # lo paso a set para no tneer duplicados

print(f"Lista de caracteres sin repetir: {conjunto}")

# ​lista = list(set(input("Ingrese una cadena: ")))
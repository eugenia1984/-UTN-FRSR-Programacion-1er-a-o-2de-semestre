# :star: Clase 4

---

# COLECCIONES

## Ejercicio 1: Eliminar duplicados de una lista

Escriba un programa donde tenga una lista y que a continuación elimine los elemento repetidos, por ultimo mostrar los elementos de la lista

---

## Ejercicio 2

Escriba un programa que tenga 2 listas y que a continuacion cree las sigueintes listas (en las que no deben haber repeticion)

1. lista de palabras que aparecen en las listas

2. lista de palabras que aparecen en la primera lista, pero no en la segunda

3. lista de palabras que aparecen en al segunda, pero no en la primera

4. lista de palabras que aparecen en ambas listas

---

## Ejercicio 3

Escriba un programa donde cree una lista con los sigueintes personajes del señor de los anillos

Nombre: Aragon

Clase : Guerrero
Raza: Dunadan del norte

Nombre: Gandalf

Clase: Mago

Raza: Istar

Nombre: Legolas

Clase ; Arquero

Raza : Elfo Sindar

---

# LISTA

# Ejercicio 1 : Llenar una lista

Llenar una lista con los numeros del 1 al 50. Luego mostrar la lista con el bucle for.  Los elementos deben mostrarse de la sigueinte forma:

1 - 2 - 3 - 4 - 5 - .. - 50


---

## Ejercicio 2

Llenar una lista con los numeros del 1 al 10, luego modificar los elementos de la lista multiplicandolos por un valor ingresado por el usuario

---

## Ejercicio 3

Pedir numeros y meterlos en una lista, cuando el usuario introduzca un numero 0, muestro: programa dejaria de insertar.

Por último, mostrar los números ordenados de menor a mayor.

---
---

# :star: Clase 5

---

## Ejercicio 4

Sumar numeros pares dentro de in rango

Hacer un programa para sumar los numeros pares dentro de un rango

Por ej.: sume de numeros pares del 2 al 30

suma = 240

```Python
comienzoDeSuma = int(input("Ingrese de donde va a comenzar a sumar: "))
finDeLaSuma = int(input("Ingrese hasta donde quiere llegar a sumar"))
suma = 0
for i in range(comienzoDeSuma, finDeLaSuma+1):
  if i % 2 == 0:
    suma += i
print(f"La suma de los numeros pares es: {suma}")
```

---

## Ejercicio 5

Hacer un programa para calcular el factorial de un numero positivo

```Python
numero = int(input("Ingrese un numero: "))

while numero < 0: # es un numero negativo
  print("Error -> El número tiene que ser positivo")
  numero = int(input("Ingrese un numero: "))

factorial = 1 # la variable para calcular el factorial

for i in range(1, numero+1):
  factorial *= i
print(f"El factorial de {numero} es: {factorial}")
```

---
# :star: Clase 4

---

# COLECCIONES

## Ejercicio 1: Eliminar duplicados de una lista

Escriba un programa donde tenga una lista y que a continuación elimine los elemento repetidos, por ultimo mostrar los elementos de la lista.

```Python
lista =  [ 1, 2, 1, 3, "Eugenia", 7, 7, 3, "Analia", 5, "Eugenia"]; # Creamos una lista
conjunto = set(lista) #  convierto de lista a set (porque los set no tienen elementos repetidos)
print(f"Mi conjunto: {conjunto}") #  Se ve por consola: {1, 2, 3, 5, 7, 'Analia', 'Eugenia'}
lista1 = list(conjunto) # lo volvo a pasar a lista
print(f"Mi lista sin repetir: {lista1}") # Imprimo la lista
# Se ve por consola: Mi lista sin repetir: [1, 2, 3, 5, 7, 'Eugenia', 'Analia']
# Haciendo lo mismo pero todo junto en un solo renglon
lista2 = list(set(lista))
print(f"Mi lista pasada a set y a lista, todo junto: {lista2}")
```

-> Lo podes ver en [**ejercicio1.py**](https://github.com/eugenia1984/UTN-FRSR-Programacion-1year-2semester/blob/main/laboratorio2/clase4_5/ejercicio1.py)

---

## Ejercicio 2

Escriba un programa que tenga 2 listas y que a continuacion cree las siguientes listas (en las que no deben haber repeticion)

1. lista de palabras que aparecen en las listas

2. lista de palabras que aparecen en la primera lista, pero no en la segunda

3. lista de palabras que aparecen en al segunda, pero no en la primera

4. lista de palabras que aparecen en ambas listas

```Python

lista1 = [ 1, 2, 3, 4, 5, 4, 3, 2, 2, 1, 5]
lista2 = [ 4, 5, 6, 7, 8, 4, 5, 6, 7, 7, 8]
# Eliminar los elementos repetidos de ambas listas pasandolos a conjuntos(set)
conjunto1 = set(lista1)
conjunto2 = set(lista2)

union = list(conjunto1 | conjunto2 ) # unimos los dos conjuntos
solo1 = list(conjunto1 - conjunto2) # solo muestra el conjunto 1
solo2 = list(conjunto2 - conjunto1) # solo muestra el conjunto 2
interseccion = list(conjunto1 & conjunto2)
print(f"Lista de palabras que aparecen en las listas: {union}")
print(f"Lista de palabras que aparecen en la primera lista, pero no en la segunda: {solo1}")
print(f"Lista de palabras que aparecen en al segunda, pero no en la primera: {solo2}")
print(f"Lista de palabras que aparecen en ambas listas: {interseccion}")
```

-> Lo podes ver en [**ejercicio2.py**](https://github.com/eugenia1984/UTN-FRSR-Programacion-1year-2semester/blob/main/laboratorio2/clase4_5/ejercicio2.py)

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

```Python
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
```

-> Lo podes ver en [**ejercicio3.py**](https://github.com/eugenia1984/UTN-FRSR-Programacion-1year-2semester/blob/main/laboratorio2/clase4_5/ejercicio3.py)

---

# Ejercicio con la clase math

## math 1

Sacar la raíz cuadrada de un número positivo

```Python
import math # importo la clase math para utilizar sus metodos

numero = int(input("Ingrese un numero positivo: "))

while numero < 0:
  print("Error -> Debería ser un númeor positivo")
  numero = int(input("Ingrese un numero positivo: "))

print(f"Su raiz cuadrada es: {math.sqrt(numero):.2f}")
```

 -> Lo podes ver en [**math1.py**](https://github.com/eugenia1984/UTN-FRSR-Programacion-1year-2semester/blob/main/laboratorio2/clase4_5/math1.py)

---

# LISTA

# Ejercicio 1 : Llenar una lista

Llenar una lista con los numeros del 1 al 50. 

Luego mostrar la lista con el bucle for.  

Los elementos deben mostrarse de la siguiente forma:

1 - 2 - 3 - 4 - 5 - .. - 50

```Python
lista = []
iterador = 1

while iterador <= 50:
  lista.append()
  iterador += 1
  
for elemento in lista:
  print(elemento, end="-")
  
# Otro modo de hacer la primer parte
lista = list(range(1, 51))
# Ahora imprimo lista
print(lista)
```

 -> Lo podes ver en [**lista/ejericico1.py**](https://github.com/eugenia1984/UTN-FRSR-Programacion-1year-2semester/blob/main/laboratorio2/clase4_5/lista/ejericio1.py)
 
---

## Ejercicio 2

Llenar una lista con los numeros del 1 al 10, luego modificar los elementos de la lista multiplicandolos por un valor ingresado por el usuario

 -> Lo podes ver en [**lista/ejerico2.py.py**](https://github.com/eugenia1984/UTN-FRSR-Programacion-1year-2semester/blob/main/laboratorio2/clase4_5/lista/ejericio2.py)
 
---

## Ejercicio 3

Pedir numeros y meterlos en una lista, cuando el usuario introduzca un numero 0, muestro: programa dejaria de insertar.

Por último, mostrar los números ordenados de menor a mayor.

 -> Lo podes ver en [**lista/ejerico3.py.py**](https://github.com/eugenia1984/UTN-FRSR-Programacion-1year-2semester/blob/main/laboratorio2/clase4_5/lista/ejericio3.py)
 
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

## :star: FUNCIONES

En un bloque de codigo que se puede ejecutar N cantidad de veces. Pero para poder utilizarla debe ser invocada.

Las funciones llevan la palabra reservada **def**.

El nombre de la función es en **snake_case**. También se suele utilizar **camelCase**.

A continuación del nombre deben ir los **()** que pueden recibir datos mediante los **parametros** y luego van los **:**. En el proximo renglon se tabula (lleva **identación**), todo el bloque que esté en esa identación será el bloque de la función.


```Python
def mi_funcion():
  print('Saludos!')

mi_funcion() #invoco la funcion  
```  

Siempre debo invocar la función luego de ser definida (declarada).

La funcion puede retornar como no.

Para poder utilizar la función en otro módulo hay que importarla para en el otro archivo exportarla.

---

## Ejercicio 6 : Tabla de multiplicar

Hacer un programa que pida un numero por teclado y guarde en una lista su tabla de multiplicar hasta el 10.

Por ejemplo:

Si digita el 5 la lista tendra: 5, 10, 15, 20, 25, 30, 35, 40, 45, 50

```Python
numero = int(input("Ingrese un numero para mostrarle su tabla de multiplicar: "))
lista = []
for i in range(1,11):
  lista.append(i*numero)

print(f"\n Tabla de multiplicar del {numero}: \n {lista}")

# Para mostrarlo como una tabla
for indice, i in enumerate(lista):
  print(f"{numero} x {i} = {lista[indice]}")
```

---

## Ejercicio 7:

Realizar un juego para adividar un numero.

Para ello se debe generar un número aleatorio entre 1 - 100 y luego ir pidiendo números indicando "es mayor" o "es menor" según sea mayor o menor con respecto a N.

El proceso termina cuando el usuario acierta y alli se debe mostrar el número de intentos.

```Python
import random # para utilizar la libreria y tener el numero random

aleatorio = random.randint(1, 100)
contador = 0
while True:
  numero = int(input("ingrese un numero: "))
  contador+=1
  if numero > aleatorio:
    print("\t No es el número. Ingresa un número menor.")
  elif numero < aleatorio:
    print("\t No es el número. Ingrese un número mayor.")
  else:
    print(f"Felicitacines, el número es {numero}")
    break

print(f"\nNúmero de intentos: {contador}")
```

---

## Ejercicio 8: Menu interactivo - Cajero automatico

Hacer un programa que simule un cajero automatico con un saldo inicial de $ 1000 y tendra el sigueinte menu de opciones:

1. Ingresar dinero en la cuenta

2. Retirar dinero de la cuenta

3. Mostrar dinero disponible

4. Salir

```Python
saldo = 1000

while True:
  print("\t.: MENU :.")
  print("1. Ingresar dinero en la cuenta")
  print("2. Retirar dinero de la cuenta")
  print("3. Mostrar dinero disponible")
  print("4. Salir")
  opcion = int(input("Ingrese una opcion del menu: "))
  print()
  if opcion == 1:
    extra = float(input("Cuanto dinero desea ingresar: "))
    saldo += extra
    print(f"Dinero en la cuenta: $ {saldo}")
  elif opcion == 2:
    retirar = float(input("Cuanto dinero desea retirar: "))
    if retirar > saldo:
      print("No tiene saldo suficiente para retirar ese monto")
    else:
      saldo -= retirar
      print(f"Dinero en la cuenta: $ {saldo}")
  elif opcion == 3:
    print(f"Dinero en la cuenta: $ {saldo}")
  elif opcion == 4:
    print("Gracias por utilizar el cajero automatico")
    break
  else:
    print("Error. Eligio una opción no valida")
    print()
```

---

## Ejercicio 9 : Mostrar una frase sin espacios y contrar su longitus

Hacer un programa donde el usuario ingrese una frase, se le devolverá la misma frase pero sin los espacios en blanco, y ademas un contador de cuántos caracteres tiene la frase (sin contar los espacios en blanco)

Ejempo:

frase = vivir por siempre en paz

frase final = vivirporsiemprenepaz

Nº de caracters = 20



```Python
frase1 = input("ingrese un numero: ")
frase2 = " "

for i in frase1:
  if i != " ":
    frase2 += i

frase1 = frase2
print(f"\nFrase final: {frase1}")
print(f"Nº de caracteres: {len(frase1)}")
```

---

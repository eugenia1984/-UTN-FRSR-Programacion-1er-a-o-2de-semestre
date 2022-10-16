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

-> Lo podes ver en [**ejercicio1.py**](https://github.com/eugenia1984/UTN-FRSR-Programacion-1year-2semester/blob/main/laboratorio2/clase4_5_6_7/ejercicio1.py)

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

-> Lo podes ver en [**ejercicio2.py**](https://github.com/eugenia1984/UTN-FRSR-Programacion-1year-2semester/blob/main/laboratorio2/clase4_5_6_7/ejercicio2.py)

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

-> Lo podes ver en [**ejercicio3.py**](https://github.com/eugenia1984/UTN-FRSR-Programacion-1year-2semester/blob/main/laboratorio2/clase4_5_6_7/ejercicio3.py)

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

 -> Lo podes ver en [**math1.py**](https://github.com/eugenia1984/UTN-FRSR-Programacion-1year-2semester/blob/main/laboratorio2/clase4_5_6_7/math1.py)

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

 -> Lo podes ver en [**lista/ejericico1.py**](https://github.com/eugenia1984/UTN-FRSR-Programacion-1year-2semester/blob/main/laboratorio2/clase4_5_6_7/lista/ejericio1.py)
 
---

## Ejercicio 2

Llenar una lista con los numeros del 1 al 10, luego modificar los elementos de la lista multiplicandolos por un valor ingresado por el usuario

```Python
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
```

 -> Lo podes ver en [**lista/ejerico2.py.py**](https://github.com/eugenia1984/UTN-FRSR-Programacion-1year-2semester/blob/main/laboratorio2/clase4_5_6_7/lista/ejericio2.py)
 
---

## Ejercicio 3

Pedir numeros y meterlos en una lista, cuando el usuario introduzca un numero 0, muestro: programa dejaria de insertar.

Por último, mostrar los números ordenados de menor a mayor.

```Python
lista= []
salir = False

while not salir: # mientras salir sea verdadero
  numero = int(input("Ingrese un numero : "))
  if numero == 0:
    salir = True
  else:
    lista.append(numero)
    
# con sort ordenamos
lista.sort()
print(f"Mi lista ordenada: {lista}")
```

 -> Lo podes ver en [**lista/ejerico3.py.py**](https://github.com/eugenia1984/UTN-FRSR-Programacion-1year-2semester/blob/main/laboratorio2/clase4_5_6_7/lista/ejericio3.py)
 
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

-> Lo podes ver en [**ejercicio4.py**](https://github.com/eugenia1984/UTN-FRSR-Programacion-1year-2semester/blob/main/laboratorio2/clase4_5_6_7/ejercicio4.py)

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
-> Lo podes ver en [**ejercicio5.py**](https://github.com/eugenia1984/UTN-FRSR-Programacion-1year-2semester/blob/main/laboratorio2/clase4_5_6_7/ejercicio5.py)

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
  print(f"{numero} x {indice+1} = {lista[indice]}")
```

-> Lo podes ver en [**ejercicio6.py**](https://github.com/eugenia1984/UTN-FRSR-Programacion-1year-2semester/blob/main/laboratorio2/clase4_5_6_7/ejercicio6.py)

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

-> Lo podes ver en [**ejercicio7.py**](https://github.com/eugenia1984/UTN-FRSR-Programacion-1year-2semester/blob/main/laboratorio2/clase4_5_6_7/ejercicio7.py)

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

-> Lo podes ver en [**ejercicio8.py**](https://github.com/eugenia1984/UTN-FRSR-Programacion-1year-2semester/blob/main/laboratorio2/clase4_5_6_7/ejercicio8.py)

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

-> Lo podes ver en [**ejercicio9.py**](https://github.com/eugenia1984/UTN-FRSR-Programacion-1year-2semester/blob/main/laboratorio2/clase4_5_6_7/ejercicio9.py)

---

## Ejercicio 10

Hacer un programa que pida una cadena por teclado, luego meter los caracteres en una lista sin repetir caracteres.

```Python
cadenaIngresada = input("Ingrese una frase: ")
lista = [] # creo una lista

for i in cadenaIngresada: # recorro la cadena ingresada y la asigno a la lista
  if (i not in cadenaIngresada): # si el caracter aun no esta en la lista
    lista.append(i) # lo agrego

conjunto = set(lista) # lo paso a set para no tneer duplicados

print(conjunto)
```

-> Lo podes ver en [**ejercicio10.py**](https://github.com/eugenia1984/UTN-FRSR-Programacion-1year-2semester/blob/main/laboratorio2/clase4_5_6_7/ejercicio10.py)

---

## Ejercicio 11 : Agenda telefonica

Hacer un programa que simule una agenda de contactos.

Crear un diciconario donde la clave sea el nombre del usuario y el valor sea el telefono, el programa tendrá el siguiente menú de opciones:

1. Nuevo contacto

2. Borrar contacto

3. Ver contactos existentes

4. Salir

```Python
agenda = {
  "Eugenia": 1111111111,
  "Sonia": 2222222222,
  "Matias": 3333333333,
  "Rodrigo": 4444444444,
  "Pablo": 5555555555
}

while True:
  print(".: MENU :.")
  print("1. Nuevo contacto")
  print("2. Borrar contacto")
  print("3. Ver contactos existentes")
  print("4. Salir")
  opcion = int(input("Ingrese una opcion de menu: "))
  if opcion == 1:
    nombre = input("Digite el nombre del contacto: ")
    telefono = input("Ingrese el telefono: ")
    if nombre not in agenda:
      print("contacto ingresado")
    else:
      print("Este nombre de contacto ya existe")
  elif opcion == 2:
    nombre = input("Cual es el nombre del contacto: ")
    if nombre in agenda:
      del(agenda[nombre])
      print("Se ha eliminado el contacto requerido")
    else:
      print("este contacto no existe en la agenda") 
  elif opcion == 3:
    print("AGENDA DE CONTACTOS")
    for clave, valor in agenda.items():
      print(f"Nombre: {clave}, Telefono: {valor}")
  elif opcion == 4:    
    print("GRACIAS POR UTULIZAR SU AGENDA DE CONTACTOS")
    break # para romper el ciclo y salir
  else:
    print("Opcion incorrecta")
```

-> Lo podes ver en [**ejercicio11.py**](https://github.com/eugenia1984/UTN-FRSR-Programacion-1year-2semester/blob/main/laboratorio2/clase4_5_6_7/ejercicio11.py)

---

## Desempaquetado de listas

```Python
def show(name, lastName):
  print(name + " " + lastName)

person = ["Maria Eugenia", "Costa"]
show(person[0], person[1]) # pasamos uno por uno los datos de la lista a la función

#otro modo de hacerlo
show(*person) # esto es lo mismo que lo anterior pero lo pasamos todo junto

person2 = ("Maria Eugenia", "Costa") # desempaquetamos a través de tupla
show(*person2)

persona3 = {"lastName": "Costa", "name": "Maria Eugenia"}
```


-> Lo podes ver en [**funciones**](https://github.com/eugenia1984/UTN-FRSR-Programacion-1year-2semester/blob/main/laboratorio2/clase4_5_6_7/funciones)

---

## Repaso del ciclo FOR ELSE

```Python
numbers = [1, 2, 3, 4, 5]
for n in numbers:
  print(n)
else:
  print("Esto se termina")
```

-> Siempre al final se va a ver el *Esto se termina*, s emuestr ael else.


```Python
numbers = [1, 2, 3, 4, 5]
for n in numbers:
  print(n)
  if n == 3:
    break # Esta es la unica manera para que no se ejecute el else
else:
  print("Esto se termina")
```

---

## Lista de comprension

Tomar solo lo necesario de la lista, sin modificarla.

```Python
names= ["Paolo", "Rodrigo", "Lupe", "Pepe"]
alongP = [p for p in names if p[0] == "p"] # recorro todos los nombres de la lista
print(alongP)

# con un diccionario
bottleC = [{"name": "Quilmes", "country": "Arg"},
            {"name": "Corona", "country": "Mx"}
          ]
Arg = [b for b in bottleC if b["country"] == "Arg"] # recorro todos los nombres de la lista
print(Arg)
print(bottleC)
```

---

## Funciones * Paso de argumentos

```Python
def mi_funcion2(name, lastName): # le paso parametros
  print(f"Hola {name} {lastName}")

mi_funcion2("Euge", "Costa") # invoco la funcion con los argumentos
```

**parametro** -> trabaja con una variable dentro de la función.

**argumento** -> el valor que le paso a la fumción, es el valor que recibe el parametro.

Puedo llamar varias veces a la misma función, con diferentes argumentos.

-> Lo podes ver en [**funciones**](https://github.com/eugenia1984/UTN-FRSR-Programacion-1year-2semester/blob/main/laboratorio2/clase4_5_6_7/funciones)

---

## Funciones con return

```Python
def sumar(a, b):
  return a+b

resultado = sumar(2,3)
print(f"El resultado de la suma de 2 + 3 es: {resultado}")
```

-> Lo podes ver en [**funciones**](https://github.com/eugenia1984/UTN-FRSR-Programacion-1year-2semester/blob/main/laboratorio2/clase4_5_6_7/funciones)

---

## Valores por default en funciones

```Python
def sumar2(a=0, b=0):
  return a+b

resultado = sumar2()
print(f"Resultado de la suma: {resultado}") # da 0

resultado = sumar2(print(f"Resultado de la suma: {sumar2(1,1)}")) # da 2
```

---

## Argumentos, variables en funciones

```Python
def listarNombres(*nombres):
  for nombre in nombres:
    print(nombre)

listarNombres(["Maria", "Analia", "Carlos"])    
```

---

## Tarea

Crear una funcion para sumar los valores recibidos de tipo numericos, utilizando argumentos variables *args como parametro de la funcion y agregar como resultado la suma de todos los valores pasados como argumentos

```Python
# Defino la funcion
def sumar_valor(*args): #recibimos una cantidad de parametros indefinidos
  resultado = 0
  for valor in args: # iteramos los elementos
    rasultado += valor
  return resultado

print(sumar_valor(3, 5, 9)) # Invocamos a la funcion
```

---

## Trabajo practico integrador: 

Elegir del grupo a un integrante para que yo, como profesor, lo ingrese al repositorio en Git Hub, deben pasarme el correo y nombre de usuario, luego de recibir al invitación por correo, deben ingresar a Git Hub y clonar la carpeta de TecnicaturaGit, luego este integrante debe habilitar a los demás integrantes del grupo para que puedan clonar también. De esta manera van a poder tener acceso a todo lo que  he ingresado en esta carpeta, desde python, java, javascript y node.js

---

## Clase 27/9

### Ejercicio con funciones con *args para multiplicar

Consigna:

- Crear una funcion para multiplicar los valores recibidos de tipo numerico, utilizando argumentos variables *args como parametro de la funcion y regresar como resultado la multiplicacion de todos los valores pasados como argumentos

-> Lo podes ver en [**funciones**](https://github.com/eugenia1984/UTN-FRSR-Programacion-1year-2semester/blob/main/laboratorio2/clase4_5_6_7/funciones/funciones.py)

```Python
# Definimos la funcion
def multiplicar_valores(*numeros): # es mas utilizado *args
  resultado = 1 # el 0 no nos ayuda a multiplicar
  for numero in numeros:
    resultado *= numero
  return resultado

# invocamos a la funcion
print(multiplicar_valores(3,5,15)) # le pasamos argumentos
```

---

## :star: Diccionarios

##  Argumentos variables para un diccionario

```Python
# Defino la funcion para que maneje una lista de terminos
def listarTerminos(**kwargs): # **kwargs es como se suele utilizar en documentacion para recibir los argumentos
  for llave, valor in kwargs.items():
    print(f"¨{llave}: {valor}")

listarTerminos() # como no le paso argumentos la funcion no se ejecuta

listarTerminos(IDE="Integrated Development Enviroment") # ¨IDE: Integrated Development Enviroment
```

```Python
listarTerminos(IDE="Integrated Development Enviroment", PK="Primary Key") 
# ¨IDE: Integrated Development Enviroment
# ¨PK: Primary Key
```
Voy a tener dos pares key - value

-> Las llaves no llevas comillas. Deben ser STRING pero sin las comillas, NO puedo usar numeros.

-> **kwargs = key word argument

-> Si tenemos que pasar más de un parámetro, se pasan de forma independiente. Por ejemplo:

```def listarTerminos(nombre, *nombres, **kwargs):```

nombre -> es un **Argumento fijo**

*nombre -> es de tipo **tupla**

```**kwargs``` -> es de tipo **diccionario**

-> Lo podes ver en [**ejercicio12.py**](https://github.com/eugenia1984/UTN-FRSR-Programacion-1year-2semester/blob/main/laboratorio2/clase4_5_6_7/ejercicio122.py)

---

##  Lista de elementos con funciones (convertir)

Vemos distintos tipos de datos como argumentos.

```Python
# Usamos una lista para recibir elementos
def desplegarNombres(nombres):
  for nombre in nombres:
    print(nombre)

nombres2 = ["Euge", "Agus", "Andi"]
desplegarNombres(nombres2)
# Euge
# Agus
# Andi
```

-> Si le paso como argumento un String me va a separar en caracteres:
```Python
desplegarNombres("Carla")
# C
# a
# r
# l
# a
```

-> Si le paso como argumento un numero entero va a dar un error, y va a avisar que no es un objeto iterable
```Python
# desplegarNombres(10)
```

Pero... si usamos los **()** lo convertimos en tupla que SI es iterable

```Python
desplegarNombres((10, 11))
# 10
# 11
```

Si tenemos un solo numero, para que sea tupla recordar usar la **,**:
```Python
desplegarNombres((2, ))
```

Tambien... podemos convertirlo a una lista para que pueda ser iterable.

```Python
desplegarNombres([10, 11])
# 10 el primer elemento de la lista, un entero
# 11 el segundo elemento de la lista, un entero
```

-> Lo podes ver en [**ejercicio12.py**](https://github.com/eugenia1984/UTN-FRSR-Programacion-1year-2semester/blob/main/laboratorio2/clase4_5_6_7/ejercicio12.py)

---

##  Funciones recursivas con factorial 

Una **funcion recursiva** se manda a llamar a si misma para completar una tarea.

Necesita:

- un caso base

- un caso recursivo

```Python
def factorial(numero): # se envia cmo argumento y se recibe como parametro
  if numero == 1: # caso base
    return 1
  else:
    return numero * factorial(numero-1) # caso recursivo

resultado = factorial(5)
print(f"El factorial de 5 es:  {resultado}")
```

### Tarea

Hacer que el numero a calcular el cactorial se ingrese por teclado:

```Python
factorialACalcular = int(input("Ingrese un numero para calcular su factorial: "))
print(f"El factorail de {factorialACalcular} es {factorial(factorialACalcular)}")
```

-> Lo podes ver en [**funciones3.py**](https://github.com/eugenia1984/UTN-FRSR-Programacion-1year-2semester/blob/main/laboratorio2/clase4_5_6_7/funciones/funciones3.py)

---

## Ejercicio 4 con funciones (impuestos)

Crear una funcion para calcular el total de un pago incluyendo un impuesto aplicado. (IVA)

Formula: pago_total = pago_Sin_impuesto + pago_sin_impuesto * (impuesto/100)

Proporcionar el pago_sin_impuesto de 1000

Proporcionar el monto del impuesto del 21%

Pago con impuesto: XXX

```Python
def calcular_total_pago(pago_sin_impuesto, impuesto):
  if impuesto <= 0:
    return("El impuesto debe ser mayor a 0")
  else:
    pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto/100)
    return pago_total

# Ejecuto la funcion pidiendole los datos al usuario
pago_sin_impuesto = float(input("Ingrese el pago sin impuestos: "))
impuesto = float(input("Ingrese el monto dle impuesto a aplicar: "))
pago_con_impuesto = calcular_total_pago(pago_sin_impuesto, impuesto)
print(f"El pago total es: {pago_con_impuesto}")
```

-> Lo podes ver en [**funciones4.py**](https://github.com/eugenia1984/UTN-FRSR-Programacion-1year-2semester/blob/main/laboratorio2/clase4_5_6_7/funciones/funciones4.py)

---

##  Ejercicio 5 Funciones (Celsius a Fahrenheit)

Realizar dos funciones para convertir de grados celsius a fahrenheit y viceversa

```Python

# Funcion que convierte de celsius a fahrenheit
def celsius_fahrenheit(celsius):
  conversion = celsius * 9/5 + 32
  return conversion

# Funcion que convierte de fahrenheit a celcius
def fahrenheit_celsius(fahrenheit):
  conversion = (fahrenheit - 32 ) * 5/9
  return conversion

celsius = float(input("Ingrese un valor de celsius: "))  
resultado = celsius_fahrenheit(celsius)
print(f"Los {celsius} Celsius pasados a Fahrenheit son: {resultado}")

fahrenheit = float(input("Ingrese un valor de fahrenheit: ")) 
resultado = fahrenheit_celsius(fahrenheit)
print(f"Los {fahrenheit} Fahrenheit pasados a Celsius son : {resultado}") 
```

-> Lo podes ver en [**funciones5.py**](https://github.com/eugenia1984/UTN-FRSR-Programacion-1year-2semester/blob/main/laboratorio2/clase4_5_6_7/funciones/funciones5.py)

---
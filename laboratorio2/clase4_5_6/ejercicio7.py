# Ejercicio 7:
# Realizar un juego para adividar un numero.
# Para ello se debe generar un número aleatorio entre 1 - 100 y 
# luego ir pidiendo números indicando "es mayor" o "es menor" según sea mayor o menor con respecto a N.
# El proceso termina cuando el usuario acierta 
# y alli se debe mostrar el número de intentos.
import random # para utilizar la libreria y tener el numero random
print("\t.: Juego Adivina el número :.")

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
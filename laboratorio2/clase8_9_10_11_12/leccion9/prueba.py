from Cuadrado import Cuadrado
from Rectangulo import Rectangulo

print("Creacion de objeto clase Cuadrado".center(50, "_"))
cuadrado1 = Cuadrado(5, "Azul")
print(f"El ancho dle cuadrado es: {cuadrado1.ancho}")
print(f"El alto del cuadrado es: {cuadrado1.ancho}")
print(f"El area es: {cuadrado1.calcular_area()}")

# MRO = Method R3solution Order 
print(Cuadrado.mro()) 

print(f"cuadrado1: {cuadrado1}")

# instancio un objeto Rectangulo
print("Creacion de objeto clase Rectangulo".center(50, "_"))
rectangulo1 = Rectangulo(3, 8, "verde")
print(f"El area es: {rectangulo1.calcular_area()}")
print(rectangulo1)
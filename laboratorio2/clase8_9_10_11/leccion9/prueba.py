from Cuadrado import Cuadrado

cuadrado1 = Cuadrado(5, "Azul")
print(f"El ancho dle cuadrado es: {cuadrado1.ancho}")
print(f"El alto del cuadrado es: {cuadrado1.ancho}")
print(f"El area es: {cuadrado1.calcular_area()}")

# MRO 
print(Cuadrado.mro()) 
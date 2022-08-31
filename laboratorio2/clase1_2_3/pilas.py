# Pila# LIFO Last In First out
# Como una pila de ropa el ultimo que pusimos arriba es el que sale
# Como una pila de platos
pila = [1, 2, 3]
pila.append(4) # cada elemento que agrego se ubica al final
pila.append(5)
print(pila) # {1, 2, 3, 4, 5}
pila.pop() # casa el ultimo elemento y retorna
print(pila) # {1, 2, 3, 4}
elementoBorrado = pila.pop() # va a casar el 4 y lo guardo en la variable elementoBorrado
print(f"Sacamos el elemento {elementoBorrado} y la pila ahora quedo asi: {pila}")
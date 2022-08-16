# Ejercicio 1 : Iterar un rango e imprimir numeros divisibles entre 3 , para obtener (0, 3, 6, 9)
rango = range(10)
resultado = []

for n in rango: # con el for in range voy a recorrer la lista del 0 al 10
  if n % 3 == 0: # con el if voy a seleccionar solo los divisibles entre 3
    resultado.append(n) # cn el append los guardo en mi lista resultado 

print(resultado) # muestro la lista resultado
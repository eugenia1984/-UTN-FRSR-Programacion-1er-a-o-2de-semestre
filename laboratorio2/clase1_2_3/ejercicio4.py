# Ejercicio 4: dada la siguiente tupla
tupla = (13, 1, 8, 3, 2, 5, 8)
# Crear una lista que solo incluya los numeros menores a 5 e imprima por consola [1, 3, 2]
menores_a_5 = []
for elemento in tupla:
  if elemento < 5:
    menores_a_5.append(elemento)

print(menores_a_5)

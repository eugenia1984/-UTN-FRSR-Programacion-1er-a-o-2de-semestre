def listarNombres(*nombres):
  for nombre in nombres:
    print(nombre)

listarNombres("Analia", "Eugenia", "Carlos")    

#  Argumentos variables para un diccionario

# Defino la funcion para que maneje una lista de terminos
def listarTerminos(**kwargs): # **kwargs es como se suele utilizar en documentacion para recibir los argumentos
  for llave, valor in kwargs.items():
    print(f"¨{llave}: {valor}")

listarTerminos() # como no le paso argumentos la funcion no se ejecuta
listarTerminos(IDE="Integrated Development Enviroment") # ¨IDE: Integrated Development Enviroment
listarTerminos(IDE="Integrated Development Enviroment", PK="Primary Key") 
# ¨IDE: Integrated Development Enviroment
# ¨PK: Primary Key

# Usamos una lista para recibir elementos
def desplegarNombres(nombres):
  for nombre in nombres:
    print(nombre)

nombres2 = ["Euge", "Agus", "Andi"]
desplegarNombres(nombres2)
# Euge
# Agus
# Andi
desplegarNombres("Carla")
# C
# a
# r
# l
# a
# desplegarNombres(10) no podemos pasarle numeros porque da error

# si usamos los () lo convertimos en tupla que SI es iterable
desplegarNombres((10, 11))
# 10
# 11
# si tenemos un solo numero, para que sea tupla recordar usar la ,
desplegarNombres((2, ))

# Si usamos los [] lo convertimos en lista
desplegarNombres([10, 11])
# 10
# 11


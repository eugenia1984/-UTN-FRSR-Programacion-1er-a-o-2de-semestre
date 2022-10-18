# Maria Eugenia Costa
# Ejercicio 11 : Agenda telefonica
# Hacer un programa que simule una agenda de contactos.
# Crear un diciconario donde la clave sea el nombre del 
# usuario y el valor sea el telefono, el programa tendrá el 
# siguiente menú de opciones:

# 1. Nuevo contacto
# 2. Borrar contacto
# 3. Ver contactos existentes
# 4. Salir

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



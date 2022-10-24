# CREACION DE OBJETOS CON ARGUMENTOS
class Persona:
  def __init__(self, nombre, apellido, edad): # variables
    self.nombre = nombre #atributo de metodo
    self.apellido = apellido #atributo de metodo
    self.edad = edad #atributo de metodo
# Al instanciar a un nuevo objeto Persona debo indicarle los argmuemtnos    
persona2 = Persona("Maria Eugenia ", "Costa", 38)
# Accedo a los atributos de mi objeto
print(persona2.nombre) # Maria Eugenia
print(persona2.apellido) # Costa
print(persona2.edad) #38

# Instancio un nuevo objeto
persona3 = Persona("Agustin", "Costa", 34) # recibe los argumentos
print(f"persona3 -> nombre: {persona3.nombre}, apellido: {persona3.apellido} y edad: {persona3.edad}") # persona3 -> nombre: Agustin, apellido: Costa y edad: 34
# Métodos de instancia: Definimos un método
class Persona:
  def __init__(self, nombre, apellido, edad): # variables
    self.nombre = nombre #atributo de metodo
    self.apellido = apellido #atributo de metodo
    self.edad = edad #atributo de metodo

  # Un nuevo metodo de la clase
  def mostrar_detalle(self):
    print(f"Persona: {self.nombre} {self.apellido} {self.edad}")

persona4 = Persona("Analia", "Bruni", 61)
persona4.mostrar_detalle() # la referencia se pasa de forma automatica      

# Palabra reservada self y atributos de instancia
#Persona.mostrar_detalle()

# Crear atributos desde un objeto
persona4.telefono = "1234567890"
print(f"Este es el teelfono de {persona4.nombre} : {persona4.telefono}") # Este es el teelfono de Analia : 1234567890
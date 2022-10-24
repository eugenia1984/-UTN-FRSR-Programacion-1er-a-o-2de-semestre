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
persona4.mostrar_detalle()      
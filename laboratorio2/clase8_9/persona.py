"""
class Persona:  # creamos una clase 
  pass # no se procesa nada mas (no tiene contenido)
"""

class Persona:
  def __init__(self):
    # son los atributos de la persona dentro del metodo constructor de la clase)
    self.nombre = "Maria Eugenia"
    self.apellido = "Costa"
    self.edad = 38

print(type(Persona)) # <class "type">

# instancio un nuevo objeto Persona que ya a tener sus valores definidos por el metodo constructor
persona1 = Persona()
# Veo los atributos de mi nuevo objeto
print(persona1.nombre) # Maria Eugenia
print(persona1.apellido) # Costa
print(persona1.edad) # 38



class Rectangulo:
  """
  Crear una clase llamada Rectangulo, debe tener 2 atributos:
  altura y base
  el nombre del metodo sera calcular_area para utilizar la formula:
  area = base + altura
  La base y la altura deben ser ingresadas por el usuario
  y los objetos deben ser tres
  """
  def __init__(self, altura, base):
    self.altura = altura
    self.base= base
  def calcular_area(self):
    return self.base * self.altura

base = int(input("Ingrese en numeros la base del resctangulo: "))
altura = int(input("Ingrese en numeros la altura del resctangulo: "))
rectangulo = Rectangulo(base, altura)
print(f"El area del rectangulo es {rectangulo.calcular_area()}")
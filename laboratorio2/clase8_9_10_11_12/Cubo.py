class Cubo:
  """
  Crear la clase Cubo con los atributos ancho, alto y profundidad
  con el metodo calcular_volumen que tendra al formula
  volumen = ancho * altura * profundidad
  El usuario debe ingresar los valores
  """
  def __init__ (self, ancho, altura, profundidad):
    self.ancho = ancho
    self.altura = altura
    self.profundidad = profundidad

  def calcular_volumen(self):
    return self.ancho * self.altura * self.profundidad

ancho = int(input("Ingresar el ancho del cubo (en numeros): "))
altura = int(input("Ingresar la altura del cubo (en numeros): "))
profundidad = int(input("Ingresar la profundidad del cubo (en numeros): "))
cubo = Cubo(ancho, altura, profundidad)
print(f"El volumen del cubo es: {cubo.calcular_volumen()}")
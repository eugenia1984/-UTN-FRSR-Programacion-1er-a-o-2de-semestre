# Crear la clase Aritmética: Sumar
class Aritmetica:
  """
  Aca puede ir el DocString
  es decir la documentacion de la clase
  """
  def __init__ (self, operandoA, operandoB):
    self.operandoA = operandoA
    self.operandoB = operandoB
  # Metodo para sumar  
  def sumar(self):
    return self.operandoA + self.operandoB

aritmetica1 = Aritmetica(7,9)
print(aritmetica1.sumar()) # 16
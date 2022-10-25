# Crear la clase Aritmética: Sumar, REstar, Multiplicar y Dividir
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
  # Metodo para restar
  def restar(self):
    return self.operandoA - self.operandoB
  # Metodo para multiplicar
  def multiplicar(self):
    return self.operandoA * self.operandoB 
  # Metodo para dividir 
  def dividir(self):
    if self.operandoB == 0:
      return "Error no se puede dividir por cero"
    else:
      return self.operandoA / self.operandoB

aritmetica1 = Aritmetica(7,9)
print(f"La suma de 7 y 9 es: {aritmetica1.sumar()}") # 16
print(f"La resta de 7 y 9 es: {aritmetica1.restar()}") # -2
print(f"La multiplicacion de 7 y 9 es: {aritmetica1.multiplicar()}") #  63
print(f"La division de 7 y 9 es: {aritmetica1.dividir()}") #  0.7777777777777778



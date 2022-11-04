class Vehiculo:
  def __init__(self, color, ruedas):
    self.color = color
    self.ruedas = ruedas
  def __str__(self):
    return f"Color: {self.color}, ruedas: {self.ruedas}"

class Auto(Vehiculo):
  def __init__(self, color, ruedas, velocidad):
    super().__init__(color, ruedas)
    self.velocidad = velocidad
  def __str__(self):
    return f"{super().__str__()} velocidad(km/h): {self.velocidad}" 

class Bicicleta(Vehiculo):
  def __init__(self, color, ruedas, tipo):
    super().__init__(color, ruedas)
    self.tipo = tipo
  def __str__(self):
    return f"{super().__str__()} tipo: {self.tipo}"

# Instancio un objeto de la clase Vehiculo
vehiculo1 = Vehiculo("Blanco", 4)
print(vehiculo1)

# Instancio un objeto de la clase Auto
auto1 = Auto("Amarillo", 4, 120)
print(auto1)

# Instancio un objeto de la clase Bicicleta
bicicleta1 = Bicicleta("Roja", 2, "Montaña")
print(bicicleta1)
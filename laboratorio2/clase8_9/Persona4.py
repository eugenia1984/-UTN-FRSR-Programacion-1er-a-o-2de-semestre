# Método init Dunder con argumentos variables
class Persona:
  def __init__(self, nombre, apellido, dni, edad, *args, **kwargs): # variables
    self.__nombre = nombre #Encapsulamiento con doble __
    self.apellido = apellido 
    self._dni = dni # Encapsulamiento
    self.edad = edad 
    self.args = args
    self. kwargs = kwargs

  # Un nuevo metodo de la clase
  def mostrar_detalle(self):
    # Como esta encapculado no uedo tener: {self.__nombre}
    print(f"La clase Persona tiene los siguientes datos: {self.apellido} {self.edad}, el dni es {self._dni} la direccion es {self.args}, los datos importantes son: {self.kwargs}")

persona = Persona("Rogelio", "Romero", 12345678, 22, "telefono", "1234567891", "Calle Lopez", 823, "Manzana", 77, "Casa", 18, Altura=1.83, Peso=105, CFavorito="Azul", Auto="Citroen", Modelo=2021)   # puedo instanciarla con el nombre 
# como el atributo nombre esta encapsulado no voy  apoder modificarlo con persona.__nombre = ""
persona.mostrar_detalle() # Pero NO vere el nombre -> La clase Persona tiene los siguientes datos: Romero 22, el dni es 12345678 la direccion es ('telefono', '1234567891', 'Calle Lopez', 823, 'Manzana', 77, 'Casa', 18), los datos importantes son: {'Altura': 1.83, 'Peso': 105, 'CFavorito': 'Azul', 'Auto': 'Citroen', 'Modelo': 2021}

# print(persona._dni) esto no se debe utilizar, esto dice que lo desconocemos

# persona.__nombre no se puede hacer, porque esta totalmente encapsulado
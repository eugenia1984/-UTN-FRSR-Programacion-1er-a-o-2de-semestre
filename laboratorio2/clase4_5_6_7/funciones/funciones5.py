# Realizar dos funciones para convertir de grados celsius a fahrenheit y viceversa

# Funcion que convierte de celsius a fahrenheit
def celsius_fahrenheit(celsius):
  conversion = celsius * 9/5 + 32
  return conversion

# Funcion que convierte de fahrenheit a celcius
def fahrenheit_celsius(fahrenheit):
  conversion = (fahrenheit - 32 ) * 5/9
  return conversion

celsius = float(input("Ingrese un valor de celsius: "))  
resultado = celsius_fahrenheit(celsius)
print(f"Los {celsius} Celsius pasados a Fahrenheit son: {resultado}")

fahrenheit = float(input("Ingrese un valor de fahrenheit: ")) 
resultado = fahrenheit_celsius(fahrenheit)
print(f"Los {fahrenheit} Fahrenheit pasados a Celsius son : {resultado}") 
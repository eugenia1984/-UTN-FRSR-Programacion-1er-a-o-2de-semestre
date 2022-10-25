from Persona2 import Persona2 #importo para poder utilizarlo 
# si quiero importar todo -> from Perros import *

print("Creacion de objetos".center(50, "-"))  

if __name__ == "__main__":
  persona_nueva = Persona2("Analia", "Bruni", 62) # instancio un objeto persona y le paso los argumentos
  persona_nueva.mostrar_detalle()

  print(__name__) # Comprobación del módulo principal en ejecución

print("Eliminacion de objetos".center(50, "-"))  
# del persona_nueva
#Esto no se utiliza ya que Python iene el Garbage Colector, no es necesario destruir el objeto
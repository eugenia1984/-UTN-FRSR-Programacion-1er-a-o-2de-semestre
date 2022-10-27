## Diagrama UML (UNIFIED MODELING LANGUAGE / LENGUAJE UNIFICADO DE MODELADO)

- Utilizamos la extension **UMLet** en el VSC. Asi podemos ver los archivos con extension **.uxf**

- Sino en el navegador [www.umletino.com](www.umletino.com) tambien nos permite crear UML, ya que está basado en UMLet -> [umlet.com](umplet.com) con un video tutorial de como aramr los diagramas, ya sea el UML o los de flujo. Desde **download** se puede descargar y usarlo desde la computadora.

---

### Ejemplo de UML:

```

 | -------------------|
 |     Persona        |
 |--------------------|
 | -nombre:str        |
 | -apelliod:str      |
 | -edad:int          |
 |--------------------|
 | mostrar_detalle    |
 |--------------------|
         ^
         |
         | << extends >>
         |
  |----------------------|
  |      persona1        |
  |----------------------|
  | nombre: str="Andres" | 
  | apellido:str="Costa" |
  | edad:int=30          |
  |----------------------|      

```

---

## :star: Clase 11

- Vemos un UML creandolo en el VSC con la extension **UMLet**.

Asi la clase hija va a extender/heredar (**extends**) de la clase padre los mismos atributos y metodos.

Como aca estamos en Pyhon, solo se pone el nombre del atributo, no es necesario ocmo el UML de Java que ponemos el tipo de dato que va a guardar.

- Vamos a tener la clase **Persona** con los atributos : **nombre** y **edad**. Y la clase **Empleado** que va a heredar de persona y ademas va a tener su propio atributo **sueldo**.

-> Esta dentro de la carpeta [**poo**](https://github.com/eugenia1984/UTN-FRSR-Programacion-1year-2semester/blob/main/laboratorio2/clase8_9_10_11/poo/Persona.py)


```Python
class Persona:
  def __init__(self, nombre, edad):
    self.nombre = nombre
    self.edad = edad

class Empleado(Persona): # extiende de la clase Persona
  def __init__ (self, nombre, edad, sueldo):
    super().__init__(nombre, edad)
    self.sueldo = sueldo

# Instancio un objeto empleado
empleado1 = Empleado("Ana", 40, 110000)  
print(empleado1) 
print(f"nombre: {empleado1.nombre}")  
print(f"edad: {empleado1.edad}")
print(f"sueldo: {empleado1.sueldo}")
```

### Tarea

Encapsular los atributos y agregar los metodos getters y setters.

Crear otro objeto, pasar los datos para nombre, edad y sueldo.

Mostrar estos datos, luego modificar nuevamente.

-> Realizada en [**poo/Persona2.py**](https://github.com/eugenia1984/UTN-FRSR-Programacion-1year-2semester/blob/main/laboratorio2/clase8_9_10_11/poo/Persona2.py)

```Pythono
class Persona:
  def __init__(self, nombre, edad):
    self._nombre = nombre
    self._edad = edad
  # getters
  @property
  def nombre(self):
    return self._nombre  
  @property
  def edad(self):
    return self._edad
  # setters
  def nombre(self, nombre):
    self._nombre = nombre
  def edad(self, edad):
    self._edad = edad

class Empleado(Persona): # extiende de la clase Persona
  def __init__ (self, nombre, edad, sueldo):
    super().__init__(nombre, edad)
    self._sueldo = sueldo
    # getter
    @property
    def sueldo(self):
      return self._sueldo
    # setter
    def sueldo(self, sueldo):
      self._sueldo = sueldo

# Instancio un objeto empleado
empleado1 = Empleado("Ana", 40, 110000)  
print(empleado1) 
print(f"nombre: {empleado1._nombre}")  
print(f"edad: {empleado1._edad}")
print(f"sueldo: {empleado1._sueldo}")
````

---

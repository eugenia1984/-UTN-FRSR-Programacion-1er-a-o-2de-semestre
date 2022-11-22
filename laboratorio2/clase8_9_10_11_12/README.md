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

-> Esta dentro de la carpeta [**poo**](https://github.com/eugenia1984/UTN-FRSR-Programacion-1year-2semester/blob/main/laboratorio2/clase8_9_10_11_12/poo/Persona.py)


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

-> Realizada en [**poo/Persona2.py**](https://github.com/eugenia1984/UTN-FRSR-Programacion-1year-2semester/blob/main/laboratorio2/clase8_9_10_11_12/poo/Persona2.py)

```Python
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
```

---

### Metodo dunder __str__()

Dentro de **poo** creamos **ClientPersona.py**.

Vamos a importar: ``` from Persona import *```

Es como el **toString** de Java, para que en vez de mostrar el espacio en memoria me muestre las propiedades del objeto.

Entonces volvemos a Persona2.py y hacemos los cambios:

```Python
def __str__(self):
  return (f"Persona: {self._nombre} {self._edad}")
```

Y en la clase Empleado:

```Python
def __Str__(self):
  return f"Empleado: sueldo {self._sueldo} {super().__str__()}"
```


---

### Ejercicio : uso de herencia

Definir una clase padre llamada Vehiculo y dos clases hijas llamas Auto y Bicicleta, las cuales heredan de la clase padre Vehiculo.

La clase padre debe tener los siguientes atributos y metodos:

- Vehiculo (clase padre)

-Atributos (color, ruedas)

-Metodos (_ _init_ _(color, ruedas) y _ _str_ _())

- Auto(clase hija de Vehiculo)

-Atributos (velocidad(km/h))

-Metodos (_ _init_ _(color, ruedas, velocidad) y _ _str_ _()) 

- Bicicleta(clase hija de Vehiculo)

-Atributos(tipo(urbana, montaña, etc))

-Metodos(__init__(color, ruedas, tipo) y __str__())

-> crear un objeto de cada clase

-> armar el diagrama UML

-> Lo resuelvo todo dentro de [**herencia**](https://github.com/eugenia1984/UTN-FRSR-Programacion-1year-2semester/tree/main/laboratorio2/clase8_9_10_11_12/herencia)

```Python
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
```

---

## :star: Clase 12 Herencia multiple

En Python tenemos **herencia ultiple**

---

-> Realizamos el diagrama UML:

```
----------------------    -----------------
<<FiguraGeometrica>>        <<Color>>
--------------------     ------------------
+alto                    +color
+ancho
---------------------    -----------------
       \                     / 
         \                 /
           \             /
         --------------------
            << Cuadrado>>
         -------------------
         +area()
         --------------------   
```

-> Creamos las clases el [leccion9](https://github.com/eugenia1984/UTN-FRSR-Programacion-1year-2semester/tree/main/laboratorio2/clase8_9_10_11_12/leccion9), con los archivos:

**FiguraGeometrica.py**:
```Python
class FiguraGeometrica:
  def __init__(self, ancho, alto):
    self.ancho = ancho
    self.alto = alto
```    

**Cuadrado.py**:
```Python
from FiguraGeometrica import FiguraGeometrica
from Color import Color

class Cuadrado(FiguraGeometrica, Color):
  def __init__(self, lado, color):
    # super.__init__(lado)
    FiguraGeometrica.__init__(self, lado, lado)
    Color.__init__(self, color)

  def calcular_area(self):
    return self.alto * self.ancho
```

**Color.py**:
```Python
class Color:
  def __init__(self, color):
    self.color = color
```

**prueba.py**:
```Python
from Cuadrado import Cuadrado

cuadrado1 = Cuadrado(5, "Azul")
print(f"El ancho dle cuadrado es: {cuadrado1.ancho}")
print(f"El alto del cuadrado es: {cuadrado1.ancho}")
print(f"El area es: {cuadrado1.calcular_area()}")

# MRO 
print(Cuadrado.mro()) 
```


---

### MRO Method Resolution Order

-> Nos permite conocer la gerarquia de las clases frente a la clase actual que estamos utilizando.

```Python
print(Cuadrado.mro())
```

---

-> Agregamos a nuestro UML la nueva clase Resctangulo

-> Agregamos los getters, setters y _ _str_ _ a todas als clases padres y a las hijas (Cuadrado y Rectangulo solo el _ _str_ _)

---

### Modificamos el ejercico de leccion9

-> Encapsulamos a FiguraGeometrica.py agregando los **guiones bajos**.

-> Agregamos los **getters** y **setters**.

Quedandonos:

**FiguraGeometrica.py**:
```Python
class FiguraGeometrica:
  def __init__(self, ancho, alto):
    self._ancho = ancho
    self._alto = alto

  @property
  def ancho(self):
    return self._ancho

  @ancho.setter
  def ancho(self, ancho):
    self._ancho = ancho

  @property
  def alto(self):
    return self._alto

  @alto.setter
  def alto(self, alto):
    self._alto = alto

  def __str__(self):
    return f"FiguraGEometrica: ancho: {self._ancho} - alto: {self._alto}"
```

**Color.py**:
```Python
class Color:
  def __init__(self, color):
    self.color = color

  @property
  def color(self):
    return self._color

  @color.setter
  def color(self, color):
    self._color = color

  def __str__(self):
    return f"Color: color : {self._color}"   
```

En **Cuadrado.py** agrego el metodo _ _ str_ _

```Python
from FiguraGeometrica import FiguraGeometrica
from Color import Color

class Cuadrado(FiguraGeometrica, Color):
  def __init__(self, lado, color):
    # super.__init__(lado)
    FiguraGeometrica.__init__(self, lado, lado)
    Color.__init__(self, color)

  def calcular_area(self):
    return self.alto * self.ancho

  def __str__(self):
    return f"{FiguraGeometrica.__str__(self)} {Color.__str__(self)}"  
```

Ahora hago las pruebas en **prueba.py**

-> Y creamos la clase **Rectangulo.py**

```Python
from Color import Color
from FiguraGeometrica import FiguraGeometrica

class Rectangulo(FiguraGeometrica, Color):
  def __init__(self, ancho, alto, color):
    FiguraGeometrica.__init__(self, ancho, alto)
    Color.__init__(self, color)

  def calcular_area(self):
    return self.alto * self.ancho

  def __str__(self):
    return f"{FiguraGeometrica.__str__(self) {Color.__str__(self)}}"
```

---
---

## :star:  Clase 13 Abstract y Static


### Validaciones en atributos

Simplemente le agrego el print.

```Python
# instancio un objeto Rectangulo
print("Creacion de objeto clase Rectangulo".center(50, "_"))
rectangulo1 = Rectangulo(3, 8, "verde")
print(f"El area es: {rectangulo1.calcular_area()}")
print(rectangulo1)
```

Y en la clase **FiguraGeometrica** hizo una "validación" que nos ata a que estén entre ene rango de (0-10). 

Mucho mejor es hacer la validación para que sean números positivos, no atarnos a un rango. 

```Python
class FiguraGeometrica:
  def __init__(self, ancho, alto):
    if 0 < ancho < 10:
      self._ancho = ancho
    if 0 < alto < 10:  
      self._alto = alto
```

Después le agregó un else, peor igual seguimos atados a ese rango, mucho mejor validar que sean numero sy que sean positivos, sin atarlo a un rango.

```Python
class FiguraGeometrica:
  def __init__(self, ancho, alto):
    if 0 < ancho < 10:
      self._ancho = ancho
    else:
      self._ancho = 0
    if 0 < alto < 10:  
      self._alto = alto
    else:
      self._alto = 0
```

###  Método encapsulado y setter

Como no tengo todo encapsulado puedo alterar los valores, por ejemplo:

```Python
# instancio un objeto Rectangulo
print("Creacion de objeto clase Rectangulo".center(50, "_"))
rectangulo1 = Rectangulo(3, 8, "verde")
rectangulo1.ancho = 15 # hacemos la reasignacion porque no esta encapsulado
print(f"El area es: {rectangulo1.calcular_area()}")
print(rectangulo1)
```

-> En **FiguraGeometricas** creo el método **_validar_valores** como tiene el _ está encapsulado, solo se puede usar dentro de esa clase.

```Python
  def _validar_valores(self, valor):
    return True if 0 < valor < 10 else False
```

Y sigue insisitiendo en validar que este entre 0 a 10, en vez de que sea numero positivo.


Entonces puedo modificar aca:

```Python
class FiguraGeometrica:
  def __init__(self, ancho, alto):
    if 0 < ancho < 10:
      self._ancho = ancho
    else:
      self._ancho = 0
    if 0 < alto < 10:  
      self._alto = alto
    else:
      self._alto = 0
```

Para usar el nuevo método:

```Python
  def __init__(self, ancho, alto):
    if self._validar_valores(ancho):
      self._ancho = ancho
    else:
      self._ancho = 0
      print(f"Valor erroneo para el ancho: {ancho}")
    if self._validar_valores(alto):  
      self._alto = alto
    else:
      self._alto = 0
      print(f"Valor erroneo para el alto: {alto}")
```

Estas validaciones tambien se pueden utilizar en el método **setter**:

```Python
@ancho.setter
def ancho(self, ancho):
  if self._validar_valores(ancho):
    self._ancho = ancho
```

```Python
@alto.setter
def alto(self, alto):
  if self._validar_valores(alto):
    self._alto = alto
```

###  Explicación de validaciones setter

### Clases abstractas: Diagrama de clases UML, teoría y practica
### Atributo Read-only y método mro

###  Diagrama de clases UML con variables de clase: Teoría en carpeta Lección10

###  Variables de clase: Practica en carpeta Lección10 

---
---

##:star: Clase 14  Diseño, Constante y contexto estáticoLección

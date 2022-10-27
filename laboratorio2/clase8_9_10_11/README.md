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

---
# :star: Clase 11 * TABLAS RELACIONALES

---

##  <img src="https://img.icons8.com/external-flaticons-lineal-color-flat-icons/40/null/external-table-mobile-app-development-flaticons-lineal-color-flat-icons-4.png"/> ELEMENTO FUNDAMENTAL DE UNA BASE DE DATOS RELACIONAL

El elemento fundamental del método racional de una base de datos, es una tabla relacional.

### TABLA:

![image](https://user-images.githubusercontent.com/72580574/202468069-5db92571-b36d-4319-9e6e-ff7f4a3ec88c.png)

• VA A SER EL ESPAPCIO DODNE VOY A ORGANIZAR LA INFORMACIÓN DENTRO DE MI BASE DE DATOS.

• VA A CONTENER COLUMNA Y FILAS

---

### <img src="https://img.icons8.com/external-flaticons-lineal-color-flat-icons/40/null/external-table-mobile-app-development-flaticons-lineal-color-flat-icons-4.png"/>  TABLA RELACIONAL

![image](https://user-images.githubusercontent.com/72580574/202468242-2fa3c996-b342-4342-a37b-127c5929b3c4.png)

Es una representación extencional de una relación definida sobre un cierto dominio, decodificado o dividido en varias tablas.


### <img src="https://img.icons8.com/external-flaticons-lineal-color-flat-icons/40/null/external-table-mobile-app-development-flaticons-lineal-color-flat-icons-4.png"/>   Entidad

![image](https://user-images.githubusercontent.com/72580574/202468330-e5befc43-f5a0-4bea-836d-8ba75718ff75.png)

Una entidad es la representación de un objeto o concepto del mundo real que se describe en una base de datos. Son datos referentes.

Ejemplos de nombres de entidades: Alumno, Empleado, Artículo, Noticia, etc.

Las entidades se describen en la estructura de la base de datos empleando un modelo de datos.

![image](https://user-images.githubusercontent.com/72580574/202468413-33c489d3-e9c9-4808-8011-aeae90f5dff4.png)

Cada entidad está constituida por uno o más atributos.
---

### <img src="https://img.icons8.com/external-flaticons-lineal-color-flat-icons/40/null/external-table-mobile-app-development-flaticons-lineal-color-flat-icons-4.png"/> Atributos

•Un atributo representa una propiedad de interés de una entidad.

•Los atributos se describen en la estructura de la base de datos empleando un modelo de datos.

Atributos representados de forma gráfica

![image](https://user-images.githubusercontent.com/72580574/202468537-587db916-ec8a-455a-aaff-384c6bfee0ed.png)

Atributos representados en Tablas

![image](https://user-images.githubusercontent.com/72580574/202468577-c6d048af-226a-4eb9-a471-f2d82f29b7a1.png)


---

### TUPLAS:( filas)

![image](https://user-images.githubusercontent.com/72580574/202468635-1b543341-ec40-447e-817b-82e95f54fde5.png)

Se la define como una función que asocia univocamente los nombre de los atributos de una relación con los valores de la misma.

Es una fila de una tabla realciona

### Clave Primaria:

![image](https://user-images.githubusercontent.com/72580574/202468700-3ee18dc2-5d41-49d2-9be3-ce19cb4d359a.png)

•Cada entidad tiene una clave primaria , campo llave o llave que identifica de forma única el conjunto de datos.

•La llave primaria es un dato, el cual es único y no se repite de lo que vendría siendo una tabla ouna entidad.

• Me va permitir relacionar datos.

### Clave Foránea:

![image](https://user-images.githubusercontent.com/72580574/202468770-8050f343-c616-4ca6-8e72-d409029e0f30.png)

•Es cuando en una entidad figura la clave primaria de otra entidad , esta se denomina clave foranea o clave ajena.
•Las entidades se realcionan entre si por medio de las claves foraneas

Metadatos:

•Son Datos sobre los datos  presentes en la Base de Datos.

•Hace referencia al tipo de Dato que vamos a almacenar ( texto, nuemro, fechas, etc.)

•También el nombre que va a recibir cada dato (nombre, apellido, fecha, edad, etc.)


---

### Operadores Lógicos:

• Los operadores lógicos nos van a permitir definir sentencias así como también  llamar datos.

![image](https://user-images.githubusercontent.com/72580574/202468858-81f2a6dc-0413-4eb8-9c00-7961c28f17b0.png)

### Función que realiza el operador:

Una función de operador se centra en uno y tres argumentos y devuelve un valor.

Cuando una sentencia SQL contiene un operador, el Servido de bases de Datos, invoca automáticamente la función del operador asociado.

---

### OPERACIONES FUNDAMENTALES.

1. **SELECCIÓN**

•Me va atraer todos los datos de la tabla en general.
•Se va a ocupar de seleccionar filas
   

En la ventana de comandos nos arrojada los datos de la tabla ya sean generales o solo los que seleccionemos.

```SQL
SELECT * FROM (nombre de tabla);
```
O 
```SQL
SELECT NOMBRE, EDAD FROM (NOMBRE DE TABLA)
````

*FROM, nos arrojará todos los datos de la tabla

![image](https://user-images.githubusercontent.com/72580574/202469296-1ce5ed27-2242-4890-bf97-7c12526cf6f9.png)

Si especificamos los datos, solo nos arrojará los solicitados.

![image](https://user-images.githubusercontent.com/72580574/202469336-481d8394-d1d5-47b8-9070-7ff0ebb4a1a7.png)



2. **PROYECCION**

• Esta operación nos ayuda a seleccionar datos específicos.

• Sólo traerá el campo específico que se le indique.

• Se va  a ocupar de seleccionar columnas 

```DQL
SELECT nombre FROM estudiantes where Nombres ='nombre';
```
ó

```SQL
SELECT nombre, edad FROM estudiantes where Nombres='nombre';
```

![image](https://user-images.githubusercontent.com/72580574/202469465-04e0bcdf-ec4a-4074-99ab-57326681c67d.png)

![image](https://user-images.githubusercontent.com/72580574/202469486-fa698f50-0957-4417-893c-6a0007b748a0.png)


###  Como ingresamos datos en nuestras tablas:

![image](https://user-images.githubusercontent.com/72580574/202469527-7c4f88cf-4cb0-40d2-ba8a-784464fa8155.png)


![image](https://user-images.githubusercontent.com/72580574/202469554-c7b66a24-5e0f-4b1e-82d9-3aa26feee297.png)

Para que me permita ingresar datos debemos ingresar nuevamente a la configuración de la tabla y seleccionar en la fila id estudiante  en la opción AI (Auto Incrementable) y aplicamos.

![image](https://user-images.githubusercontent.com/72580574/202469594-7dc7702b-6548-4cf2-b5ca-09d749cb6660.png)


---

## :star: ACTIVIDAD

1. Responder cuestionario para la asistencia en el Campus.
  
2. Realizar la siguiente actividad:
 A) ingresar datos en la tabla creada la clase anterior.

B) utilizar los operadores para selección y proyección

---




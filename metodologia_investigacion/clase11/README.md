# :star: Clase 11 

---

## MySQL

### ELEMENTO FUNDAMENTAL DE UNA BASE DE DATOS RELACIONAL

- El elemento fundamental del método racional de una base de datos, es una tabla relacional.

#### TABLA:

![image](https://user-images.githubusercontent.com/72580574/200966727-86227679-64f1-4244-8e38-0d2acb93a0ad.png)

- VA A SER EL ESPAPCIO DODNE VOY A ORGANIZAR LA INFORMACIÓN DENTRO DE MI BASE DE DATOS.

- VA A CONTENER COLUMNA Y FILAS 

#### TABLA RELACIONAL

![image](https://user-images.githubusercontent.com/72580574/200966806-fed1832d-be31-4266-a0d3-e3f709e84646.png)

Es una representación extencional de una relación definida sobre un cierto dominio, decodificado o dividido en varias tablas.

#### Entidad

![image](https://user-images.githubusercontent.com/72580574/200966873-ed78716e-74f0-4335-a09d-de507c0b2d2a.png)


- Una entidad es la representación de un objeto o concepto del mundo real que se describe en una base de datos. Son datos referentes.

- Ejemplos de nombres de entidades: Alumno, Empleado, Artículo, Noticia, etc.

- Las entidades se describen en la estructura de la base de datos empleando un modelo de datos.

![image](https://user-images.githubusercontent.com/72580574/200967018-19bd2fab-eafd-4cee-9132-aad8751dfbc4.png)

- Cada entidad está constituida por uno o más atributos.

#### Atributos

- Un atributo representa una propiedad de interés de una entidad.

- Los atributos se describen en la estructura de la base de datos empleando un modelo de datos.


#### Atributos representados de forma gráfica

![image](https://user-images.githubusercontent.com/72580574/200967081-c9035832-2ea8-4e49-a503-324dbbe6c906.png)

#### TUPLAS:( filas)

![image](https://user-images.githubusercontent.com/72580574/200967118-88032bef-5f8c-4651-8378-2bf2d02224e0.png)


Se la define como una función que asocia univocamente los nombre de los atributos de una relación con los valores de la misma.

Es una fila de una tabla realcional



#### Clave Primaria:

![image](https://user-images.githubusercontent.com/72580574/200967143-615419a6-b5db-4239-9e1d-2a4f9582cf27.png)

• Cada entidad tiene una clave primaria , campo llave o llave que identifica de forma única el conjunto de datos.

• La llave primaria es un dato, el cual es único y no se repite de lo que vendría siendo una tabla ouna entidad.

• Me va permitir relacionar datos.

#### Clave Foránea:

• Es cuando en una entidad figura la clave primaria de otra entidad , esta se denomina clave foranea o clave ajena.

• Las entidades se realcionan entre si por medio de las claves foranea

####  Metadatos:

• Son Datos sobre los datos  presentes en la Base de Datos.

• Hace referencia al tipo de Dato que vamos a almacenar ( texto, nuemro, fechas, etc.)

• También el nombre que va a recibir cada dato (nombre, apellido, fecha, edad, etc.)

#### Operadores Lógicos:

•Los operadores lógicos nos van a permitir definir sentencias así como también  llamar datos.


![image](https://user-images.githubusercontent.com/72580574/200967251-a6491a87-d16a-4c47-8dd7-6c0a878066ba.png)

#### Función que realiza el operador:

Una función de operador se centra en uno y tres argumentos y devuelve un valor.

Cuando una sentencia SQL contiene un operador, el Servido de bases de Datos, invoca automáticamente la función del operador asociado.

---
---

### OPERACIONES FUNDAMENTALES

1. SELECCIÓN

2. PROYECCIÓN

3. SELECCIÓN

---

### SELECCIÓN:

• Me va atraer todos los datos de la tabla en general.

• Se va a ocupar de seleccionar filas
   

En la ventana de comandos nos arrojada los datos de la tabla ya sean generales o solo los que seleccionemos.

```SQL
SELECT * FROM (nombre de tabla);
```

O 


```SQL
SELECT NOMBRE, EDAD FROM (NOMBRE DE TABLA)
```



```*FROM```, nos arrojará todos los datos de la tabla

![image](https://user-images.githubusercontent.com/72580574/200967532-85f11e48-7db0-4321-9c81-c044efdf12f6.png)

Si especificamos los datos, solo nos arrojará los solicitados.

![image](https://user-images.githubusercontent.com/72580574/200967553-9caa465f-7e8c-45e1-b719-8ab0f5b80f88.png)


---

### PROYECCIÓN:


• Esta operación nos ayuda a seleccionar datos específicos.

• Sólo traerá el campo específico que se le indique.

• Se va  a ocupar de seleccionar columnas 

```SQL
SELECT nombre FROM estudiantes where Nombres ='nombre';
```

ó

```SQL
SELECT nombre, edad FROM estudiantes where Nombres='nombre';
```

![image](https://user-images.githubusercontent.com/72580574/200967735-62e18320-8b39-4555-90eb-fee013959fe8.png)

![image](https://user-images.githubusercontent.com/72580574/200967747-d17a6d61-dc0f-4709-b550-093279f4b826.png)


Como ingresamos datos en nuestras tablas:

![image](https://user-images.githubusercontent.com/72580574/200967784-a5fb50da-5772-40f0-be65-433cde682213.png)

![image](https://user-images.githubusercontent.com/72580574/200967794-c9f866ae-2678-433d-89b1-58d03ffea0ea.png)

Para que me permita ingresar datos debemos ingresar nuevamente a la configuración de la tabla y seleccionar en la fila id estudiante  en la opción 

AI (Auto Incrementable) y aplicamos.

![image](https://user-images.githubusercontent.com/72580574/200967821-652a49ea-ec64-40e6-a90a-99e734d2cfe6.png)


---

### Actividad

1.   Responder cuestionario para la asistencia en el Campus.

2. Realizar la siguiente actividad:

A) ingresar datos en la tabla creada la clase anterior.

B) utilizar los operadores para selección y proyección

---





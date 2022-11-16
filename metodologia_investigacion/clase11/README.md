# :star: Clase 12 * Comandos

---

## LENGUAJE SQL

Los orígenes del SQL nos llevan a la década de 1970, cuando en IBM se creó un software de base de datos, llamada  System R . Para gestionar los datos almacenados en System R se creó el lenguaje SQL.

Es un lenguaje que nos permite maniobrar, crear, modificar y gestionar bases de datos. En ese entonces no se las mensionaba como base de datos sino como base de almacenamiento.

Es un lenguaje de computación para trabajar con conjunto de datos y las relaciones entre ellas.

### ¿ Que nos permite ?

Cuando nosotros hablamos de SQL nos estamos refiriendo a algo relacional.

Al ser un modelo relacional, necesitamos entidades, tablas, columnas.

Necesitamos que todo tenga relación entre así, que la información tenga sentido en conjunto y no por separado.

### ¿ Para que se utiliza ?

SQL se utiliza para describir conjuntos de datos que pueden ayudarle a responder preguntas.

Al usar ese lenguaje se  debe usar la sintaxis correcta.

### Sintaxis:

Sintaxis en la forma en que se escribe un comando. Son las reglas que se deben de seguir para dar órdenes.

La sintáxis SQL se basa en la sintaxis del idioma inglés y usa mucho de los mismos elementos de Visual Basic.

### Elemento SQL:

![image](https://user-images.githubusercontent.com/72580574/202307743-4ab5f830-7a05-41c7-9662-f17ffd80ef7b.png)

### Linea de comandos

Todos los comandos necesarios en los sistemas de gestión se ejecutan a través de una interfaz específica llamada línea de comandos SQL (Command- line interface o CLI)

### Query (conusltas)

Es una sentencia que va a dar  una orden o una indicación.

Va a recuperar los datos en base a un criterio dado, trayendo datos de una base de datos o de una tabla.

### Consulta SQL

Son también sentencias que nos da estados de cada uno de los componentes de la base de datos y de cómo están las querys, si se ejecutan o si no se ejecuta.

Todas las cláusulas van a realizar siempre una función.

Se ve error de sintaxis, entre otras cosas.

![image](https://user-images.githubusercontent.com/72580574/202307935-ebc8200a-a637-450a-9f20-43abdb592ea3.png)


---

###  COMANDOS (SENTENCIAS)


Se utilizan para el envío de consultas desde un programa cliente a un servidor donde se almacenan las bases de datos.

Un comando es una sentencia u orden, es una indicación que se le da a partir de una nomenclatura propia de SQL.

---

###  TIPOS DE COMANDOS:

### EXISTEN DOS TIPOS DE COMANDOS SQL :

- **DDL**  (DATA DEFINITION LANGUAJE)

Nos va a permitir y crear nuevas bases de datos, campos e índices.

Un campo es un espacio en el que va a ir un dato, mientras que un índice es un espacio donde se va a agrupar un dato.

Estos tres comandos que son:

**CREATE**: sirve para eso, para crear nuevos campos, ya sean nuevas bases de datos, nuevas tablas, nuevos campos, nuevos índices 

**DROP**:  sirve para eliminar tablas e índices.

**ALTER**:  es utilizado para modificar las tablas agregando campos o cambiando la definición de los mismos.

- **DML** (DATA MANIPULATION LANGUAJE)

Su función es la manipulación de Datos, a través de él podemos insertar, eliminar y actualizar datos.

También generar consultas para ordenar, filtrar y extraer datos de la base de datos.​

Comandos DML:

**INSERT**: Es utilizado para cargar lotes de datos de una base de datos en una única operación. Un insert va a introducir nuevos datos o conjunto de éstos en una base de datos (tabla).

**UPDATE**: utilizado para modificar los valores de los campos y registros especificados.​

**DELETE**: utilizado para eliminar registros de una tabla de base de datos . Se la eliminando uno a uno los registros.

---

### EXPRESIONES

Las expresiones pueden producir valores escalares o tablas que consisten en columnas y filas de datos.

Una expresión me va a traer como resultado distintas funciones, pero entre ellas la creación de columnas y tablas.

### PREDICADOS:

Los predicados especifican las condiciones que se utilizan para limitar los efectos de los comandos y las consultas o para cambiar el flujo del programa.

Un predicado va a ser como un condicional que técnicamente le va a dar un alcance a un comando.

**Instancia** : Nos permite conectarnos a una base de Datos

En Workbenck vamos a crear una nueva instancia, haciendo click en el signo + , donde se nos abrirá una nueva ventana.

![image](https://user-images.githubusercontent.com/72580574/202308657-cd54cfca-3249-4348-9364-5bb71bec3dd6.png)

Escribimos El Nombre De La Nueva Conección En Este Caso colocaremos Metodología y hacer click en el boton Test connection, les pedirá la clave cuando abrieron workbench, introducen la clave y luego dan ok y listo

![image](https://user-images.githubusercontent.com/72580574/202308685-6eb96d31-3961-4c5b-a955-d63a889faa72.png)

Se Ha Creado Una Nueva Conección

![image](https://user-images.githubusercontent.com/72580574/202308706-fb062f0f-883b-4355-b201-ed777ce68f1f.png)

Ingresar A La Nueva Conección Creada

![image](https://user-images.githubusercontent.com/72580574/202308733-79cc5c46-80b2-4aed-918a-acb6ac51708d.png)

Creamos Una Base De Datos Desde La Ventana De Comandos con el comando:
 
```Create database <Nombre de la base de Datos>;```

Hacemos Click en el icono del rayo y automáticamente nos aparecerá debajo la confirmación que la base de dato a sido creada.

![image](https://user-images.githubusercontent.com/72580574/202308859-2c1f7c64-ac5c-42c6-a271-c3a56fc8ecbb.png)

Si REFRESCAMOS LA INFORMACIÓN NOS APARECERÁ LA BASE DE DATOS CREADA

![image](https://user-images.githubusercontent.com/72580574/202308891-66399b74-74af-4ecc-9817-58146522675e.png)

Creamos 2 Bases De Datos Más sin utilizar el ;(punto y coma) y seleccionado el 2ª icono de  rayo, refrescar para ver las bases creadas.

![image](https://user-images.githubusercontent.com/72580574/202308914-9e879d73-5771-4278-962d-ea2807c3cb99.png)

![image](https://user-images.githubusercontent.com/72580574/202308947-186bdc82-aa3b-415f-bd03-7fa065f24fbf.png)

![image](https://user-images.githubusercontent.com/72580574/202308967-45c84857-9ee1-404f-9a26-0ec77893019f.png)


---

## :star: Actividad

1. Realizar Cuestionario para la asistencia en el campus de 21 a 23hs.

2. Crear una nueva conección con el nombre *Metodología*​

3. Crear una base de Datos con el nombre *BASE1* desde la ventana de comandos 

4. Creamos 2 bases de datos más (en total debe haber 3 bases de datos)

5. dentro de cada base de datos ingresaremos los comando para crear una tabla.

datos que debe contener la tabla:

```
-id
-nombre
-apellido
-correo
````

las tablas de las base2 y base3 pueden ser otros datos

---

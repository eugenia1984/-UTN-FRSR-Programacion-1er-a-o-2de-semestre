# :star: Clase 13 (15/11) * Tablas

---

###  <img src="https://img.icons8.com/external-flaticons-lineal-color-flat-icons/40/null/external-table-mobile-app-development-flaticons-lineal-color-flat-icons-4.png"/> TABLAS

![image](https://user-images.githubusercontent.com/72580574/202463952-21e1b2cb-c523-4e2d-8c40-3e9840321fc9.png)

---

### <img src="https://img.icons8.com/external-flaticons-lineal-color-flat-icons/20/null/external-table-mobile-app-development-flaticons-lineal-color-flat-icons-4.png"/> Use:


Nos permite posicionarnos en una base de datos : 

```SQL
Use <nombre de la base>;
```

![image](https://user-images.githubusercontent.com/72580574/202464115-b1d132af-7d55-4b1f-8e8b-7c2900454e93.png)


---

###  <img src="https://img.icons8.com/external-flaticons-lineal-color-flat-icons/20/null/external-table-mobile-app-development-flaticons-lineal-color-flat-icons-4.png"/> CARGAR DATOS EN LAS TABLAS :


- Para cargar datos a nuestras tablas utilizaremos también una sentencia SQL propiamente del lenguaje a partir de palabras reservadas, en este caso utilizaremos: 

```SQL
Insert Into <nombre de la tabla> values (<valores>);
```

- Para tener en cuenta los datos en  números se escriben en números 

- Los datos tipo caracter o varchar se escriben entre 1 comilla 'Nombre'


UNA VEZ QUE UTILIZAMOS LOS COMANDOS iNSER iNTO CON TODOS LOS VALORES DE NUESTRA TABLA, EJECUTAREMOS  CON EL ÍCONO DEL RAYO.

![image](https://user-images.githubusercontent.com/72580574/202465393-ffb402f2-90d9-4129-a63e-db9322bd5bed.png)

---

###  <img src="https://img.icons8.com/external-flaticons-lineal-color-flat-icons/20/null/external-table-mobile-app-development-flaticons-lineal-color-flat-icons-4.png"/> SENTANCIA SELECT:

UTILIZAREMOS LA SENTENCIA SELECT *FROM  PARA VISUALIZAR LOS DATOS INGRESADOS EN NUESTRA TABLA, EN ESTE CASO AL EJECUTAR LA SENTENCIA UTILIZAREMOS EL RAYO CON EL CURSOR , PARA EJECUTAR SÓLO LA ULTIMA LÍNEA 

```SQL
SELECT *FROM <nombre de la tabla>;
```

Ejecutando la sentencia SELECT *from pero con el rayo que tiene el curso , porque sólo queremos ejecutar la última línea de comandos.

![image](https://user-images.githubusercontent.com/72580574/202464548-a5c89dd4-39a6-4d66-a495-b01d821d8c6e.png)

Una vez ejecutado el comando, no aparecerá la tabla con los datos ingresados

![image](https://user-images.githubusercontent.com/72580574/202464593-4ce7daa4-8fc9-4dd2-a530-bd37f2aa8533.png)

---

### :star: Actividad

Generamos datos para nuestras tablas creadas en cada base de dato de la clase nº12, añadiendo tres filas de datos a cada una de ellas.

Utilizar sentencias:

```
Use 
Inser Into
Select * From
```

Añadiendo más datos a las tablas creadas dentro de las bases de datOs de la clase 12

![image](https://user-images.githubusercontent.com/72580574/202464723-5f8229a7-ed08-4aac-9c27-f4639df4a449.png)

---

###  <img src="https://img.icons8.com/external-flaticons-lineal-color-flat-icons/20/null/external-table-mobile-app-development-flaticons-lineal-color-flat-icons-4.png"/> SENTENCIA SELECT 

La sentencia SELECT es  para mostrar, para ver, para visualizar datos de una base de datos.

```SQL
Select <columna> form<nombre base.nombre tabla>;
```
Nos permite traer los datos específicos cuando no utilizamos el asterisco y seleccionando sólo los datos que necesitamos

![image](https://user-images.githubusercontent.com/72580574/202465645-8676cf1f-bd44-4f40-bb94-a4b190e53624.png)

Nos permite traer datos de diferentes columnas

```SQL
SELECT <COMULMNA1 , COLUMNA 3 , COLUMNA 5 FROM <NOMBRE DE LA BASE>.<NOMBRE DE LA TABLA>;
```

![image](https://user-images.githubusercontent.com/72580574/202465735-4405b8cd-7737-42d4-8871-f91122fcca3c.png)

####  <img src="https://img.icons8.com/external-flaticons-lineal-color-flat-icons/20/null/external-table-mobile-app-development-flaticons-lineal-color-flat-icons-4.png"/> SELECT TAMBIÉN NOS PERMITE CAMBIAR EL NOMBRE A UNA COLUMNA


UTILIZAREMOS 

```SQL
Select <Nombre de la columna a> AS <nuevo nombre de la columna> FROM < Nombre dela Base> . <Nombre de tabla>;
```

![image](https://user-images.githubusercontent.com/72580574/202465842-926e0a45-1ee2-4403-8e29-1e12aa404e08.png)

Para cambiar el nombre a mútiples columnas

```SQL
Select <Nombre de la columna A > AS <nuevo nombre de la columna A>, <nombre de columna B> AS < nuevo nombre columna B > FROM < Nombre dela Base> . <Nombre de tabla>;
```

![image](https://user-images.githubusercontent.com/72580574/202465947-daa4007d-531b-47c4-932f-f8222d21fd0e.png)


---

###  <img src="https://img.icons8.com/external-flaticons-lineal-color-flat-icons/20/null/external-table-mobile-app-development-flaticons-lineal-color-flat-icons-4.png"/> SENTENCIA WHERE:


Esta sentencia me traer datos escpecíficos según lo que se le especifique en la búsqueda

```SQL
SELECT * FROM base1.usuario where nombre = "Romina";
```

![image](https://user-images.githubusercontent.com/72580574/202466038-cbaeabbd-c58c-4d7b-84a9-d610ea31237c.png)


---

###   <img src="https://img.icons8.com/external-flaticons-lineal-color-flat-icons/20/null/external-table-mobile-app-development-flaticons-lineal-color-flat-icons-4.png"/> SENTENCIA DISTINCT:

Esta sentencia me va a permitir mostrar datos distintos de  una sola columna, oviará los datos repetidos

![image](https://user-images.githubusercontent.com/72580574/202466115-b208a392-c762-4500-b4d1-1c3c9c482b0d.png)


---

## :star: Actividad  
 
1. Responder el cuestionario para la asistencia en el campus​

2. Realizar la Actividad nº 1 (no deben enviar captura)​

3. Ejercitar las sentencias vista durante la clase

---



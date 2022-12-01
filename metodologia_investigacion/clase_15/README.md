# :star: Clase 15 ( 30/11) * Consultas SQL

---

## Sentencias:

Sentencia para traer datos específicos de una o varias tablas


Para ello utilizaremos las sentencia:
```SQL
use base1;
select * from usuario where nombre like "J%";
```


El símbolo de  ```%```, hace referencia a cuando buscamos un dato que **empiece con una letra**, se va  a colocar la letra específica de la búsqueda y luego el sígno de porcentaje.

 
- ```LETRA%``` ->   Si se quiere buscar una palabra que finalice con una determinada letra se colocará delante de la letra.

- ```%LETRA``` -> O si se necesita buscar datos que contengan letras específicas se clocará

- ```%letra%``` -> nos arroja el dato que empieza con la letra específica

![image](https://user-images.githubusercontent.com/72580574/205054705-801bf95f-d59a-4b99-a877-702cf8afacdc.png)

- ```%letra``` -> nos arroja con la letra que finaliza el dato

![image](https://user-images.githubusercontent.com/72580574/205054798-35992378-49ff-4425-b378-82265b33fcd4.png)

- ```%letra%``` -> para búsquedas de letras específicas en datos

![image](https://user-images.githubusercontent.com/72580574/205054972-f07c2c56-d373-49e3-a6de-568c2ab6647d.png)

También se puede especificar por  cantidad de carácter que tenga un dato.

Según la cantidad de carácter que tenga ese dato.

Por ejemplo si un dato tiene 5 carácter utilizaremos el guión bajo “_” según la cantidad de caracteres que tenga el dato que necesitamos que nos arroje.

### Ejemplo

```SQL
use base1;
select * from usuario where nombre like "_____";
```

![image](https://user-images.githubusercontent.com/72580574/205055101-2ac45d98-bf6c-4722-b51c-a09b8c7524a1.png)


### Como cambiar nombre de columnas y tablas utilizando sentencias

Para cambiar el nombre a las columnas utilizaremos

```SQL
Use nombre base;
alter table nombre tabla change nombrede columna Nuevo nombre de columna varchar (50);
select * from nombre tabla; //para visualizer la modificación de nuestra tabla//
```

Utilizando “_” el guion bajo para  especificar la cantidad de caracteres que necesitamos que nos arroje.

### Utilizamos la sentencia chage para cambiar nombre a nuestra columna

![image](https://user-images.githubusercontent.com/72580574/205055253-86600ceb-1fb1-438b-bb94-dda08e961a71.png)


### Para cambiar el nombre de la tabla utilizaremos el Rename

```SQL
alter table <nombre tabla> Rename < nuevo nombre tabla>;
```

Para visualizar el cambio de nombre de nuestra tabla, refrescamos datos.

![image](https://user-images.githubusercontent.com/72580574/205055337-7a30e56c-4132-4c84-aee0-c6b2f21d7cc5.png)


### Cardinalidad:

La cardinalidad puede definirse como el número de entidades, la cual otra entidad se puede asociar mediante una relación binaria, o sea, de una  sola relación.

![image](https://user-images.githubusercontent.com/72580574/205055420-8207bd2c-4b89-4c30-ac5a-609ae31a176a.png)

### La cardinalidad puede ser de distintas formas.

![image](https://user-images.githubusercontent.com/72580574/205055453-a040fd06-794d-47a0-9e03-2ac832f0c073.png)

---

## :star: Actividad:

1. Realizar cuestionario para la asistencia en el campus.

-> Ya en el campus

2. Realizar ejercicio aplicándo las sentencias vistas en clase.

---

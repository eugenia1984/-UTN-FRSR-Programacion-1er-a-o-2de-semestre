# :star: Clase 14 (23/11) : SENTENCIAS

---

## ORDER BY

Se utiliza para ordenar de forma ascendente o descendente una un campo en una tabla, ya sea por medio de A la Z, z a la A de 1 hasta el infinito o desde el infinito hasta el 1.
```SQL
use <nombre de la base>;
Select * from <nombre de la base>. <nombre tabla> order by <nombre columna> asc;
```

### Orden de forma ascendente.

```SQL
use base1;
select * from base1.usuario order by nombre asc;
```

![image](https://user-images.githubusercontent.com/72580574/204038688-a0e4da8d-bc81-450c-8935-d8006e531710.png)

### Ordenar de forma descenedente

```SQL
use base1;
Select * from base1.usuario order by nombre desc;
```

![image](https://user-images.githubusercontent.com/72580574/204038726-0460aba6-03f8-40ef-91f3-c6cf510dabac.png)

---

## SENTENCIA NOT

El operador Not lo que hace es que no me muestra el valor que yo le indique, esto me permitirá traer sólo los datos que necesito trabajar en ese momento.

```SQL
use <nombre de la base>;
Select * from <nombre base>. <nombre tabla>
Where not <columna de la tabla>  = “dato específico";
```

-> Utilizamos el operador Not para eliminar algún dato que no necesite ver en mi tabla

```SQL
use base1;
Select * from base1.Usuario
Where not apellido = "Rojas";
```

![image](https://user-images.githubusercontent.com/72580574/204038815-33201518-5322-4ec7-ba7c-7b3b39dc1117.png)


---

## SENTENCIA DROP

Esta sentencia no permite  eliminar columnas,  un dato en específico y  eliminar una base de datos.

```SQL
Use <nombre de la base>;
alter table <nombre tabla>
drop column <nombre columna>
```

Ejemplo:
```SQL
use base1;
alter table Usuario
drop column correo
```


![image](https://user-images.githubusercontent.com/72580574/204038933-6027e3f0-bb7c-4bf9-94ee-81ed9c761797.png)

Se eliminará la columna seleccionada

![image](https://user-images.githubusercontent.com/72580574/204038948-86a949f7-2a5a-4e07-9d4f-b20dd421df0f.png)


---

## SENTENCIA DELETE

Esta sentencia nos permitirá eliminar, contenidos de tablas específicos o en general

Si utilizamos sólo el comando DELETE FROM y el nombre de la tabla eliminaremos todo el contenido de dicha tabla


```SQL
use <nombre de la base>;
delete from <nombre de la tabla>
```

Ejemplo:
```SQL
use base1;
delete from usuario
```

![image](https://user-images.githubusercontent.com/72580574/204039009-99227062-a0f9-4579-8dc1-4dcc2ec67a57.png)

Para no eliminar todos los datos de una tabla acompañamos el delete con el **where**

```SQL
use <nombre de la base>;
delete from <nombre de la tabla> where <nombre de la columna> = “dato específico”;
```

![image](https://user-images.githubusercontent.com/72580574/204039048-cdc9df44-3c57-4632-83a2-f25aca80cafe.png)

De esta manera sólo estaríamos eliminando datos específicos y no todos los datos.

![image](https://user-images.githubusercontent.com/72580574/204039067-76276afd-0587-4d5f-b91f-2e39937deb86.png)


---

```SQL

```

```SQL

```

```SQL

```

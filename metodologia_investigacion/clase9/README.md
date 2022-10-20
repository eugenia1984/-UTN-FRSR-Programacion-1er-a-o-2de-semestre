# :star: Clase 9 * 19 Octubre * MySQL

---

Es un sistema open source de administración de bases de datos que es desarrollado y soportado por Oracle.

---

## SU ORÍGEN:


MySQL fue originalmente lanzado en 1995. Desde entonces, ha pasado por varios cambios de propiedad/administración, antes de terminar en la Oracle Corporation en 2010. A pesar de que Oracle está a cargo ahora, MySQL sigue siendo un software open source, lo que quiere decir que usted puede usarlo y modificarlo a su gusto.

El nombre viene al juntar “My” – el nombre de la hija del co-fundador – con SQL – la abreviatura de Structured Query Language, el cual es el lenguaje de programación que le ayuda a acceder y administrar datos en una base de datos relacional.

"Kinsta me mimó tanto que ahora exijo ese nivel de servicio a todos los proveedores. Nosotros también intentamos estar a ese nivel con nuestro soporte de herramientas SaaS."

Para poder entender como funciona MySQL, es importante conocer dos conceptos conectados:

- Base de datos relacionales

- Modelo de Cliente-servidor


---

## Bases de Datos Relacionales:


- Cuando se trata de almacenar datos en una base de datos, hay distintos enfoques que usted puede utilizar.

- MySQL opta por un enfoque llamado una base de datos relacional.

- Con una base de datos relacional, sus datos son fragmentados en varias áreas de almacenamiento separadas – llamadas tablas – en lugar de poner todo junto en una gran unidad de almacenamiento.

- Por ejemplo, digamos que quiere almacenar dos tipos de información:
```
Clientes – su nombre, dirección, detalles, etc.
Pedidos – como los productos que compran, el precio, quién hizo la orden, etc.
````

### Si intenta poner todos estos datos juntos en un gran bote, tendrá algunos problemas como:

- Datos distintos – los datos que usted necesita para recolectar para una orden son diferentes que los que son para un cliente.

- Datos duplicados – cada cliente tiene un nombre, y cada orden también tiene el nombre de un cliente. El lidiar con datos duplicados suele ser complicado.

Sin organización – ¿cómo se conecta uno de forma concisa la información de un pedido con la información de un cliente?

### Para resolver esos problemas:


Una base de datos relacional usaría una tabla separada para los clientes y otra tabla separada para las ordenes.

Sin embargo, usted querrá poder decir “muéstreme todas las ordenes para un determinad cliente”. Aquí es donde entra la parte relacional.

### Llave:

Al usa una “llave”, usted podrá enlazar los datos, usted verá qué utiliza este modelo relacional, con todos sus datos divididos en tablas separadas.


Por defecto, WordPress utiliza 12 tablas separadas, pero muchos plugins de WordPress también agregarán sus propias tablas. Por ejemplo, ¡la base de datos para el sitio de WordPress de abajo tiene 44 tablas separadas!

---

## WordPress :


Almacena publicaciones de blog en la tabla de wp_posts y los usuarios en la tabla de wp_users. Sin embargo, porque esas dos tablas están conectadas por una llave usted podrá enlazar cada cuenta de usuario con todas las publicaciones de blog que cada usuario ha escrito.

![image](https://user-images.githubusercontent.com/72580574/196827234-8c7b7587-fdd3-41d9-b884-0dd7b218a8fb.png)


Cada publicación es asignada a post_author, la cual es un número único de identificación (esta es la llave

![image](https://user-images.githubusercontent.com/72580574/196827222-9a6059c1-152d-4c92-af53-fa92fa190aaf.png)

Luego, si quiere ver qué cuenta de usuario corresponde a ese número, usted podría ver la ID en la tabla de wp_users:
![image](https://user-images.githubusercontent.com/72580574/196827280-8238c344-786d-4bf0-8f36-f0b54af19636.png)

**La llave – el número ID – es lo que conecta todo. Y así es como se “relacionan” una con otra, a pesar de almacenar los datos en tablas separadas**

---

## Modelo de Cliente-Servidor:

- Más allá del sistema de bases de datos relacional, MySQL también utiliza algo llamado el modelo cliente-servidor.

- La parte de servidor es donde sus datos realmente residen. Pero, para poder acceder a estos datos, usted deberá pedirlos. Aquí es donde entra el cliente.

- Usando SQL- el lenguaje de programación que mencionamos anteriormente – el cliente envía una petición al servidor de la base de datos para los datos que el cliente necesita.

- Por ejemplo, si alguien visita una publicación de un blog en su sitio, su sitio de WordPress enviará múltiples peticiones SQL al servidor de la base de datos para obtener toda la información que necesita para entregar la publicación del blog al navegador del visitante. Haría:

- Consulta a la tabla wp_posts para obtener contenido para la publicación del blog

- Consulta a la tabla de wp_users para obtener información para la casilla del autor (utilizando la llave que le mostramos anteriormente)


Si quiere ver exactamente qué tipos de peticiones de bases de datos son hechas por su sitio de WordPress, usted puede utilizar un maravilloso plugin llamado Query Monitor para ver la interacción exacta entre su sitio de WordPress (el cliente) y el servidor de la base de datos:

## VENTAJAS:



- Ahorra tiempo, costes y maximiza el rendimiento del sitio con:

- Ayuda instantánea de expertos en alojamiento de WordPress, 24/7.

- Integración de Cloudflare Enterprise.

- Alcance de audiencia global con 35 centros de datos en todo el mundo.

- Optimización con nuestra herramienta de monitoreo de rendimiento de aplicación integrada.

- es libre y gratuito;

 - los requisitos para crear y usar una base de datos son relativamente escasos;

 - relacionado con el punto anterior, no es necesario contar con un ordenador muy poderoso para bases de datos normales;

 - es muy rápido y fácil de usar;

 - lo soportan casi todos los sistemas operativos;

 - las probabilidades de corrupción de datos son muy bajas;

 - es muy seguro.

---

### Pasos para instalar MySQL en Windows


MySQL está disponible tanto para entornos Windows como para arquitecturas de 32 o de 64 bits, de modo que no creo que os cueste demasiado seguir los pasos que os proponemos para poder instalar MySQL de manera rápida.

La manera más fácil de instalar MySQL en Windows es utilizar MySQL Community Server en la web de mysql.com (en el apartado Descargas o «Downloads»).

Ahora tendrás que elegir la opción indicada en función de tu sistema, en este caso, Windows (verás que aparecen dos versiones, una más pesada que la otra, puedes elegir la primera de 1,5 M).

Una vez descargado, MySQL Community Server, puede que nos solicite también la descarga de Microsoft.NET Framework 4 Client Profile.

Comienza la descarga de MySQL y para ello tendremos que elegir la opción de «Install MySQL Products»

5. Ahora se nos pedirá que seleccionemos el tipo de instalación, lo mejor es elegir la primera que es la instalación por defecto (Developers      
      
Default). Además deberás cambiar a C:MySQL en la carpeta donde deseas que se guarde la instalación.​

 6. A continuación, comenzará la instalación del programa y verás como,  además se instalan algunos complementos
 
 7.Después de eso, se verificarán los requisitos del sistema y, de cumplirse, se iniciará la instalación. Finalmente, se mostrará la pantalla de configuración.

8En esta pantalla, abajo del todo deberás escribir una contraseña para tu usuario. Además, puedes añadir otros usuarios.

9.Una vez que se completa la instalación, el servidor MySQL se iniciará automáticamente. Si hemos marcado la opción «Crear servicio de Windows» en la última pantalla nuestro servidor MySQL se iniciará simultáneamente cada vez que se inicie nuestro sistema.
    
 ---
    
 ### Actividad:

1-Responder cuestionario  para la asistencia en el campus.

2-Realizamos insatalación de MySQL


---

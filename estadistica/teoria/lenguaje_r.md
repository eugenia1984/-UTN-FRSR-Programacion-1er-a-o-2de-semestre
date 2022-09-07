# :star2: Lenguaje R :star2:

---

## ¿ Qué es lenguaje R ?

- R es un software creado en 1993 por Robert Gentleman y Ross Ihaka, que respeta la libertad de los usuarios y es similar al lenguaje y entorno S, creado en Bell Laboratories (antes AT&T, ahora Lucent Technologies) por John Chambers y algunos colegas, a finales de los 70.

- Si bien R guarda algunas diferencias importantes respecto a S, gran parte del código escrito para S se ejecuta sin cambios en R. Es por eso que se afirma naturalmente que R viene de S.

- Con el software libre R se puede hacer modelos de regresión lineal y logísticos, análisis de series de tiempo, pruebas estadísticas clásicas, agrupamientos, clustering, clasificaciones y aplicar muchas otras técnicas estadísticas.

- R es la elección perfecta de código abierto para participar en la investigación estadística. R permite producir gráficos de alta calidad con mucha facilidad, incluyendo símbolos matemáticos y fórmulas, siempre que sea necesario.


---

## ¿ Para qué sirve R ?

Este software libre proporciona un amplio abanico de herramientas estadísticas y gráficas que permiten a los usuarios definir sus propias funciones. En ese sentido, R es uno de los lenguajes de programación más utilizados en áreas como:

- Investigación científica.

- Manipulación de datos.

- Análisis estadístico.

- Inteligencia artificial.

- Aprendizaje automático o Machine Learning.

- Técnicas gráficas.

- Modelado y predicciones.

- Matemáticas financieras.

- Bioinformática.

- Investigación biomédica.

- También puede usarse como herramienta de cálculo numérico, y en este campo es tan eficaz como GNU Octave y su equivalente privativo, MATLAB.



---

## Ventajas de R

- **Ahorra gastos en licencias**: Al ser un software GNU no pertenece a nadie, y por lo tanto no debes pagar ninguna licencia.
Accesible: Funciona con paquetes fáciles de descargar que otras personas previamente han programado.

- **Libre//: El usuario puede distribuir, estudiar, cambiar y mejorar libremente el software bajo la GNU de la Free Software Foundation.

- **Excelente para el análisis y cálculo estadístico**: Es un lenguaje estadístico creado por estadísticos. Por eso, actualmente es el más utilizado para desarrollar herramientas estadísticas.

- **Soporte multiplataforma**: Es un programa independiente de la máquina, compatible con la operación multiplataforma, así que se puede utilizar en diferentes sistemas operativos.

- **Admite varios tipos de datos**: Desde vectores hasta matrices y datos de diferentes tamaños.

- **Gráficos potentes**: Puede producir gráficos y visualizaciones de alta calidad, ya sean de naturaleza estática o dinámica.

- **Computación paralela y distribuida**: Puede procesar grandes conjuntos de datos utilizando bibliotecas como ddR o multiDplyr.


---

## ¿ Dónde se puede obtener ?

Todos los paquetes de R están disponibles en la CRAN (Comprehensive R Archive Network) [http://cran.r-project.org/](http://cran.r-project.org/****) y se pueden descargar en Windows, Mac y Linux. El sitio web también proporciona información básica para descargar e instalar el software en los diferentes sistemas operativos. Finalmente, como antes hemos aclarado, este software no tiene ningún costo.

![image](https://user-images.githubusercontent.com/72580574/187312347-24ccb0bd-11f9-49a0-82d6-412bb010eab8.png)

---

## Características de R

- R version 4.2.1 (2022-06-23 ucrt) -- "Funny-Looking Kid"

- Copyright (C) 2022 The R Foundation for Statistical Computing

-Platform: x86_64-w64-mingw32/x64 (64-bit)

- R es un software libre y viene sin GARANTIA ALGUNA.

- Usted puede redistribuirlo bajo ciertas circunstancias.

- Escriba ```license()``` o  ```licence()``` para detalles de distribucion.

- R es un proyecto colaborativo con muchos contribuyentes.

- Escriba ```contributors()``` para obtener más información y ```citation()``` para saber cómo citar R o paquetes de R en publicaciones.

- Escriba ```demo()``` para demostraciones

- Escrriba ```help()``` para el sistema on-line de ayuda o ```help.start()``` para abrir el sistema de ayuda HTML con su navegador.

- Escriba ```q()``` para salir de R.

---


## Obteniendo ayuda en R

Recuerda que existen dos maneras de obtener ayuda en R. 

Lo puedes hacer a traves del menu o de la ventana de comandos. 

1. La funcion ```mean``` calcula la media aritmetica de una serie de valores. 

¿Cuales son los argumentos de dicha funcion? 

2. Dado un conjunto de valores, sabemos que existe una funcion en R que calcula el maximo, pero no recordamos su nombre.

¿Serıas capaz de encontrarla a traves de la ayuda? Recuerda que la ayuda esta en ingles.

3. Queremos utilizar el comando ```help.search``` para obtener informacion sobre la funcion ```plot```. 

El resultado es el siguiente: 

```
> help.search(plot) Error in help.search(plot) : argument ’pattern’ must be a single character string
```
 
¿Por que nos da error? 

¿Como lo escribirıas de forma correcta? 


---

## :star: Ejercicio 1:

1. Define el vector x = (1, 2, 3, 4, 5, 6). 

- A partir de dicho vector se han construido las matrices m1, m2, m3, m4  

- >``` m1 [,1] [,2] [,3] [1,] 1 3 5 [2,] 2 4 6``` - EXPRESAR ESTA MATRIZ

- >``` m2 [,1] [,2] [1,] 1 4 [2,] 2 5 [3,] 3 6``` - EXPRESAR ESTA MATRIZ  

- > ```m3 [,1] [,2] [,3] [1,] 1 2 3 [2,] 4 5 6 ```- EXPRESAR ESTA MATRIZ

- >``` m4 [,1] [,2] [,3] [1,] 1 4 1 [2,] 2 5 2 [3,] 3 6 3``` EXPRESAR ESTA MATRIZ

- Todas las matrices se han definido a partir de matrix(x,...). Intenta reproducir el codigo necesario para obtener cada una de ellas. Recuerda que puedes consultar la AYUDA



---

## :star: Ejercicio 2:

- Que ocurre cuando definimos una matriz en R y solo especificamos el numero de filas o el numero de columnas? 

- ¿Que ocurre cuando los datos no se corresponden con la dimension de la matriz que queremos definir? Compruebalo ejecutando los siguientes comandos: 

- > ```matrix(1:6,nrow=2) ```

- > ```matrix(1:6,nrow=4) ```

- > ```matrix(1:6,nrow=4,ncol=4)```



---

## :star: Ejercicio 3:

- ¿Cual es la diferencia entre  ```*```, ```%*%``` y ```outer()``` ?

- Compruebalo con las matrices 

```
A = 2 3 1 4 (ES DE 2X2)
B =  3 8 (ES DE 1X2)
```


---

## :star: Ejercicio 4

- Sean A una matriz ```2 × 3```, B una matriz ```3 × 4``` y C una matriz ```2 × 3```.
 
¿De que tipo y dimension seran los objetos obtenidos de los siguientes comandos de R? 

¿Alguno de los comandos produce mensajes de error? 

¿Por que?

a) ```A*B ```

b) ```outer(A,B) ```

c) ```A + 2 ``` 

d) ```A % *% B ``` 

e) ```exp(B). Nota: exp() es la funcion exponencial. ```

f ) ```A * C ``` 

g) ```A % *% C ```



---

## :star: Ejercicio 5:

Un grupo de amigos esta formado por Ana de 23 anos, Luis de 24 anos, Pedro de 22, Juan de 24, Eva de 21 y Jorge de 22 anos. Crea los vectores correspondientes a nombre, edad y sexo.



---

## :star: Ejercicio 6

- Con los datos anteriores hemos creado el dataframe amigos. 

- El resultado es: 
```
> amigos nombre edad 
sexo 1 Ana 23 M ;2 Luis 24 H; 3 Pedro 22 H; 4 Juan 24 H ;5 Eva 21 M ;6 Jorge 22 H 
```

¿Cual es el codigo de R da como resultado esta salida?



---

## :star: Ejercicio 7 * Graficos

- Queremos representar graficamente la funcion coseno en el intervalo ```[0, 2π]```. 

- Para ello creamos el vector x de la siguiente forma: 

```x<-seq(0,2*pi,length=100)```. 

- ¿Cual es la diferencia entre las graficas obtenidas por los siguientes comandos? 

```>plot(cos(x)) y >plot(x,cos(x))```

- Intenta reproducir en lo posible las siguientes gr´aficas. Si tienes cualquier duda consulta la ayuda de las funciones ```plot``` y ```par```.



---

## Tablas de frecuencia y graficos para variables cualitativas

![image](https://user-images.githubusercontent.com/72580574/187313382-3c696fc8-4c62-4a17-8fe5-19b49055b599.png)

- Empezamos con las variables cualitativas. Vemos en primer lugar como obtener las frecuencias absolutas de la variable Equipo. Para ello vamos a utilizar las variables del conjunto de datos utilizando el comando attach:

- > ```attach(datos.alumnos)``` 

- > Altura 

- > Peso 

- > Hermanos

---

- A continuacion, para obtener las frecuencias absolutas utilizamos la funcion table, como sigue:

- > ```fabs <-table(Equipo) ```

- > ```fabs ```

- Equipo : 
```
BAR CEL DEP NIN RMA VAL 
3    4   13  15   8   1
```

- > ```class(fabs)```


- Las frecuencias relativas las podemos obtener simplemente dividiendo la variable fabs por el numero de individuos de la muestra n.ind:

- > ```frel<-fabs/n.ind ```

- Equipo 
```
BAR               CEL                DEP               NIN               RMA  
0.06818182 0.09090909 0.29545455 0.34090909 0.18181818 
```

- VAL
```
0.02272727
```

- Obtenemos ası las frecuencias relativas de cada uno de los equipos de la muestra. Una vez que tenemos estas frecuencias podemos empezar a hacer resumenes graficos para variables cualitativas. Por ejemplo, para hacer un diagrama de barras, podemos escribir:

- > ```barplot(fabs,ylab="Frecuencias absolutas",main="Diagrama de barras de Equipo")```

- Las opciones del grafico son multiples y las podemos comprobar utilizando la ayuda:

- > ```help("barplot")```

- Ver que tambien podemos hacer un diagrama de barras de la variable Equipo utilizando las frecuencias relativas: 

- > ```barplot(frel,ylab="Frecuencias relativas",main="Diagrama de barras de Equipo")```




---

## Tablas de frecuencia y graficos para variables cuantitativas: EJERCICIO NRO 1


- Empezamos con las variables cuantitativas discretas. En primer lugar, obtenemos las frecuencias absolutas y relativas de la variable Hermanos, utilizando la funcion table como sigue:

- > ```fabs<-table(Hermanos) ```

- > ```fabs ```

```
Hermanos 1    2    3   4   6 
         8    24   9   2   1
```

- Las frecuencias relativas las podemos obtener simplemente dividiendo la variable fabs por el numero de individuos de la muestra n.ind: 

- >``` frel<-fabs/n.ind```

- > ```frel Hermanos ```
```
1                    2                    3                   4                    6 
0.18181818 0.54545455 0.20454545 0.04545455 0.02272727
```

- Ademas ahora podemos obtener las frecuencias absoluta y relativa acumuladas. Para ello, podemos hacer lo siguiente: 

> ```fabsacum<-as.table(cumsum(fabs)) ```

> ```fabsacum ```
> 
```
1  2    3  4   6 
8  32 41 43 44 
```

> ```frelacum<-as.table(cumsum(frel)) ```

>``` frelacum ```
>
```
1                  2                 3          4             6 
0.1818182    0.7272727        0.9318182      0.9772727 1.0000000
```  

---
# :star: LENGUAJE R :star: 

---

## Libro R para principiantes

Se puede ver [en este link](https://bookdown.org/jboscomendoza/r-principiantes4/)

---

## :star: CONCEPTOS BASICOS


## Objetos

En R, todo es un objeto. Todos los datos y estructuras de datos son objetos. Además, todos los objetos tienen un nombre para identificarlos.

---

## Constantes y variables

De manera análoga al uso de estos términos en lenguaje matemático, una constante es un objeto cuyo valor no podemos cambiar, en contraste, una variable es un objeto que puede cambiar de valor.

Por ejemplo, en la siguiente expresión, π y 2 son constantes, mientras que a y r son variables.

```a = π r 2```
 

Las constantes y variables en R tienen nombres que nos permiten hacer referencia a ellas en operaciones.

Las constantes ya están establecidas por R, mientras que nosotros podemos crear variables, asignándoles valores a nombres.

En R usamos ```<-``` para hacer asignaciones. De este modo, podemos asignar el valor 3 a la variable radio

```radio <- 3```

Es recomendable que al crear una variable usemos nombres claros, no ambiguos y descriptivos. Esto previene confusión y hace que nuestro código sea más fácil de comprender por otras personas o por nosotros mismos en el futuro.

Los nombres de las variables pueden incluir letras, números, puntos y guiones bajos. Deben empezar siempre con una letra o un punto y si empiezan con un punto, a este no puede seguirle un número.

Finalmente, cuando te encuentres con un renglón de código que inicia con un **gato (hashtag)**, esto representa un comentario, es código que no se ejecutará, sólo se mostrará.

```# Este es un comentario```

---

## Funciones (introducción básica)

Una función es una serie de operaciones a la que les hemos asignados un nombre. Las funciones aceptan argumentos, es decir, especificaciones sobre cómo deben funcionar.

Cuando llamamos una función, se realizan las operaciones que contiene, usando los argumentos que hemos establecido.

En R reconocemos a una función usando la notación: **nombre_de_la_función()**. Por ejemplo:

```
mean()
quantile()
summary()
density()
c()
```

Al igual que con las variables, se recomienda que los nombres de las funciones sean claros, no ambiguos y descriptivos. Idealmente, el nombre de una función describe lo que hace. De hecho, es probable que adivines qué hacen casi todas funciones de la lista de arriba a partir de su nombre.

---

## Documentación

Las funciones de R base y aquellas que forman parte de paquete tienen un archivo de documentación.

Este archivo describe qué hace la función, sus argumentos, detalles sobre las operaciones que realiza,los resultados que devuelve y ejemplos de uso.

Para obtener la documentación de una función, escribimos el ? antes de su nombre y lo ejecutamos. También podemos usar la función help(), con el nombre de la función.

Los dos procedimientos siguientes son equivalentes.

```?mean()```

```help("mean")```

Si usas RStudio, la documentación de la función se mostrará en uno de los paneles de este IDE. Si estas usando R directamente, se abrirá una ventana de tu navegador de internet.

También podemos obtener la documentación de un paquete, si damos el argumento package a la función **help()**, con el nombre de un paquete.

Por ejemplo, la documentación del paquete stats, instalado por defecto en R base.

```help(package = "stats")```

---

## Directorio de trabajo

El directorio o carpeta de trabajo es el lugar en nuestra computadora en el que se encuentran los archivos con los que estamos trabajando en R. Este es el lugar donde R buscara archivos para importarlos y al que serán exportados, a menos que indiquemos otra cosa.

Puedes encontrar cuál es tu directorio de trabajo con la función getwd(). Sólo tienes que escribir la función en la consola y ejecutarla.

```getwd()```

```## [1] "C:/Users/JuanBosco/Documents/GitHub/r-principiantes-bookdown"```

Se mostrará en la consola la ruta del directorio que está usando R.

Puedes cambiar el directorio de trabajo usando la función ```setwd()```, dando como argumento la ruta del directorio que quieres usar.

```setwd("C:\otro_directorio")```

Por último, si deseas conocer el contenido de tu directorio de trabajo, puedes ejecutar. la función ```list.files()```, sin argumentos, que devolverá una lista con el nombre de los archivos de tu directorio de trabajo. La función ```list.dirs()```, también sin argumentos` te dará una lista de los directorios dentro del directorio de trabajo.

```
# Ver archivos
list.files()
# Ver directorios
list.dirs()
```

---

## Sesión

Los objetos y funciones de R son almacenados en la memoria RAM de nuestra computadora.

Cuando ejecutamos R, ya sea directamente o a través de RStudio, estamos creando una instancia del entorno del entorno computacional de este lenguaje de programación. cada instancia es una sesión.

Todos los objetos y funciones creadas en una sesión, permanecen sólo en ella, no son compartidos entre sesiones, sin embargo una sesión puede tener el mismo directorio de trabajo que otra sesión.

Es posible tener más de una sesión de R activa en la misma computadora. Aunque ambas

Cuando cerramos R, también cerramos nuestra sesión. Se nos preguntará si deseamos guardar el contenido de nuestra sesión para poder volver a ella después. Esto se guarda en un archivo con extensión **.Rdata** en tu directorio de trabajo.

Para conocer los objetos y funciones que contiene nuestra sesión, usamos la función ```ls()```, que nos devolverá una lista con los nombres de todo lo guardado en la sesión.

```
ls()
## [1] "radio"
```

De manera más precisa, nuestra sesión es un entorno de trabajo y los objetos pertenecen a un entorno específico.

Los entornos son un concepto importante al hablar de lenguajes de programación, pero también son un tema que sale del alcance de este libro.

Con que recuerdes que cada sesión de R tiene su propio entorno global, eso será suficiente.

---

## Paquetes

R puede ser expandido con paquetes. Cada paquete es una colección de funciones diseñadas para atender una tarea específica. Por ejemplo, hay paquetes para trabajo visualización geoespacial, análisis psicométricos, mineria de datos, interacción con servicios de internet y muchas otras cosas más.

Estos paquetes se encuentran alojados en CRAN, así que pasan por un control riguroso antes de estar disponibles para su uso generalizado.

Podemos instalar paquetes usando la función ```install.packages(),``` dando como argumento el nombre del paquete que deseamos instalar, entre comillas.

Por ejemplo, para instalar el paquete readr, corremos lo siguiente.

```
install.packages("readr")
```

Hecho esto, apareceran algunos mensajes en la consola mostrando el avance de la instalación

Una vez concluida la instalación de un paquete, podrás usar sus funciones con la función ```library()```. Sólo tienes que llamar esta función usando como argument oel nombre del paquete que quieres utilizar

```
library(readr)
```

Cuando haces esto, R importa las funciones contenidas en el paquete al entorno de trabajo actual.

Es importante que tengas en mente que debes hacer una llamada a ```library()``` cada que inicies una sesión en R. Aunque hayas importado las funciones de un paquete con anterioridad, las sesiones de R se inician “limpias”, sólo con los objetos y funciones de base.

Este comportamiento es para evitar problemas de compatibilidad y para propiciar buenas prácticas de colaboración.

Si importamos paquetes automáticamente y usamos sus funciones sin indicar de donde provienen, al compartir nuestro código con otras personas, estas no tendrán la información completa para entender qué estamos haciendo. R, al pedirnos que cada sesión indiquemos qué estamos importando, nos obliga a ser explícito con todo lo que estamos haciendo. Es un poco latoso, pero te acostumbras a ello.

En caso de escribir en ```install.packages()``` el nombre de un paquete no disponible en CRAN, se nos mostrará una advertencia y no se instalará nada.

```install.packages("un_paquete_falso")```

Los paquetes que hemos importado en nuestra sesión actual aparecen al llamar ```sessionInfo()```.

También podemos ver qué paquetes tenemos ya instalados ejecutando la función ```installed.packages()``` sin ningún argumento. Una instalación nueva de R tiene pocos paquetes instalados, pero esta lista puede crecer considerablemente con el tiempo.

---

## cripts

Los scripts son documentos de texto con la extensión de archivo .R, por ejemplo ```mi_script.R```.

Estos archivos son iguales a cualquier documentos de texto, pero R los puede leer y ejecutar el código que contienen.

Aunque R permite el uso interactivo, es recomendable que guardes tu código en un archivo .R, de esta manera puedes usarlo después y compartirlo con otras personas. En realidad, en proyectos complejos, es posible que sean necesarios mútiples scripts para distintos fines.

Podemos abrir y ejecutar scripts en R usando la función ```source()```, dandole como argumento la ruta del archivo .R en nuestra computadora, entre comillas.

Por ejemplo.

```source("C:/Mis scripts/mi_script.R")```

Cuando usamos RStudio y abrimos un script con extensión .R, este programa nos abre un panel en el cual podemos ver su contenido. De este modo podemos ejecutar todo el código que contiene o sólo partes de é

---

## :star: Tipos de datos

En R los datos pueden ser de diferentes tipos. Cada tipo tiene características particulares que lo distinguen de los demás. Entre otras cosas algunas operaciones sólo pueden realizarse con tipos de datos específicos

---

## Datos más comunes

Los tipos de datos de uso más común en R son los siguientes.

| Tipo	| Ejemplo | Nombre en inglés |
| ---=- | ------- | ---------------- |
| Entero |	1 |	integer |
| Numérico	| 1.3 |	numeric |
| Cadena de texto |	“uno” |	character |
| Factor |	uno |	factor |
| Lógico	| TRUE	| logical |
| Perdido	| NA	| NA |
| Vacio	| NULL	| null |

Además de estos tipos, en R también contamos con datos complejos **numéricos complejos** (con una parte real y una imaginaria), **raw** (bytes), fechas y raster, entre otros. Estos tipos tiene aplicaciones muy específicas, por ejemplo, los datos de tipo fecha son ampliamente usados en economía, para análisis de series de tiempo.


- Como su nombre lo indica, los datos **enteros** representan **números enteros, sin una parte decimal o fraccionaria**, que pueden ser usados en operaciones matemáticas.

- Por su parte, como su nombre lo indica, los datos **numéricos** representan números, la diferencia de estos con los datos enteros es que **tiene una parte decimal o fraccionaria**. Los datos numéricos también son llamados **doble** o **float** (flotantes). 

- El tipo **character** representa **texto** y es fácil reconocerlo porque un dato siempre esta **rodeado de comillas, simples o dobles**. De manera convencional, nos referimos a este tipo de datos como cadenas de texto, es decir, secuencias de caracteres. Este es el tipo de datos más flexible de R, pues una cadena de texto puede contener letras, números, espacios, signos de puntuación y símbolos especiales.

- Un **factor** es un tipo de datos específico a R. Puede ser descrito como **un dato numérico representado por una etiqueta**. Supongamos que tenemos un conjunto de datos que representan el sexo de personas encuestadas por teléfono, pero estos se encuentran capturados con los números 1 y 2. El número 1 corresponde a femenino y el 2 a masculino. En R, podemos indicar que se nos muestre, en la consola y para otros análisis, los 1 como femenino y los 2 como masculino. Aunque para nuestra computadora, femenino tiene un valor de 1, pero a nosotros se nos muestra la palabra femenino. De esta manera reducimos el espacio de almacenamiento necesario para nuestros datos. Este comportamiento es similar a lo que ocurre con paquetes estadísticos comerciales como SPSS Statistics, en los que podemos asignar etiquetas a los datos, dependiendo de su valor. La diferencia se encuentra en que R trata a los factores de manera diferente a un dato numérico. Por último, cada una de las etiquetas o valores que puedes asumir un factor se conoce como nivel. En nuestro ejemplo con femenino y masculino, tendríamos dos niveles.

- Los datos de tipo **lógico** sólo tienen dos valores posibles: verdadero (**TRUE**) y falso (**FALSE**). Representan si una condición o estado se cumple, es verdadero, o no, es falso. Este tipo de dato es, generalmente, el resultado de operaciones relacionales y lógicas, son esenciales para trabajar con álgebra Booleana. Como este tipo de dato sólo admite dos valores específicos, es el más restrictivo de R.

- usamos **NA** para representar datos perdidos, mientras que **NULL** representa la ausencia de datos. La diferencia entre las dos es que un dato NULL aparece sólo cuando R intenta recuperar un dato y no encuentra nada, mientras que NA es usado para representar explícitamente datos perdidos, omitidos o que por alguna razón son faltantes.

Por ejemplo, si tratamos de recuperar la edad de una persona encuestada que no existe, obtendríamos un **NULL**, pues no hay ningún dato que corresponda con ello. En cambio, si tratamos de recuperar su estado civil, y la persona encuestada no contestó esta pregunta, obtendríamos un NA.

**NA** además puede aparecer como resultado de una operación realizada, pero no tuvo éxito en su ejecución

- **Coerción**: en R, los datos pueden ser coercionados, es decir, forzados, para transformarlos de un tipo a otro. La coerción es muy importante. Cuando pedimos a R ejecutar una operación, intentará coercionar de manera implícita, sin avisarnos, los datos de su tipo original al tipo correcto que permita realizarla. Habrá ocasiones en las que R tenga éxito y la operación ocurra sin problemas, y otras en las que falle y obtengamos un error. Lo anterior ocurre porque no todos los tipos de datos pueden ser transformados a los demás, para ello se sigue una regla general. La coerción de tipos se realiza de los tipos de datos más restrictivos a los más flexibles. 
Las coerciones ocurren en el siguiente orden.

```
lógico -> entero -> numérico -> cadena de texto 
```

Es decir:
```
(logical -> integer -> numeric -> character)
```

Las coerciones no pueden ocurrir en orden inverso. Podemos coercionar un dato de tipo entero a uno numérico, pero uno de cadena de texto a numérico.

Como los datos de tipo lógico sólo admiten dos valores (TRUE y FALSE), estos son los más restrictivos; mientras que los datos de cadena de texto, al admitir cualquier cantidad y combinación de caracteres, son los más flexibles.

Los factores son un caso particular para la coerción. Dado que son valores numéricos con etiquetas, pueden ser coercionados a tipo numérico y cadena de texto; y los datos numéricos y cadena de texto pueden ser coercionados a factor. Sin embargo, al coercionar un factor tipo numérico, perdemos sus niveles.

### Coerción explícita con la familia as()

También podemos hacer coerciones explícitas usando la familia de funciones as().

| Función	| Tipo al que hace coerción |
| ------- | ------------------------- |
| as.integer()	| Entero |
| as.numeric()	| Numerico |
| as.character()	| Cadena de texto |
| as.factor()	| Factor |
| as.logical()	| Lógico |
| as.null()	| NULL |

Cuando estas funciones tienen éxito en la coerción, nos devuelven datos del tipo pedido. Si fallan, obtenemos NA como resultado.

Por ejemplo, intememos convertir el número 5 a una cadena de texto. Para ello usamos la función ```as.character().

```
as.character(5)
## [1] "5"
```
Esta es una coerción válida, así que tenemos éxito. Pero, si intentamos convertir la palabra “cinco” a un dato numérico, obtendremos una advertencia y NA.

```
as.numeric("cinco")
## Warning: NAs introducidos por coerción
## [1] NA
```
Comprobemos el comportamiento especial de los factores.

Podemos coercionar al número 5 y la palabra “cinco” en un factor.
```
as.factor(5)
## [1] 5
## Levels: 5
```

```
as.factor("cinco")
## [1] cinco
## Levels: cinco
```

Asignamos la palabra “cinco” como factor al objeto factor_cinco.

```
factor_cinco <- as.factor("cinco")
#Resultado
factor_cinco
## [1] cinco
## Levels: cinco
```

Ahora podemos coercionar factor_cinco a cadena de texto y a numérico.

```
# Cadena de texto
as.character(factor_cinco)
## [1] "cinco"
# Numérico
as.numeric(factor_cinco)
## [1] 1
```

Si coercionamos un dato de tipo lógico a numérico, TRUE siempre devolverá 1 y FALSE dará como resultado 0.
```
as.numeric(TRUE)
## [1] 1
as.numeric(FALSE)
## [1] 0
```

Por último, la funcón as.null() siempre devuelve NULL, sin importar el tipo de dato que demos como argumento.
```
# Lógico
as.null(FALSE)
```

```
## NULL
```

```
# Numérico
as.null(457)
```

```
## NULL
```

```
# Cadena de texto
as.null("palabra")
## NULL
```
---

















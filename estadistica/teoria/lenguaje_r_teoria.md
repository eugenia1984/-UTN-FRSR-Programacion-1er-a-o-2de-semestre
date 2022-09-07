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


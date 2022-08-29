# Lenguaje R

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

- Escriba 'license()' o 'licence()' para detalles de distribucion.

- R es un proyecto colaborativo con muchos contribuyentes.

- Escriba 'contributors()' para obtener más información y

- 'citation()' para saber cómo citar R o paquetes de R en publicaciones.

- Escriba 'demo()' para demostraciones, 'help()' para el sistema on-line de ayuda,
o 'help.start()' para abrir el sistema de ayuda HTML con su navegador.

- Escriba 'q()' para salir de R.

---


## Obteniendo ayuda en R

Recuerda que existen dos maneras de obtener ayuda en R. Lo puedes hacer a traves del menu o de la ventana de comandos. 

1. La funcion mean calcula la media aritmetica de una serie de valores. ¿Cuales son los argumentos de dicha funcion? 

2. Dado un conjunto de valores, sabemos que existe una funcion en R que calcula el maximo, pero no recordamos su nombre. ¿Serıas capaz de encontrarla a traves de la ayuda? Recuerda que la ayuda esta en ingles.

3. Queremos utilizar el comando help.search para obtener informacion sobre la funcion plot. El resultado es el siguiente: ```> help.search(plot) Error in help.search(plot) : argument ’pattern’ must be a single character string```
 
¿Por que nos da error? 

¿Como lo escribirıas de forma correcta? 


---

## :star: Ejercicio 1:

1. Define el vector x = (1, 2, 3, 4, 5, 6). 

- A partir de dicho vector se han construido las matrices m1, m2, m3, m4  

- > m1 [,1] [,2] [,3] [1,] 1 3 5 [2,] 2 4 6 - EXPRESAR ESTA MATRIZ

- > m2 [,1] [,2] [1,] 1 4 [2,] 2 5 [3,] 3 6 - EXPRESAR ESTA MATRIZ  

- > m3 [,1] [,2] [,3] [1,] 1 2 3 [2,] 4 5 6 - EXPRESAR ESTA MATRIZ

- > m4 [,1] [,2] [,3] [1,] 1 4 1 [2,] 2 5 2 [3,] 3 6 3 EXPRESAR ESTA MATRIZ

- Todas las matrices se han definido a partir de matrix(x,...). Intenta reproducir el codigo necesario para obtener cada una de ellas. Recuerda que puedes consultar la AYUDA



---

## :star: Ejercicio 2:

- Que ocurre cuando definimos una matriz en R y solo especificamos el numero de filas o el numero de columnas? 

- ¿Que ocurre cuando los datos no se corresponden con la dimension de la matriz que queremos definir? Compruebalo ejecutando los siguientes comandos: 

- >matrix(1:6,nrow=2) 

- >matrix(1:6,nrow=4) 

- >matrix(1:6,nrow=4,ncol=4)



---

## :star: Ejercicio 3:

- ¿Cual es la diferencia entre *, %*% y outer() ?

- Compruebalo con las matrices 

A = 2 3 1 4 (ES DE 2X2)

B =  3 8 (ES DE 1X2)



---

## :star: Ejercicio 4

- Sean A una matriz 2 × 3, B una matriz 3 × 4 y C una matriz 2 × 3.
 
¿De que tipo y dimension seran los objetos obtenidos de los siguientes comandos de R? 

¿Alguno de los comandos produce mensajes de error? 

¿Por que?

a) A*B 

b) outer(A,B) 

c) A+2 

d) A%*%B 

e) exp(B). Nota: exp() es la funcion exponencial. 

f ) A*C 

g) A%*%C



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

- Queremos representar graficamente la funcion coseno en el intervalo [0, 2π]. 

- Para ello creamos el vector x de la siguiente forma: 

x<-seq(0,2*pi,length=100). 

- ¿Cual es la diferencia entre las graficas obtenidas por los siguientes comandos? 

>plot(cos(x)) y >plot(x,cos(x))

- Intenta reproducir en lo posible las siguientes gr´aficas. Si tienes cualquier duda consulta la ayuda de las funciones plot y par.



---

## Tablas de frecuencia y graficos para variables cualitativas![image](https://user-images.githubusercontent.com/72580574/187313382-3c696fc8-4c62-4a17-8fe5-19b49055b599.png)

- Empezamos con las variables cualitativas. Vemos en primer lugar como obtener las frecuencias absolutas de la variable Equipo. Para ello vamos a utilizar las variables del conjunto de datos utilizando el comando attach:

- > attach(datos.alumnos) 

- > Altura 

- > Peso 

- > Hermanos

---

- A continuacion, para obtener las frecuencias absolutas utilizamos la funcion table, como sigue:

- > fabs <-table(Equipo) 

- > fabs 

- Equipo : 
```
BAR CEL DEP NIN RMA VAL 
3    4   13  15   8   1
```

- > class(fabs)


- Las frecuencias relativas las podemos obtener simplemente dividiendo la variable fabs por el numero de individuos de la muestra n.ind:

- > frel<-fabs/n.ind 

- Equipo 
```
BAR               CEL                DEP               NIN               RMA  
0.06818182 0.09090909 0.29545455 0.34090909 0.18181818 
```

- VAL
0.02272727

- Obtenemos ası las frecuencias relativas de cada uno de los equipos de la muestra. Una vez que tenemos estas frecuencias podemos empezar a hacer resumenes graficos para variables cualitativas. Por ejemplo, para hacer un diagrama de barras, podemos escribir:

- > barplot(fabs,ylab="Frecuencias absolutas",main="Diagrama de barras de Equipo")

- Las opciones del gr´afico son m´ultiples y las podemos comprobar utilizando la ayuda:

- > help("barplot")

- Ver que tambien podemos hacer un diagrama de barras de la variable Equipo utilizando las frecuencias relativas: 

- > barplot(frel,ylab="Frecuencias relativas",main="Diagrama de barras de Equipo")




---

## Tablas de frecuencia y graficos para variables cuantitativas: EJERCICIO NRO 1


- Empezamos con las variables cuantitativas discretas. En primer lugar, obtenemos las frecuencias absolutas y relativas de la variable Hermanos, utilizando la funcion table como sigue:

- > fabs<-table(Hermanos) 

- > fabs 

```
Hermanos 1    2    3   4   6 
         8    24   9   2   1
```

- Las frecuencias relativas las podemos obtener simplemente dividiendo la variable fabs por el numero de individuos de la muestra n.ind: 

- > frel<-fabs/n.ind

- > frel Hermanos 
```
1                    2                    3                   4                    6 
0.18181818 0.54545455 0.20454545 0.04545455 0.02272727
```

- Ademas ahora podemos obtener las frecuencias absoluta y relativa acumuladas. Para ello, podemos hacer lo siguiente: 

> fabsacum<-as.table(cumsum(fabs)) 

> fabsacum 
```
1  2    3  4   6 
8  32 41 43 44 
```

> frelacum<-as.table(cumsum(frel)) 

> frelacum 
```
1                  2                 3          4             6 
0.1818182    0.7272727        0.9318182      0.9772727 1.0000000
```  

---
















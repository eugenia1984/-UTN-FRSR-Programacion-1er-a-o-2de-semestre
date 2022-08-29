# Lenguaje R

---

## ¿ Qué es lenguaje R ?

- R es un software creado en 1993 por Robert Gentleman y Ross Ihaka, que respeta la libertad de los usuarios y es similar al lenguaje y entorno S, creado en Bell Laboratories (antes AT&T, ahora Lucent Technologies) por John Chambers y algunos colegas, a finales de los 70.

- Si bien R guarda algunas diferencias importantes respecto a S, gran parte del código escrito para S se ejecuta sin cambios en R. Es por eso que se afirma naturalmente que R viene de S.

- Con el software libre R se puede hacer modelos de regresión lineal y logísticos, análisis de series de tiempo, pruebas estadísticas clásicas, agrupamientos, clustering, clasificaciones y aplicar muchas otras técnicas estadísticas.

- R es la elección perfecta de código abierto para participar en la investigación estadística. R permite producir gráficos de alta calidad con mucha facilidad, incluyendo símbolos matemáticos y fórmulas, siempre que sea necesario.
![image](https://user-images.githubusercontent.com/72580574/187312037-19e71f37-5732-41bd-b9ff-07c86d94e0b1.png)

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

![image](https://user-images.githubusercontent.com/72580574/187312081-525e438e-7093-4fdc-9c88-63c233e2605c.png)

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

![image](https://user-images.githubusercontent.com/72580574/187312142-960302cc-5f1f-40c9-8c0a-65c7c319064e.png)

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

![image](https://user-images.githubusercontent.com/72580574/187312426-3d909547-8717-470b-8d00-c1ae78dabb90.png)

---

## Obteniendo ayuda en R

Recuerda que existen dos maneras de obtener ayuda en R. Lo puedes hacer a traves del menu o de la ventana de comandos. 

1. La funcion mean calcula la media aritmetica de una serie de valores. ¿Cuales son los argumentos de dicha funcion? 

2. Dado un conjunto de valores, sabemos que existe una funcion en R que calcula el maximo, pero no recordamos su nombre. ¿Serıas capaz de encontrarla a traves de la ayuda? Recuerda que la ayuda esta en ingles.

3. Queremos utilizar el comando help.search para obtener informacion sobre la funcion plot. El resultado es el siguiente: ```> help.search(plot) Error in help.search(plot) : argument ’pattern’ must be a single character string```
 
¿Por que nos da error? 

¿Como lo escribirıas de forma correcta? 

![image](https://user-images.githubusercontent.com/72580574/187312505-f3ded73f-c3d7-4c15-a7e0-cdd2f2975119.png)

---

## :star: Ejercicio 1:

1. Define el vector x = (1, 2, 3, 4, 5, 6). 

- A partir de dicho vector se han construido las matrices m1, m2, m3, m4  

- > m1 [,1] [,2] [,3] [1,] 1 3 5 [2,] 2 4 6 - EXPRESAR ESTA MATRIZ

- > m2 [,1] [,2] [1,] 1 4 [2,] 2 5 [3,] 3 6 - EXPRESAR ESTA MATRIZ  

- > m3 [,1] [,2] [,3] [1,] 1 2 3 [2,] 4 5 6 - EXPRESAR ESTA MATRIZ

- > m4 [,1] [,2] [,3] [1,] 1 4 1 [2,] 2 5 2 [3,] 3 6 3 EXPRESAR ESTA MATRIZ

- Todas las matrices se han definido a partir de matrix(x,...). Intenta reproducir el codigo necesario para obtener cada una de ellas. Recuerda que puedes consultar la AYUDA

![image](https://user-images.githubusercontent.com/72580574/187312612-5147f9e4-fa77-494a-b47a-d6328b3dca44.png)

---

## :star: Ejercicio 2:

- Que ocurre cuando definimos una matriz en R y solo especificamos el numero de filas o el numero de columnas? 

- ¿Que ocurre cuando los datos no se corresponden con la dimension de la matriz que queremos definir? Compruebalo ejecutando los siguientes comandos: 

- >matrix(1:6,nrow=2) 

- >matrix(1:6,nrow=4) 

- >matrix(1:6,nrow=4,ncol=4)

![image](https://user-images.githubusercontent.com/72580574/187312699-9e66dc4d-946c-4d38-8997-da6b54ad1121.png)

---

## :star: Ejercicio 3:

- ¿Cual es la diferencia entre *, %*% y outer() ?

- Compruebalo con las matrices 

A = 2 3 1 4 (ES DE 2X2)

B =  3 8 (ES DE 1X2)

![image](https://user-images.githubusercontent.com/72580574/187312756-9d0d9d89-efd9-4de8-8a9a-6febaaf8740d.png)

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

![image](https://user-images.githubusercontent.com/72580574/187312798-1f8ae690-09ee-4a7d-95f7-74da52e999ad.png)

---

## :star: Ejercicio 5:

Un grupo de amigos esta formado por Ana de 23 anos, Luis de 24 anos, Pedro de 22, Juan de 24, Eva de 21 y Jorge de 22 anos. Crea los vectores correspondientes a nombre, edad y sexo.

![image](https://user-images.githubusercontent.com/72580574/187312875-f512f629-7e47-4348-b1dc-12c641b55140.png)

---

## :star: Ejercicio 6

- Con los datos anteriores hemos creado el dataframe amigos. 

- El resultado es: 
```
> amigos nombre edad 
sexo 1 Ana 23 M ;2 Luis 24 H; 3 Pedro 22 H; 4 Juan 24 H ;5 Eva 21 M ;6 Jorge 22 H 
```

¿Cual es el codigo de R da como resultado esta salida?

![image](https://user-images.githubusercontent.com/72580574/187312911-1e07e592-f606-4e61-aeb6-0313134985f6.png)

---











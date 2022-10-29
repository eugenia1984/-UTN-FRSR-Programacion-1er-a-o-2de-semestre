### Clase 8

#### Contexto estatico y Contexto Dinamico

1. Contexto Estatico -> carga de clases

2. Contexto Dinamico -> carga de objetos

Todo lo definido con **static** se asocian a la **class** y no al **object**.


PALABRA STATIC
```
---------------------
 NombreObjeto1                         ------------------------------
---------------------                   NombreClase
+atributoNoEstatico1    -------------> -------------------------------
+atributoNoEstatico2     comparten      +atributoEstatico:
...                      los
---------------------    atributos     -------------------------------
                         y              + metodoEstatico(arg): return
--------------------     metodos
 NombreObjeto2           estaticos      ------------------------------
--------------------    ------------->
+atributoNoEstatico1
+atributoNoEstatico2
...
--------------------- 

```

### Comenzamos con otra practica de HERENCIA

![image](https://user-images.githubusercontent.com/72580574/198844787-df2d2030-2778-4af8-8d86-8c83ab55992d.png)


---

## :star: Clase 9

- Vamos a poner ne codigo el diagrama UML visto en la ultima clase.

-> {aca esta el ejercico en codigo](https://github.com/eugenia1984/UTN-FRSR-Programacion-1year-2semester/tree/main/programacion2/clase7_8_9/Herencia)

---

## :star: POO

#### ¿ Que es ?

¿Sabes en qué consiste exactamente la POO? Es uno de los conceptos más importantes que debes aprender como programador?

La programación es muy amplia y existen muchas formas de programar. Es tan amplia, que a muchas personas les estresa aprender programación. Sin embargo, cada programador tiene un estilo diferente de programar, y en términos generales, a eso se le llama paradigma.

El paradigma con el que nos enseñan a programar, a la mayoría, es secuencial o estructurado. Es decir, las instrucciones van de arriba hacia abajo, una después de la otra. Simplemente damos una orden, luego otra, leemos unos datos, lo manipulamos con alguna operación, ponemos una condicional para validar ese resultado y, según esos resultados, mándanos una cosa u otra. De arriba hacia abajo, así aprendimos todos a programar.

Pero, cuándo empiezas a trabajar con proyectos más grandes, te das cuenta que este paradigma no te ayuda mucho y allí se te complican las cosas. Vamos a poner un ejemplo muy simple: imagina que un cliente te pide una tienda en línea para vender zapatos. ¿Cómo vas a hacer ese programa de arriba hacia abajo? toca pensar de una manera diferente porque tienes ciertas cosas:

Los zapatos, que pueden tener un precio, color, una marca.

Los productos deben poder filtrarse.

Necesitas un carrito que se conecte con las pasarelas de pago para recibir el dinero.

Tienes a los usuarios que van a hacer las compras.

Son muchas cosas que no pueden escribirse de arriba hacia abajo. Y aún así, como es la única manera en la qué sabemos programar, lo hacemos de esa forma. Y cómo también he pasado por allí, sé que es muy difícil cambiar la mentalidad.

### ¿ Cual es le paradigma mas usado ?

El paradigma más usado en el mundo, (no el mejor, porque eso es relativo), es la **programación orientada a objetos (POO)**. Es el más usado porque cada uno de estos elementos que necesita el sistema o la aplicación, como el carrito, el producto, el usuario, entre otros, es un objeto en este paradigma. Estos objetos tienen sus propios datos y su propio comportamiento. 

Por ejemplo:

-> Los **zapatos** son un objeto, y por lo tanto, tienen estas dos propiedades:

- **Datos** (**atributos** / **propiedades**): marca, precio, nombre.

- **Funcionalidad** (**metodos**): pueden ser comprados o agregados al carrito.

-> Los **usuarios** también se dividen igual:

- **Datos** (**atributos**): su nombre, número de tarjeta de crédito.

- **Funcionalidad** (**metodos**): comprar los productos.

-> Lo mismo pasa con el **carrito**:

- **Datos** (**atributos**): productos agregados al carrito o que usuarios están en el carrito.

- **Funcionalidad** (**metodos**): mandar esa orden de compra a la pasarela de pago, para que se procese y recibir el mensaje si el pago fue exitoso.

Cada uno de estos elementos en los que vamos dividiendo el sistema, es un objeto, y los objetos, tienen datos y funcionalidades.

---

- Con la Programación Orientada a Objetos pasamos de tener un código de arriba hacia abajo, en el que las funcionalidades están mezcladas y son difíciles de separar o escalar, a un sistema en el que tenemos los elementos (Objetos) separados y se comunican entre ellos:

- El usuario se comunica con el producto para comprarlo.

- El producto se comunica con el carrito para ser agregado.

- El carrito se comunica con la pasarela de pago y con el usuario.

- De esta manera es más fácil manejar y mantener un sistema y hacerlo crecer. Si luego necesitáramos otra funcionalidad, podemos agregar otro objeto, o incluso, agregarle atributos o funcionalidad a los objetos que ya existen.

---

### Atributos y metodos

Como dije antes, los objetos tienen datos y funcionalidad y en la POO se les llama de esta manera:​

Datos → **Atributos**

Funcionalidad → **Métodos**

Cada objeto tiene sus atributos y sus métodos. Te pondré un caso de vida real para que quede mucho más claro. Estamos programando la aplicación de cursos de una empresa, y queremos crear usuarios, entonces hacemos un proceso llamado abstracción. Significa pensar los atributos y métodos que debería de tener este usuario para la aplicación.

Luego de la reflexión, llegamos a la conclusión de que nuestro usuario debe tener: nombres, apellidos, contraseñas y premium (sería un valor que puede ser verdadero o falso).

A través de este mismo proceso de abstracción, definimos sus métodos: iniciar sesión, cerrar sesión, editar su perfil y contraseña, pasar a premium o publicar un artículo en la comunidad.

---


### Ejemplo con class Usuario

- Atributos:

```
-Nombres
-Apellidos
-Correo
_Contraseña
-Premium
```

- Metodos:

```
-iniciarSesion
-cerrarSesion
-editarPerfil
-cambiarContraseña
-pasarAPremium
-publicarEnComunidad
```

---

Obviamente en el proceso podemos darnos cuenta que necesitamos también del atributo país, género, fecha de nacimiento y los agregamos. Ya tenemos la estructura y los agregamos sin problemas. Estos objetos se crean en código, obviamente, pero te imaginas que, para cada vez que un usuario quiera registrarse a la empresa, ¿llamemos al programador y lo pongamos a escribir código para el usuario? no sería eficiente. Tendríamos una cola de cientos de usuarios esperando que el programador termine con el actual, para pasar al siguiente.

¿Cómo resolvemos este problema? usamos algo llamado clase.

### ¿ Que es una clase ?

La clase es una plantilla, un molde, que tiene esa estructura básica del objeto (atributos: datos y métodos: funcionalidad). En el ejemplo anterior, no creamos realmente el objeto-usuario, creamos la plantilla (la clase). Entonces, cada vez que una persona se registra en la empresa, realmente está usando la clase que ya creamos y que ya está en el código, para crear nuevos objetos (usuarios).

Ese proceso de crear objetos a partir de una plantilla, llamada clase, se llama instanciar. Por eso es que cada uno de esos objetos, también se les llama instancia, y de esa manera, es que, con una sola clase, podemos crear decenas o cientos de usuarios sin tener que escribir código nuevamente. Solamente escribimos una vez la plantilla.

En este punto, debes tener claro, que un objeto tiene datos (atributos) y funcionalidad (métodos ) y que a través de una clase, podemos crear varios objetos. ¿Cómo es el proceso de usar estos objetos en una aplicación real? Te lo mostraré con un ejemplo, para que nunca más tengas dudas.

---




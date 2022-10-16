# :star: Clase 1 * JavaScript (13/09)

---

Temas

- un poco de historia de JavaScript

- instalación de Node.js

- extensiones para VSC

---

## Extensiones de VSC para JavaScript

Las recomendadas son:

- Quokka.js

- Braket Pair Colorizer 2

- ESLint

- Debugger for Chrome
 
- Intelli Code

- Live Server

---


# :star: Clase 2 * JavaScript (20/09)

## Variables

- Para declarar una variable de tipo String:


```JavaScript
let nombre = " Maria Eugenia"
```

- Para mostrar la variable:

```JavaScript
console.log(nombre)
```

- JavaScript es **single threat** (de un solo hilo, no es multihilo).

- El ; es opcional, pero a veces si no se incluye trae inconvenientes.

---



# :star: Clase 3 * JavaScript (27/09)

---

## El metodo alert()

```JavaScript
alert("Bievenidos a las primeras practicas de JavaScript")
```

-> Al verlo en el navegador se va a abrir una ventana como de alerta con el mensaje que le escriba entre los ().

-> Voy a ver un boton de **Aceptar**

---

## Comentarios(sintaxis)

Para los comentarios usamos // si son comentarios en linea y usamos /**/ si eson en más de una linea.

Por ejemplo:

```JavaScript
// comentario en linea

/* comentario
multilinea*/
```

---

## Tipo de datos

### Primitivos

### 1 - String

Puede ir entre comillas dobles o simples, lo que si es que si abro con comillas doble debo cerrar con comillas dobles, no puedo intercambiarlas, debo usar las mismas.

```JavaScript
let name = "Maria Eugenia"
console.log(`La variable de tipo String es: name = ${name}`)
```

### 2 - Number

### Complejos

### 1 - Object

Declaro mi objeto:
```JavaScript
const objetoPersona = {
  firstName: "Maria Eugenia ",
  lastName: "Costa"
}
```

Muestro por consola los values de las keys:
```JavaScript
console.log(`Este es mi objeto objetoPersona.`)
console.log(`Tiene la clave firstName con su valor: ${objetoPersona.firstName} y la clave lastName con su valor ${objetoPersona.lastName}`)
```

---

# :star: Clase 4 * JavaScript (04/10)

### Reutilizar variables

Las variables son dinamicas, se pueden reutilizar.

Lo que hay que tener cuidado es que JavaScript es debilmente tipado, entonces una variable que almacenaba unNumber luego puede almacenar un String, lo que puede traer errores futuros.

Ejemplo:

```JavaScript
let name = "Maria"
console.log(name) // Maria
name = "Eugenia "
console.log(name) // Eugenia
console.log(typeOf(name)) // String
```

---

### Repaso: creación del archivo index.html

En el **index.html** siempre al final, justo antes de cerrar el ```<body>``` voy a tener el **script**:

```HTML
  <script src="./01_hola_mundo.js"></script>
  <script src="./02_alert.js"></script>
</body>
</html>
```

---

### Tipos de datos booleanos, función y Symbol


#### Boolean

Tienen dos posibles valoreS:

- true

- false

```JavaScript
let bandera = true
console.log(`Mi variable boolean bandera, tiene el valor: ${bandera}`)
```

Se usa bastante en los condicionales, por ejemplo:

```JavaScript
if(numero > 2) {
  console.log(numero)
}
```

-> Si el numero es mayor a dos mostrarlo por consola, es decir si la condicion es **true** que lo muestre.


### Funcion

Una funcion e sun bloque de codigo que se puede reutilizar las veces que sea necesaria. ¿Cómo se hace ? Invocandona.

- Function (declarativa)

En este caso debo utilizar la palabra reservada **function**

```JavaSCript
function myFunctionSayHi() {
  console.log("Hi")
}
myFunctionSayHi(); // Hi
```

- Arrow function

```JavaScript
myFunctionSayHi() => console.log("Hi")
```
En este cao tengo un **return explicito** como solo tengo una linea de codigo puedo obviar las **{}** y la palabra reservada **return**, pero el cuerpo de mi arrow function tiene más e una lineade código si debo utilizar las {} y la palabra reservada **return**

Lo mismo los (), cuando no lleva parametros, pueden ser obviados.

- Arrow function con fucnion anonima

```JavaScript
const myFunctionSayHi = () => console.log("Hi")
```

#### Symbol

```JavaScript
const simbolo = Symbol("My Symbol")
console.log(simbolo)
```

- El valor de “Symbol” representa un identificador único.

- Un ejemplo: Un valor de este tipo puede ser creado usando Symbol():

```JavaScript
let id = Symbol();
```

Al crearlo, podemos agregarle una descripción (también llamada symbol name), que será útil en la depuración de código:

```JavaScript
// id es un symbol con la descripción "id"
let id = Symbol("id");
```

Se garantiza que los símbolos son únicos. Aunque declaremos varios Symbols con la misma descripción, éstos tendrán valores distintos. La descripción es solamente una etiqueta que no afecta nada más.

Por ejemplo, aquí hay dos Symbols con la misma descripción… pero no son iguales:

```JavaScript
let id1 = Symbol("id");
let id2 = Symbol("id");

alert(id1 == id2); // false
```

---

### Definir un tipo de clase

**Class** es un azucar sintactico, en realidad JavaScript está basado en **prototipos**


Va a tener su metodos constructor para poder ser definida con sus **atributos** y **metodos**

```JavaScript
class Persona {
  // constructor
  constructor(firstName, lastName) {
    // Atributos
    this.firstName = firstName;
    this.lastName = lastName;
  }
  // Metodos
}
let persona1 = new Persona("Maria Eugenia", "Costa")
console.log(persona1)
```

-> La palabra reservda **this** hace referencia al atributo de a clase, ya que tiene en el parametro y en el atributo el mismo nombre.

---

## :star: Clase 5

---

## Tipo de dato Undefined

Es una variable que fue definida/creada pero que no se le ha asignado un valor.

```JavaScript
let indefinida;
console.log(`Mi variable indefinida: ${indefinida}`)
```


### null

Es la **ausencia de valor**, es una variable vacia, sin asignacion de un tipo de dato.

```JavaScript
let nula = null
```

null no es un tipo de dato, pero es un **object**

---

## Array 

En JavaScript los **arrays** son de tipo **object**.

Se definen entre []

Ejemplo:
```JavaSCript
const cars = ["Citroen", "Audi", "BMW"]
```

Dentro pueden almacenar todo tipo de datos, inclusive de distintos tipos, comom: Number, String, boolean, array, etc.

```JavaSCript
const variado = ["Hola", 1, true]
```


## Empty String

```JavaScript
let vacia = " "
```

---

## Similitudes entre JavaScript y Java


- Son muy pocas las similitudes entre Java y JavaScript

1. Operadores simplificados:
```
+=
-=
*=
/=
```

2. Operadores aritmeticos:
```
+
-
*
%
/
```

3. Operadores de asignacion
```
=
```

4. Operadores de comparacion:
```
==
```

Pero recordar que JavaScript también tiene el estricto ```====```

5. Comentarios:
```
// Comentario de una sola linea
/* Comentario
multilena*/
```

6. Secuencias de escape:
```
\' muestra una comilla simple dentro de una cadena
\" muestra una comilla doble dentro de una cadena
\\ muestra una barra invertida (back slash) dentro de una cadena
\n para un salto de linea
\r retorno
\t tabulacion
\b retroceso
\f salto de pagina
```

7. Operador de aumento (```++```) y   Operador de decremento (```--```)

---
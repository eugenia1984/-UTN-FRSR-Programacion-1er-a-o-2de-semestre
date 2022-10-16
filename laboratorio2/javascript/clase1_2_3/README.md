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

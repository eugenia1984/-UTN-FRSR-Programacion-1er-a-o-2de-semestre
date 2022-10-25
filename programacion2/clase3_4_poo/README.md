## :star:  POO

---

## ¿Que es un objeto ?

En el mundo real, las personas identifican los objetos como cosas que pueden ser percibidas por los cinco sentidos.

Los objetos tienen **propiedades** especificas, tales como posicion, tamaño, color, forma, textura, etc., que definen su estado. Los objetos tambien tienen ciertos **comportamientos** que los hacen diferentes a otros objetos (son los **metodos**).

### Ejemplo de una clase Auto


- Atributos (caracteristicas):
```
> color: "Plateado"
> marca: "audi"
> km: "0Km"
```

- Métodos (acciones):
```
> encender()
> acelerar()
> frenar()
```

### Otro ejemplo:

3 / 2

- Atributos (caracteristicas):
```
> numerador: 3
> denominador : 2
```

- Metodos (acciones):
```
> simplificar()
> sumarseConOtraFraccion()
> restarseConOtraFraccion()
```

---

## ¿Que es una clase ?

Una clase es un conjunto de objetos que comparten uan estructura y comportamientos comunes.

-> Volviendo con el ejemplo de la **class Auto**:

```
miCoche1

------------------
Atributos
------------------
> color: "Rojo"
> marca: "Ferrari"
> km: "0Km"

------------------
Metodos
------------------
> encender()
> acelerar()
```


```
miCoche2

------------------
Atributos
------------------
> color: "Negro"
> marca: "Audi"
> km: "0Km"

------------------
Metodos
------------------
> encender()
> acelerar()
```


**La class Coche**:
```
-------------------
Coche
------------------
> color
> marca
> km:
------------------
Metodos
------------------
> encender()
> acelerar()
> frenar()
```

---

### Diagrama general de una clase Java

```
--------------------------
   Persona                     <---- nombre de la clase
---------------------------
-nombre: String
-genero: char                  <------- atributos
-ocupacion: String
--------------------------
+obtenerNombre(): String
+obtenerGenero(): String
+obtenerOcupacion(): String     <------ metodos
+modificarNombre(nombre: String)
+modificarGenero(genero: String)
+modificarOcupacion(ocupacion: String)
--------------------------
```

---

### Inroduccion a las clases y objetos en Java

- Una **clase** es una **plantilla** (como un molde de tortas)

```
   Persona (class) -posee atributos y metodos-
   |         |
   v         v
 Karla     Armando
(objeto)   (objeto)
```

- Un **objeto** es una **instancia de una clase**
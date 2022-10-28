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

---

### Metodo constructor

- Contruye un objeto.

- Reserva un espacio de memoria.

- Inicializa los atributos de la clase.

---

### Sobrecarga de metodos

Como cuando tenemos varios metodos contructores, que varian por los parametros que reciben y mantienen el mismo nombre(que es el mismo nombre que el de la clase).

-> Está el constructor vacío (que no recibe parametros)

-> Estan los constructores con prametros (los parametros son los atributos de la funcion). 


#### Ejemplo en codigo:

```Java
package operaciones;
/**
 * @author Maria Eugenia Costa
 */
public class Aritmetica {
    // Atributos de la clase
    int numero1;
    int numero2;
        
    // constructor vacio
    public Aritmetica() {
        System.out.println("Se esta ejecutando el constructor numero uno");
    }
    // Constructor con parametros
    public Aritmetica(int numero1, int numero2) {
        this.numero1 = numero1;
        this.numero2 = numero2;
        System.out.println("Se esta ejecutando el contructor numero dos");
    }
    
    // Metodo sin retorno
    public void sumarNumeros() {
        int resultado = numero1 + numero2;
        System.out.println("Resultado: " + resultado);
    }
    
    // Metodo con retorno
    public int sumarConRetorno() {
        // int resultado = numero1 + numero2;
        //return resultado;
        return numero1 + numero2;
    }
    
    // Paso de argumentos a un metodo
    public int sumarConArgumentos(int arg1, int arg2) {
        return arg1 + arg2;
    }
    
    //  Un método llamando a otro método
    public int sumarLllamandoAOtroMetodo(int arg1, int arg2) {
        numero1 = arg1;
        numero2 = arg2;
        return sumarConRetorno();
    }
}
```

### Alcance de variables

```Java
public Aritmetica(int numero1, int numero2) {
       this.numero1 = numero1;
       this.numero2 = numero2;
       System.out.println("Se esta ejecutando el contructor numero dos");
   }
```

Las variables **numero1** y **numero2** son parametros que se reciben en la funcion, por mas que tiene el mismo nombre no son los argumentos, por eso para setear esos valores a los argumentos es que utilizamos el **this** para decirle esta variable que me llega como argumento va a dar el valor al atributo.

-> El alcance de la variable esta dentro del metodo que se definio, en el caso de las variables dentro de los metodos

-> Hay variables locales, cuando creamos en el main, se declaran al principio y se pueden utilizar durante todo el programa. (en realidad serian las globales, pero el profesor le puso local, esta mal, encima usa var en vez de aclarar el tipo de dato, sigue con la inferencia de tipo -al menos aclaro que var no se usa dentro del metodo cuando se declara el parametro-).

-> En el mismo main, al cerrarlo, debajo podemos crear nuevos metodos con el acceso **public**.

```Java
package Operaciones;

/**
 * @author Maria Eugenia Costa
 */
public class PruebaAritmetica {

    public static void main(String[] args) {
        // instancio el metodo fuera del main
        miMetodo();
    }
    
    // Metodo fuera del main, siendo public lo puedo invocar
    public static void miMetodo() {
        int numero1 = 10; // esa variable es local del metodo
        System.out.println("Aqui hay otro metodo");
    }
    
}
```

---

### Ingineer Java: Memoria stack y heap

Stack/heap es una clasificacion de la memoria.

-> **stack** son las variables locales, solo almacena la referencia del objeto.

-> **hep** para los atributos y objetos.

La memoria trabaja de manera dinamica.

En Java no se utiliza asignarle un valor null a una variable. Se suele hacer para que la memoria quede limpia, peor en realidad Java tiene el **garbage collector**, por lo que no es necesario esto.

Hay un metodo para limpiar:

```Java
System.gc();
```

gc -> garbage collector

es un metodo sin parametros

---

### Paso por valor

-> Creo el ejercicio en el paquete **PasoPorValorReferencia**

```Java
package pasoporvalorreferencia;

public class PasoPorValorReferencia {


    public static void main(String[] args) {
        int valorX = 20;
        System.out.println("ValorX: " + valorX); // ValorX: 20
        cambioValor(valorX); // solo le enviamos una copia
        System.out.println("ValorX: " + valorX); // ValorX: 20
    }
    
    public static void cambioValor(int arg1) {
        System.out.println("arg1: " + arg1);
    }
    
}

```

### Paso por referencia

```Java
package pasoporvalorreferencia;

public class PasoPorValorReferencia {


    public static void main(String[] args) {
        int valorX = 20;
        System.out.println("ValorX: " + valorX); // ValorX: 20
        cambioValor(valorX); // solo le enviamos una copia
        System.out.println("ValorX: " + valorX); // ValorX: 20
        
        Persona persona1 = new Persona();
        persona1.nombre = "Ana";
        System.out.println("persona1 - nombre: " + persona1.nombre); // Ana
        cambiarValor(persona1);
        System.out.println("persona1 - nombre: " + persona1.nombre); // Maria
    }    
    
    // Paso por valor
    public static void cambioValor(int arg1) {
        System.out.println("arg1: " + arg1);
    }
    
    // paso por referencia
    public static void cambiarValor(Persona persona) { // para metro por referencia
        persona.nombre = "Maria";
    }
    
}
```

---

## null y return

```Java
// Return
    public static Persona cambiarElValor(Persona persona) {
        if(persona == null) {
            System.out.println("Valor invalido");
            return null;
        } else {
            persona.nombre = "Monica";
        return persona;
        }
    }
 ```
 
 ---
 
 ## :star: Clase 7
 
 ### Usando la palabra this
 
 ```Java
 public class Persona {
    String nombre;
    String apellido;
        
    Persona(String nombre, String apellido) { // Constructor
        this.nombre = nombre;
        this.apellido = apellido;
        System.out.println("Objeto persona usando this: " + this);
    }
}
```

### Clase Object

```Java
public class Persona {
    String nombre;
    String apellido;
        
    Persona(String nombre, String apellido) { // Constructor
        //Llamada al constructor de la clase padre Object
        // super(); 
        this.nombre = nombre;
        this.apellido = apellido;
        System.out.println("Objeto persona usando this: " + this);
    }
}
```


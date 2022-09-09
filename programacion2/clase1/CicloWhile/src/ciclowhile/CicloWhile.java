package ciclowhile;

import java.util.Scanner;
import java.lang.Math;

public class CicloWhile {


    public static void main(String[] args) {
        Scanner read = new Scanner(System.in);
        
        System.out.println("---- CLASE 1 ---- \n---CICLO WHILE ---");
        int conteo = 0;
        while (conteo <7) {
            System.out.println("conteo = "+ conteo);
            conteo++;
        }
        System.out.println("--- CICLO DO WHILE ---");
        // A diferencia de lWhile el Do siempre se va a ejecutar al menos 
        // una vez ya que comprueba al final
        // En el Do While al final debo tenr el ;
        int contador = 0;
        do {
            System.out.println("contador = "+ contador);
            contador++;
        } while (contador < 7);
        System.out.println("--- CICLO FOR ---");
        // la variable contador / iterador
        // la condicion a cumplir, que en un momento deja de cumplir para cortar el ciclo
        // como se va a modificar la variable en cada iteracion
        for (int i = 0; i < 7; i++) {
            System.out.println("i = " + i);
        }
         System.out.println("--- CICLO FOR ---");
        for (int index = 0; index < 7; index++) {
            if (index % 2 == 0) {
                System.out.println("index = " + index);
            }
            
        }
        // BREAK para interrumpir el ciclo y salir de el
        // CONTINUE va a pasar a la proxima iteracion, no sale del ciclo
        /*
        EJERCICIO 1
        Leer un numero y mostrar su cuadrado, repetir el proceso hasta 
        que se introduzca un numero negativo
        */
        int numeroIngresado;
        int cuadradoDelNumero = 0;
        
        do {
            System.out.println("Ingrese un numero: ");
            numeroIngresado = read.nextInt();
            if (numeroIngresado > 0) {
                cuadradoDelNumero = numeroIngresado * numeroIngresado;
                System.out.println("El cuadrado es: " + numeroIngresado);
            }  else {
                System.out.println("Ingresaste el 0 o un numero negativo");
            }
            
        } while(numeroIngresado < 0);
        // otro modo de hacerlo es con la Clase Math y su metodo sqrt
        //cuadradoDelNumero = Math.sqrt(numeroIngresado);
        /*
        EJERCICIO 2
        Leer un numero e indicar s es positivo o negativo.
        El proceso se repetira hasta que se introduzca un cero.
        */
        int numeroIntroducido;
        do {
            System.out.println("Ingrese un numero: ");
            numeroIntroducido = read.nextInt();
            if (numeroIntroducido > 0) {
                System.out.println("Es un numero POSITIVO");
            } else if (numeroIntroducido < 0) {
                System.out.println("Es un numero NEGATIVO");
            } else {
                System.out.println("Ingresaste el 0");
            }
            
        } while(numeroIntroducido != 0);
        
        /*
        EJERCICIO 3
        Leer numeros hasta que se introduzca un 0.
        Por cada uno indicar si es par o impar.
        Primero con Scanner.
        Luego con JOptionPane
        */
        int numeroIntroducido2;
        do {
            System.out.println("Ingrese un numero: ");
            numeroIntroducido2 = read.nextInt();
            if (numeroIntroducido2 == 0) {
                System.out.println("Ingresaste el 0");
            } else if (numeroIntroducido2 % 2 == 0) {
                System.out.println("Es un numero PAR");
            } else {
                System.out.println("Es un numero IMPAR");
            }
            
        } while(numeroIntroducido2 != 0);
    }
    
}

package ciclowhile;

import java.util.Scanner;
import java.util.Random;

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
        /*
        EJERCICIO 4
        Pedir numeros hasta que se introduzca uno negativo y mostrar
        cuantos numeros se han introducido
        */
        int numeroIntroducido3;
        int contador3 = 0;
        
        do {
            System.out.println("Ingrese un numero: ");
            numeroIntroducido3 = read.nextInt();
            if (numeroIntroducido3 >= 0) {
                contador3++;
            } 
            
        } while(numeroIntroducido3 > 0);
        System.out.println("Se han indocido: " + contador3 + " numeros positivos.");
        /*
        EJERCICIO 5
        Realizar un juego para adivinar un numero, para ello generar
        un numero aleatorio entre 0 y 100 y luego ir pidiendo numeros 
        indicando "es mayor" o "es menor" segun sea mayor o menor
        con respecto a N.
        El proceso termina cuando el usuario acierta y mostramos
        el numero de intentos hechos
        */
        int numeroAleatorio = 0;
        int entrada = 0;
        Random rd = new Random();
        numeroAleatorio = rd.nextInt(101);
        System.out.print("Se ha generado un numero aleatorio entre 1 y 100. Intente adivinarlo: ");
         while (numeroAleatorio != (entrada = read.nextInt())){
             if (entrada < numeroAleatorio)
                 System.out.print("No has acertado, el número es mayor. Prueba otra vez: ");
             else
                 System.out.print("No has acertado, el número es menor. Prueba otra vez: ");
         }
         System.out.println("LO HAS ADIVINADO");
         
         // EJERCICIO 6
         // Ingresar numeros y sumarlos hasta ingresar 0
            int numero = 1;
            int suma = 0;
            do {
                System.out.println("Ingrese un numero: ");
                numero = read.nextInt();
                suma+= numero;
            } while (numero != 0);

            System.out.println("La suma de todos los numeros ingresados es: " + suma);
        
            // EJERCICIO 7
            // Pedir numeros hasta que se ingrese uno negativo y calcular la media
            int numero2 = 0;
            int conteo2 = 0;
            int suma2 = 0;
            float promedio2 = 0;
            
            System.out.println("Ingrese un numero: ");
            while(numero2 >= 0) { // Mientras el numeor no sea negativo
                suma2 += numero2;
                conteo2++;
                numero2 = read.nextInt();
            }
            if(conteo == 0) {
                System.out.println("Error, la division entre 0 no existe");
            } else {
                promedio2 = (float) suma2/conteo2;
                System.out.println("El promedio es: " + promedio2);
            }
            
            // EJERCICIO 8
            // Pedir un numero N y mostrar todos los numeros del 1 al N
            System.out.println("Ingrese un numero: ");
            int numero3 = read.nextInt();
            int i = 1;
            while( i <= numero3 ) {
                System.out.println(i);
                i++;
            }
                    
            // EJERICICO 9
            // Pedir el dia, mes y año y una fecha e indicar
            // si la fecha es correcta
            // Suponiendo que todos los meses son de 30 dias
            System.out.println("Ingrese un dia (en numeros): ");
            int dia = read.nextInt();
            System.out.println("Ingrese el mes (en numero): ");
            int mes = read.nextInt();
            System.out.println("Ingrese el año: ");
            int anio = read.nextInt();
            if(dia != 0 && dia <= 30) {
                if(mes != 0 && mes <= 12) {
                    if(anio != 0 && anio <= 2022) {
                        System.out.println("La fecha ingresada es: "+dia+"/"+mes+"/"+anio);
                    } else {
                        System.out.println("FEcha incorrecta. Año incorrecto");}
                } else {
                    System.out.println("Fecha incorrecta. Mes incorrecto.");
                }            
            } else {
                System.out.println("Fecha incorrecta. Dia incorrecto");
            }
    }
    
}

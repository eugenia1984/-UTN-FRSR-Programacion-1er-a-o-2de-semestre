package ciclowhile;

public class CicloWhile {


    public static void main(String[] args) {
        System.out.println("---- CLASE 1 ---- \n---CICLO WHILE ---");
        int conteo = 0;
        while (conteo <7) {
            System.out.println("conteo = "+ conteo);
            conteo++;
        }
        System.out.println("--- CICLO DO WHILE ---");
        // A diferencia dl lWhile el Do siempre se va a ejecutar al menos 
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
        // BREAk para interrumpir el ciclo y salir de el
        // CONTINUE va a pasar a la proxima iteracion, no sale del ciclo
    }
    
}

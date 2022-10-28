package proyectocaja;

public class ProyectoCaja {

    public static void main(String[] args) {
        // valores harcodeados
        int medidaAncho = 3;
        int medidaAlto = 2;
        int medidaProfundidad = 6;
        int volumen = 0; // en esta variable calculare el volumen
        
        // Instancio un objeto de la clase Caja con el constructor vacio
        Caja caja1 = new Caja();
        // Le asigno los valores a los atributos
        caja1.alto = medidaAlto;
        caja1.ancho = medidaAncho;
        caja1.profundidad = medidaProfundidad;
        // Invoco el metodo para calcular el volumen y lo asigno a una variable
        volumen = caja1.calcularVolumen();
        // Lo muestro en consola
        System.out.println("El volumen de una caja de: "+medidaAncho+" de ancho, "+
                medidaAlto+" de alto y "+medidaProfundidad+" de profundidad, es: "+
                volumen);
        
        // Isntancio un nuevo objeto con el contructor que recibe argumentos
        Caja caja2 = new Caja(2, 4, 6);
        System.out.println("El volumen de una caja de 2 x 4 x 6 es: "+
                caja2.calcularVolumen());
    }
    
}

/**
 *
 * @author juan
 */
public class PruebaPersona {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // Instancio un objeto de la clase Persona
        Persona persona1 = new Persona();
        persona1.nombre = "Maria Eugania";
        persona1.apellido = "Costa";
        persona1.obtenerInformacion();
        
        // instancio un nuevo objeto de la clase Persona
        Persona persona2 = new Persona();
        persona2.obtenerInformacion(); // Me da todo null porque no le asigne valores a los atributos
        System.out.println("persona2: " + persona2); // veo el espacio en memoria que ocupa
        System.out.println("persona1: " + persona1);
    }
    
}

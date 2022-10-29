
package domain;

public class PersonaPrueba {

    public static void main(String[] args) {
        // insancio un objeto de la clase Persona
        Persona persona1 = new Persona("Marta");
        System.out.println("persona1 -> " + persona1);
        // instancio otro objeto de la clase Persona
        Persona persona2 = new Persona("Sandra");
        System.out.println("persona2 -> " + persona2);
    }
    
    public void imprimir(Persona persona) {
        System.out.println("");
    }
    
}

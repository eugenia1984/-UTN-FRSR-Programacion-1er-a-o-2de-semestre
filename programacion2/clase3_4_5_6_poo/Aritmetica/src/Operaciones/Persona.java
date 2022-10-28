package Operaciones;


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

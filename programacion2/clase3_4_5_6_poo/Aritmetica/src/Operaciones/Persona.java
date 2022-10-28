package Operaciones;


public class Persona {
    String nombre;
    String apellido;
        
    Persona(String nombre, String apellido) { // Constructor
        //Llamada al constructor de la clase padre Object
        super(); 
        
        Imprimir imprimir = new Imprimir();
        // new Imprimir().imprimir(this)
        this.nombre = nombre;
        this.apellido = apellido;
        System.out.println("Objeto persona usando this: " + this);
    }
}

class Imprimir {
    public Imprimir() {
        super(); // el constructor de la clase padre para reservar memoria
    }
}

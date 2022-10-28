
package encapsulamiento;

public class Encapsulamiento {

    public static void main(String[] args) {
        // Crear un objeto del tipo persona 
        // Asignar valores de manera inicial e imprimir
        Persona persona = new Persona("Carlos", 180000.00, true);
        persona.toString();
        // Luego modificar sus valores 
        persona.setNombre("Gustavo");
        persona.setSueldo(190000.00);
        persona.setEliminado(false);
        // y volver a imprimir
        persona.toString();
        
    }
    
}

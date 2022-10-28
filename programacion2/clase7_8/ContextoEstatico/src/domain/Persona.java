
package domain;


public class Persona {
    // Properties
    private int idPersona;
    private static int contadorPersona;
    private String nombre;
    
    // constructores
    public Persona() {
    }

    public Persona(String nombre) {
        this.nombre = nombre;
        // incrementamos el contador por cada objeto nuevo
        Persona.contadorPersona++;
        // asignamos un nuevo valor a la variable idPersona
        this.idPersona = Persona.contadorPersona;
    }
    // getters y setters
    public int getIdPersona() {
        return idPersona;
    }

    public void setIdPersona(int idPersona) {
        this.idPersona = idPersona;
    }

    public static int getContadorPersona() {
        return contadorPersona;
    }

    public static void setContadorPersona(int contadorPersona) {
        Persona.contadorPersona = contadorPersona;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }
    // toString

    @Override
    public String toString() {
        return "Persona{" + "idPersona = " + idPersona + ", nombre = " + 
            nombre + '}';
    }
    
    
    
}

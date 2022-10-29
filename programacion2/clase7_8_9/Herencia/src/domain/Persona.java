
package domain;


public class Persona {
    // Atributos
    protected String nombre;
    protected char genero;
    protected int edad;
    protected String direccion;
    
    // Constructor vacio, para crear el objeto 
    // sin inicializar los atributos de la clase
    public Persona() {}
    // constructor con inicializacion de atributos
    public Persona(String nombre, char genero, int edad, String direccion) {
        this.nombre = nombre;
        this.genero = genero;
        this.edad = edad;
        this.direccion = direccion;
    }
    // Sobrecarga de metodos
    // constructor que solo inicializa el nomnre
    public Persona (String nombre) {
        this.nombre = nombre;
    }
    // getters y setters
    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public char getGenero() {
        return genero;
    }

    public void setGenero(char genero) {
        this.genero = genero;
    }

    public int getEdad() {
        return edad;
    }

    public void setEdad(int edad) {
        this.edad = edad;
    }

    public String getDireccion() {
        return direccion;
    }

    public void setDireccion(String direccion) {
        this.direccion = direccion;
    }
    // ToString
    @Override
    public String toString() {
        return "Persona{" + "nombre = " + nombre + ", genero = " + genero +
            ", edad = " + edad + ", direccion = " + direccion +'}';
    }
    
    
}

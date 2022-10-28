package proyectocaja;


public class Caja {
    // Atributos (propiedades)
    int ancho;
    int alto;
    int profundidad;
    // Metodos y constructores
    // constructor vacio
    public Caja() {
    }
    // Constructor con parametros
    public Caja( int ancho, int alto, int profundidad) {
        this.ancho = ancho;
        this.alto = alto;
        this.profundidad = profundidad;
    }
    // Metodo para calcular el volumen
    public int calcularVolumen() {
        return ancho * alto * profundidad;
    }
    
}

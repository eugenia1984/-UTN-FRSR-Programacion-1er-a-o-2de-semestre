
package domain;


public class Empleado extends Persona { // va a ser clase hija de Persona (hereda)
    private int idEmpleado;
    private double sueldo;
    private static int contadorEmpleados; // para incrementar
    
    // constructor

    public Empleado(String nombre, double sueldo) { // para instanciar solo con el nombre y sueldo
        super(nombre); 
        this.idEmpleado = ++contadorEmpleados; // setteo el idEmpleado
        this.sueldo = sueldo;
    }
    // getters y setters
    public int getIdEmpleado() {
        return idEmpleado;
    }
    // el setter del isEmpleado lo hago en el constructor

    public double getSueldo() {
        return sueldo;
    }

    public void setSueldo(double sueldo) {
        this.sueldo = sueldo;
    }
    // toString

    @Override
    public String toString() {
        return "Empleado{" + "idEmpleado = " + idEmpleado + ", sueldo = " + 
            sueldo + super.toString() + '}';
    }
    
    
}

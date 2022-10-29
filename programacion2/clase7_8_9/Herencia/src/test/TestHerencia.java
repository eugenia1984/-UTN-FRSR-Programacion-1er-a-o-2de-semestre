
package test;

import domain.Cliente;
import domain.Empleado; // importo para poder usar la class Empleado
import java.util.Date;

public class TestHerencia {
    public static void main(String[] args) {
        // Instancio un objeto de la clase Empleado
        Empleado empleado1 = new Empleado("Maria", 140000);
        System.out.println("empleado1 : " + empleado1);
        // instancio un objeto de la clase cliente
        Cliente cliente1 = new Cliente(new Date(), true, "bety", 'F', 32, "9 de Julio 1413");
        System.out.println("cliente1 : " + cliente1);
    }
}

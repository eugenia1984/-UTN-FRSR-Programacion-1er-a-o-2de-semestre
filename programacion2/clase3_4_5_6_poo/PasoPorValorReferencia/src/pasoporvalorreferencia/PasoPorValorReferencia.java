package pasoporvalorreferencia;

public class PasoPorValorReferencia {


    public static void main(String[] args) {
        int valorX = 20;
        System.out.println("ValorX: " + valorX); // ValorX: 20
        cambioValor(valorX); // solo le enviamos una copia
        System.out.println("ValorX: " + valorX); // ValorX: 20
        
        Persona persona1 = new Persona();
        persona1.nombre = "Ana";
        System.out.println("persona1 - nombre: " + persona1.nombre);
        cambiarValor(persona1);
        System.out.println("persona1 - nombre: " + persona1.nombre);
    }    
    
    // Paso por valor
    public static void cambioValor(int arg1) {
        System.out.println("arg1: " + arg1);
    }
    
    // paso por referencia
    public static void cambiarValor(Persona persona) { // para metro por referencia
        persona.nombre = "Maria";
    }
    
}

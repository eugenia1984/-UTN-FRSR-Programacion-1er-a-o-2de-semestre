package pasoporvalorreferencia;

public class PasoPorValorReferencia {


    public static void main(String[] args) {
        int valorX = 20;
        System.out.println("ValorX: " + valorX); // ValorX: 20
        cambioValor(valorX); // solo le enviamos una copia
        System.out.println("ValorX: " + valorX); // ValorX: 20
        
        Persona persona1 = new Persona();
        persona1.nombre = "Ana";
        System.out.println("persona1 - nombre: " + persona1.nombre); // Ana
        cambiarValor(persona1);
        System.out.println("persona1 - nombre: " + persona1.nombre); // Maria
        // pruebo que el null funcione
        Persona persona2 = null;
        persona2 = cambiarElValor(persona2);
        System.out.println("El nuevo valor de persona2 es: " + persona2.nombre);
    }    
    
    // Paso por valor
    public static void cambioValor(int arg1) {
        System.out.println("arg1: " + arg1);
    }
    
    // paso por referencia
    public static void cambiarValor(Persona persona) { // para metro por referencia
        persona.nombre = "Maria";
    }
    // Return
    public static Persona cambiarElValor(Persona persona) {
        if(persona == null) {
            System.out.println("Valor invalido");
            return null;
        } else {
            persona.nombre = "Monica";
        return persona;
        }
    }
    
}

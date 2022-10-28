package Operaciones;

/**
 * @author Maria Eugenia Costa
 */
public class PruebaAritmetica {

    public static void main(String[] args) {
        // instancio el metodo fuera del main
        miMetodo();
        // instancio un objeto de la clase Aritmetica
        Aritmetica aritmetica1 = new Aritmetica();
        aritmetica1.numero1 = 3;
        aritmetica1.numero2 = 7;
        aritmetica1.sumarNumeros();
        
        // utilizo el metodo que tiene retorno y lo guardo en una variable
        int resultado = aritmetica1.sumarConRetorno();
        System.out.println("Resultado de sumarConRetorno es: " + resultado);
    
        // Paso de argumentos a un metodo
        int resultadoConArgumentos = aritmetica1.sumarConArgumentos(2, 3);
        System.out.println("Resultado de sumarConARgumentos(2,3) es: " + 
                resultadoConArgumentos);
        
        //  Un método llamando a otro método
        int resultadoLlmanadoAOtroMetodo = aritmetica1.sumarLllamandoAOtroMetodo(5, 7);
        System.out.println("El resultado de la suma invocando a otro metodo que suma es: " +
                resultadoLlmanadoAOtroMetodo);
        
        // Instancio un nuevo objeto de la clase Aritmetica utilizando 
        //el constructor con los 2 parametros
        Aritmetica aritmetica2 = new Aritmetica(5, 8);
        System.out.println("aritmetica2 - primer atributo :" +aritmetica2.numero1); // 5
        System.out.println("aritmetica2 - srgundo atributo: "+aritmetica2.numero2); // 8
    }
    
    // Metodo fuera del main, siendo public lo puedo invocar
    public static void miMetodo() {
        int numero1 = 10; // esa variable es local del metodo
        System.out.println("Aqui hay otro metodo");
    }
    
}

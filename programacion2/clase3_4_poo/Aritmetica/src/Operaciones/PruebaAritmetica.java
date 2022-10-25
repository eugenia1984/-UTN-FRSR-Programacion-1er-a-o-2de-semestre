package Operaciones;

/**
 * @author Maria Eugenia Costa
 */
public class PruebaAritmetica {

    public static void main(String[] args) {
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
    }
    
}

package Operaciones;
/**
 * @author Maria Eugenia Costa
 */
public class Aritmetica {
    // Atributos de la clase
    int numero1;
    int numero2;
        
    // constructor vacio
    public Aritmetica() {
        System.out.println("Se esta ejecutando el constructor numero uno");
    }
    // Constructor con parametros
    public Aritmetica(int numero1, int numero2) {
        this.numero1 = numero1;
        this.numero2 = numero2;
        System.out.println("Se esta ejecutando el contructor numero dos");
    }
    
    // Metodo sin retorno
    public void sumarNumeros() {
        int resultado = numero1 + numero2;
        System.out.println("Resultado: " + resultado);
    }
    
    // Metodo con retorno
    public int sumarConRetorno() {
        // int resultado = numero1 + numero2;
        //return resultado;
        return numero1 + numero2;
    }
    
    // Paso de argumentos a un metodo
    public int sumarConArgumentos(int arg1, int arg2) {
        return arg1 + arg2;
    }
    
    //  Un método llamando a otro método
    public int sumarLllamandoAOtroMetodo(int arg1, int arg2) {
        numero1 = arg1;
        numero2 = arg2;
        return sumarConRetorno();
    }
}

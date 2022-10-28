package pasoporvalorreferencia;

public class PasoPorValorReferencia {


    public static void main(String[] args) {
        int valorX = 20;
        System.out.println("ValorX: " + valorX);
        cambioValor(valorX); // solo le enviamos una copia
        System.out.println("ValorX: " + valorX);
    }
    
    public static void cambioValor(int arg1) {
        System.out.println("arg1: " + arg1);
    }
    
}

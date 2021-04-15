// Fig. 2.1: Bienvenido1.java
// Programa para imprimir texto.
import java.util.Scanner;

public class Learn_//Java
{
    // el método main empieza la ejecución de la aplicación en Java
    public static void main(String[] args)
    {
        Scanner entrada = new Scanner(System.in);

        int numero1;
        int numero2;
        int suma;

        System.out.print("Escriba el primer entero: ");
        numero1 = entrada.nextInt();
        
        System.out.print("Escriba el segundo entero: ");
        numero2 = entrada.nextInt();

        suma = numero1 + numero2;

        System.out.printf("La suma es %d%n", suma);
    } // fin del método main
} // fin de la clase Bienvenido1
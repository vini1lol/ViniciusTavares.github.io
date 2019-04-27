
package bascara;

import java.util.Scanner;

public class Bascara {

   
    public static void main(String[] args) {
        Scanner sc =  new Scanner(System.in);
        String s;
        do{
        System.out.println("digite o valor de a/b/c em ordem para resolucao de bascara");
        double a = sc.nextFloat();
        double b = sc.nextFloat();
        double c = sc.nextFloat();
        double del = Formula.delta(a, b, c);
        if(a == 0){
            System.out.println(" n possui resultado");
        }else if(del > 0){
            System.out.println("possui duas solucoes distintas"); 
            double resul1 = Formula.posi(del, a, b);
            System.out.println("o primeiro resultado e: "+resul1);
            double resul2 = Formula.nega(del, a, b);
            System.out.println("o segundo resultado e: "+resul2);
        }
        else if(del == 0){
            System.out.println("possui uma solucao");
            double resul = Formula.posi(del, a, b);
            System.out.println("o resultado e: "+resul);
        }
        else if(del < 0){
            System.out.println("nao possui solucao real");
        }
        System.out.println("gostaria de resolver outra equacao?\tsim ou nao");
        s = sc.next();
        }while(s.equals("sim"));
    }
    
}

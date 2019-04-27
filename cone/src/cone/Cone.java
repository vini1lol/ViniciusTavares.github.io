
package cone;

import java.util.Scanner;


public class Cone {

    
    public static void main(String[] args) {
        
        Scanner sc =  new Scanner(System.in);
        String s;
        float r; float R; float h;
        do{
            do{
                System.out.println("digite o raio maior: ");
                R = sc.nextFloat();
                if(R<=0){
                    System.out.println("valor invalido");
                }
            }while(R<0);
            do{
                System.out.println("digite o raio menor: ");
                r = sc.nextFloat();
                if(r<=0){
                    System.out.println("valor invalido");
                }
            }while(r<0);
            do{
                System.out.println("digite a altura do tronco de cone: ");
                h = sc.nextFloat();
                if(h<=0){
                    System.out.println("valor invalido");
                }
            }while(h<0);
            System.out.println("a area da superficie e:"+calc.area(R, r, h)+" e o volume do tronco de cone e: "+calc.volume(R, r, h));
            System.out.println("gostaria de fazer outro calculo?\tsim ou nao");
            s=sc.next();
            }while(s.equals("sim"));
    }
    
}

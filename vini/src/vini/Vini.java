
package vini;

import java.util.Scanner;
import javax.swing.JOptionPane;


public class Vini {


    public static void main(String[] args) {
        String j = "n a nada para imprimri";
        Scanner sc = new Scanner(System.in);
        JOptionPane.showInputDialog("ola! bom dia! Deseja imprimir algo?se sim:1 se não:0");
        int i = sc.nextInt();
        if(i == 1){
            JOptionPane.showInputDialog("digite o que vc quer imprimir na tela:");
            j = sc.next();
        }
        else{
            JOptionPane.showInputDialog("obrigado, e tenha um bom dia");
        }
        JOptionPane.showInputDialog("oq vc quis imprimir foi: "+j);
    }
    
}


package passar;

	
import java.util.Scanner;

public class JogoDaVelha1 {


    private static int jog;
    private static int[][] casa = new int[3][3];
    private static int linha, coluna, win;
    private static Scanner leitor = new Scanner(System.in);
    private static int jogador1, jogador2;


    public static void desenha(int x, int y){

        if(casa[x][y]==1){
            System.out.print("X");
        }else if(casa[x][y]==2){
            System.out.print("O");
        }else{
            System.out.print(" ");
        }
    }
    public static void jogo(){
        System.out.print("\n   1   2   3\n");
        System.out.print("1 ");
        desenha(0,0);
     System.out.print("  | ");
        desenha(0,1);
        System.out.print("  | ");
        desenha(0,2);
        System.out.print("\n --------------\n2 ");
        desenha(1,0);
        System.out.print("  | ");
        desenha(1,1);
        System.out.print("  | ");
        desenha(1,2);
        System.out.print("\n --------------\n3 ");
        desenha(2,0);
        System.out.print("  | ");
        desenha(2,1);
        System.out.print("  | ");
        desenha(2,2);
        System.out.println("\n");
    }
    public static void jogar(int jogador){
        int i=0;
        if (jogador==1){
            jog=1;
            System.out.println("Vez do jogador:"+jogador1);
        }else{
            jog=2;
            System.out.println("Vez do jogador:"+jogador2);
        }
        while(i==0){
            linha=0;
            coluna=0;
            while(linha<1||linha>3){
                System.out.print("Escolha a Linha (1,2,3):");
                linha=leitor.nextInt();
                if(linha<1 || linha>3){
                    System.out.println("Linha inválida! Escolha uma posição entre 1 e 3");
                }

            }
            while(coluna<1 || coluna>3){
                System.out.print("Escolha a Coluna (1,2,3):");
                coluna=leitor.nextInt();
                if(coluna<1||coluna>3){
                    System.out.println("Coluna invalida! Escolha uma posição entre 1 e 3");
                }
            }
            linha=linha-1;
            coluna=coluna-1;
            if(casa[linha][coluna]==0){
                casa[linha][coluna]=jog;
                i=1;
            }else{
                System.out.println("Posição ocupada!");
            }

        }
    }
   
    public static void check(){
        int i=0;

        for(i=0;i<3;i++){
            if(casa[i][0]==casa[i][1]&& casa[i][0]==casa[i][2]){
                if(casa[i][0]==1){
                    win=1;
                }
                if(casa[i][0]==2){
                    win=2;
                }
            }

        }

        for(i=0;i<3;i++){
            if(casa[0][i]==casa[1][i]&&casa[0][i]==casa[2][i]){
                if(casa[0][i]==1){
                    win=1;
                }
                if(casa[0][i]==2){
                    win=2;
                }
            }
        }
        if(casa[0][0]==casa[1][1] && casa[0][0]==casa[2][2]){
            if(casa[0][0]==1){
                win=1;
            }
            if(casa[0][0]==2){
                win=2;
            }
        }
        if(casa[0][2]==casa[1][1] && casa[0][2]==casa[2][0]){
            if(casa[0][2]==1){
                win=1;
            }
            if(casa[0][2]==2){
                win=2;
            }
        }
    }
    public static void cadastro(){
        System.out.println("Digite o nome do jogador1:");
        jogador1 = leitor.next();
        System.out.println("Digite o nome do jogador2");
        jogador2 = leitor.next();
    }
    public static void main(String[] args){

        cadastro();
        int i=0;
        for(i=0;i<9;i++){
            jogo();
            if(i%2==0)
                jogar(2);
            else
                jogar(1);
            check();
            if(win==1||win==2){
                i=10;
            }
        }
        jogo();
        System.out.println();
        if(win==1){
            System.out.println("Jogador "+ jogador1+ " é o ganhador!");
        }else if(win==2){
            System.out.println("Jogador "+ jogador2+ "e o ganhador!");
        }       
        else{
            System.out.println("Não houve vencedor! O jogo foi empate!!");
        }
    }

}
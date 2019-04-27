
package gui;

import controle.Controle;
import controle.ControleDist;
import exception.ModeloInexistenteException;
import javax.swing.JOptionPane;
import Modelo.Distribuidor;
import java.util.ArrayList;
import Modelo.Produto;
import Modelo.Distribuidor;

public class Menu {
    private Controle controle;
    private ControleDist cont;
    String menu = ":::Bem Vindo:::\n"+
                  "1-Distribuidor\n"+
                  "2-Produto\n"+
                  "0-Sair";
    String dti = ":::Distribuidor:::\n"+
                 "1-Cadastrar\n"+
                 "2-Buscar\n"+
                 "3-Excluir\n"+
                 "4-Atualizar\n"+
                 "0-Voltar";
    String pro =":::Produto:::\n"+
                 "1-Cadastrar\n"+
                 "2-Buscar\n"+
                 "3-Excluir\n"+
                 "4-Atualizar\n"+
                 "0-Voltar";
    int opcao = 0;
    public Menu(){
    controle = new Controle();
    cont = new ControleDist();
    }
        public void executar(){
            do{
                opcao = Integer.parseInt(
                JOptionPane.showInputDialog(menu));
                switch(opcao){
                case 1: Distribuidor();break;
                case 2: Produto();break;
                case 0: JOptionPane.showMessageDialog(null, "saindo");break;
                default:JOptionPane.showMessageDialog(null, "Opção invalida");break;
                }
            }while(opcao!=0);
        }

    private void Distribuidor() {
            do{
                opcao = Integer.parseInt(
                JOptionPane.showInputDialog(dti));
                switch(opcao){
                case 1: cadastrar();break;
                case 2: buscar();break;
                case 3: excluir();break;
                case 4: atualizar();break;   
                case 0: executar();break;
                default:JOptionPane.showMessageDialog(null, "Opção invalida");break;
                }        
            }while(opcao!=0);
    }
    private void Produto() {
            do{
                opcao = Integer.parseInt(
                JOptionPane.showInputDialog(pro));
                switch(opcao){
                case 1: cadastrarr();break;
                case 2: buscarr();break;
                case 3: excluirr();break;
                case 4: atualizarr();break;   
                case 0: executar();break;
                default:JOptionPane.showMessageDialog(null, "Opção invalida");break;
                }        
            }while(opcao!=0);
    }

    private void atualizar() {
         try{
            String CNPJ = JOptionPane.showInputDialog("digite o CNPJ");
            Distribuidor d = cont.buscar(CNPJ);
            String nome = JOptionPane.showInputDialog("digite o novo nome:");
            int cod = Integer.parseInt(JOptionPane.showInputDialog("digite o novo codigo:"));
            String tels = JOptionPane.showInputDialog("digite os novos telefones");
            d.setNome(nome);
            d.setCod(cod);
            d.setTels(null);
        }catch(ModeloInexistenteException a){
            JOptionPane.showMessageDialog(null, a.getMessage());
        }
    }

    private void excluir() {
        try{
            String CNPS = JOptionPane.showInputDialog("Digite o CNPj:");
            cont.excluir(CNPS);
        }catch(ModeloInexistenteException a){
            JOptionPane.showMessageDialog(null, a.getMessage());
        }
    }

    private void buscar() {
         try{
            String CNPS = JOptionPane.showInputDialog("Digite o CNPj:");
            Distribuidor a = cont.buscar(CNPS);
            JOptionPane.showMessageDialog(null, a);
        }catch(ModeloInexistenteException a){
            JOptionPane.showMessageDialog(null, a.getMessage());
        }
    }

    private void cadastrar() {
        int cod = Integer.parseInt(JOptionPane.showInputDialog("digite o cod:"));
        String nome = JOptionPane.showInputDialog("digite o nome:");
        String CNPS = JOptionPane.showInputDialog("digite o CNPj");
        String tels = JOptionPane.showInputDialog("digite o telefone");
        cont.cadastrar(opcao, nome, CNPS, null);
    }

    private void cadastrarr() {
        int cod = Integer.parseInt(JOptionPane.showInputDialog("digite o cod:"));
        String nome = JOptionPane.showInputDialog("digite o nome:");
        String descricao = JOptionPane.showInputDialog("digite a descrição do produto:");
        String dist = JOptionPane.showInputDialog("digiti o distribuidor:");
        controle.cadastrar(opcao, nome, descricao, null);
    }

    private void buscarr() {
         try{
            String CNPS = JOptionPane.showInputDialog("Digite o cod:");
            Produto a = controle.buscar(opcao);
            JOptionPane.showMessageDialog(null, a);
        }catch(ModeloInexistenteException a){
            JOptionPane.showMessageDialog(null, a.getMessage());
        }
    }

    private void excluirr() {
         try{
            String CNPS = JOptionPane.showInputDialog("Digite o cod:");
            controle.buscar(opcao);
        }catch(ModeloInexistenteException a){
            JOptionPane.showMessageDialog(null, a.getMessage());
        }
    }

    private void atualizarr() {
        try{
            int cod = Integer.parseInt(JOptionPane.showInputDialog("digite o codigo"));
            Produto p = controle.buscar(cod);
            String nome = JOptionPane.showInputDialog("digite o novo nome:");
            String desc = JOptionPane.showInputDialog("digite a nova descrição");
            String cnpj = JOptionPane.showInputDialog("digite o novo CNPJ");
            Distribuidor d = cont.buscar(cnpj);
            p.setNome(nome);
            p.setDescricao(desc);
            p.getDist();
        }catch(ModeloInexistenteException a){
            JOptionPane.showMessageDialog(null, a.getMessage());
        }
    }

}
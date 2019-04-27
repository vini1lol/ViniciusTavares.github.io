
package controle;

import Modelo.Distribuidor;
import Modelo.Produto;
import exception.ModeloInexistenteException;
import java.util.ArrayList;


public class Controle implements IntProduto {
    
    ArrayList<Produto> modelo= new ArrayList<Produto>();
    
    
    @Override
    public void cadastrar(int cod, String nome, String descricao, Distribuidor dist) {
        Produto d = new Produto(cod, nome, descricao, dist);
        modelo.add(d);
    }

    public Produto buscar(int cod) throws ModeloInexistenteException{
         for(Produto d: modelo){
            if( d.getCod() == cod){
                return d;
             }
        }
        throw new ModeloInexistenteException();
    }

    @Override
    public void excluir(int cod) throws ModeloInexistenteException {
        Produto d = buscar(cod);
        modelo.remove(d);
    }
    
    
}

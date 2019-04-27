
package controle;

import Modelo.Distribuidor;
import Modelo.Produto;
import exception.ModeloInexistenteException;


public interface IntProduto {
    public void cadastrar(int cod, String nome, String descricao, Distribuidor dist);
    public Produto buscar(int cod) throws ModeloInexistenteException;
    public void excluir(int cod) throws ModeloInexistenteException;
}

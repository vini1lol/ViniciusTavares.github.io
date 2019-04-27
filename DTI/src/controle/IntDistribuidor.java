
package controle;

import Modelo.Distribuidor;
import exception.ModeloInexistenteException;
import java.util.ArrayList;


public interface IntDistribuidor {
    public void cadastrar(int cod, String nome, String CNPj, ArrayList<String>tesl);
    public Distribuidor buscar(String CNPj)throws ModeloInexistenteException;
    public void excluir(String CNPj)throws ModeloInexistenteException;
}

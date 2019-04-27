

package controle;

import Modelo.Distribuidor;
import exception.ModeloInexistenteException;
import java.util.ArrayList;

public class ControleDist implements IntDistribuidor {
    
    ArrayList<Distribuidor>dist=new ArrayList<Distribuidor>();
    private ArrayList<String> tels;
  
        public void cadastrar(int cod, String nome, String CNPj,ArrayList<String>tels) {
        Distribuidor dt = new Distribuidor(cod, nome, CNPj, tels);
        dist.add(dt);
    }

        public Distribuidor buscar(String CNPj) throws ModeloInexistenteException {
        for(Distribuidor dt : dist){
            if(dt.getCNPS().equals(CNPj)){
                return dt;
            }
        }
        throw new ModeloInexistenteException();
    }

        public void excluir(String CNPj) throws ModeloInexistenteException {
            Distribuidor dt = buscar(CNPj);
            dist.remove(dt);
    }

    
}

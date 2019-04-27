

package Modelo;


public class Produto {
    private int cod;
    private String nome, descricao;
    private Distribuidor dist;
    
    public Produto(int cod, String nome, String descricao,Distribuidor dist ){
        this.cod = cod;
        this.nome=nome;
        this.descricao=descricao;
        this.dist=dist;
    }

    public int getCod() {
        return cod;
    }

    public void setCod(int cod) {
        this.cod = cod;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getDescricao() {
        return descricao;
    }

    public void setDescricao(String descricao) {
        this.descricao = descricao;
    }

    public Distribuidor getDist() {
        return dist;
    }

    public void setDist(Distribuidor dist) {
        this.dist = dist;
    }


    @Override
    public String toString(){
        return "Cod: "+this.cod+"\n"+
               "Nome: "+this.nome+"\n"+
               "descrição: "+this.descricao+"\n"+
               "distribuidor: "+this.dist;
    }
}

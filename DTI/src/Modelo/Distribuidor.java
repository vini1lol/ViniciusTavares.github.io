

package Modelo;

import java.util.ArrayList;

public class Distribuidor {
    private int cod;
    private String nome, CNPj;
    private ArrayList<String>tels;
    
    public Distribuidor(int cod, String nome,String CNPj,ArrayList<String>tels){
        this.cod=cod;
        this.nome=nome;
        this.CNPj=CNPj;
        this.tels=tels;
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

    public String getCNPS() {
        return CNPj;
    }

    public void setCNPS(String CNPS) {
        this.CNPj = CNPS;
    }

    public ArrayList<String> getTels() {
        return tels;
    }

    public void setTels(ArrayList<String> tels) {
        this.tels = tels;
    }
    @Override
    public String toString(){
        return "Cod: "+this.cod+"\n"+
               "Nome: "+this.nome+"\n"+
               "CNPS: "+this.CNPj+"\n"+
               "Telefones: "+this.tels;
    }
}

class Refrigerante:
    def __init__(self,nom,preco):
        self.nome= nom
        self.preco = preco
    def imprimirefri(self):
        print("Nome: {} \nPreço: R${}.".format(self.nome,self.preco))
if __name__=="__main__":
    c = Refrigerante('coca',12.10)
    c.imprimirefri()

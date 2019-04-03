import refri as R
class Pedido:
    def __init__(self,lis= None):
        self.nrefri = lis
    def imprimipedido(self):
        for i in range(len(self.nrefri)):
            self.nrefri[i].imprimirefri()
    def total(self):
        c=0.0;
        for i in range(len(self.nrefri)):
            c += self.nrefri[i].preco
        print(c)
    def add(self,re):
        self.nrefri.append(re)
    def remov(self,r):
        for i in range(len(self.nrefri)):
            if r in self.nrefri[i].nome:
                self.nrefri.pop(i)
                break
if __name__=="__main__":
    a = R.Refrigerante("ca",10.20)
    b = R.Refrigerante("al",10.20)
    p = Pedido([a,b])
    p.imprimipedido()
    p.total()
    p.add(c)
    p.imprimipedido()
    p.total()
    p.remov('al')
    p.imprimipedido()
    

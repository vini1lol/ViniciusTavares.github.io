import refri as R
import pedido as P
class MaquinaDeRefrigerante:
    def __init__(self):
        a = R.Refrigerante("coca",10.20)
        b = R.Refrigerante("pp",5.20)
        c = R.Refrigerante("dc",13.20)
        self.re= [a,b,c]
    def listref(self):
        for i in range(len(self.re)):
            print(i,end=' ')
            self.re[i].imprimirefri()
    def addp(self,p,r):
        p.add(self.re[r])
if __name__=="__main__":
    a = R.Refrigerante("coca",10.20)
    b = R.Refrigerante("pp",5.20)
    c = R.Refrigerante("dc",13.20)
    p = P.Pedido([a,b])
    p.imprimipedido()
    m = MaquinaDeRefrigerante()
    m.addp(p,2)
    p.imprimipedido()

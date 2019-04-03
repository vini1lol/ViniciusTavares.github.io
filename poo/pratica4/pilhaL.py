import listaNormal as LN

class Pilha:
    def __init__(self):
        self._l = LN.Array()
        self._quantidade = 0
    def empilha(self,ob):
        self._quantidade+=1
        self._l.insere(ob)
    def desempilha(self):
        self._quantidade-=1
        self._l.remove(self._quantidade)
    def vazio(self):
        return self._l.eh_vazio()
    def imprime(self):
        self._l.imprime()
if __name__=="__main__":
    c = Pilha()
    print(c.vazio())
    c.empilha(10)
    c.empilha(15)
    c.empilha("ola")
    c.imprime()
    print(c.vazio())
    c.desempilha()
    c.imprime()
    

import listaNormal as LN

class Fila:
    def __init__(self):
        self._l=LN.Array()
        self._quantidade = 0
    def enfileira(self,ob):
        self._quantidade+=1
        self._l.insere(ob)
    def desenfileira(self):
        self._quantidade-=1
        self._l.remove(0)
    def vazio(self):
        return self._l.eh_vazio()
    def imprime(self):
        self._l.imprime()

if __name__=="__main__":
    c = Fila()
    print(c.vazio())
    c.enfileira(15)
    c.enfileira(40)
    c.imprime()
    c.desenfileira()
    c.imprime()
    print(c.vazio())

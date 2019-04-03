import listaEncadeada as LE

class Fila:
    def __init__(self):
        self._l= LE.Encadeada()
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
    c.enfileira(1)
    c.enfileira(849)
    c.enfileira("oi")
    c.imprime()
    c.desenfileira()
    c.imprime()
    print(c.vazio())

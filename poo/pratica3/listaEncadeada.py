import celula as cel
class Encadeada:
    def __init__(self):
        self._quantidade = 0
        self._head= None
        self._tail= None
    def insere(self,ob):
        c = cel.celula(ob)
        if self._quantidade == 0:
            self._head = c
            self._tail = c
        else:
            self._tail.proxima=c
            self._tail = c
        self._quantidade+=1
    def obtem_objeto(self,ob):
        c = self._head
        if ob < self._quantidade:
            for b in range(ob):
                c = c.proxima
            return c.dados
        else:
            print("objeto não existe")
    def eh_vazio(self):
        if self._quantidade == 0:
            return True
        else:
            return False
    def remove(self,a):
        if self.eh_vazio():
            print("lista vazia")
        else:
            c = self._head
            if a>0:
                for d in range(a-1):
                    c = c.proxima
                c.proxima = c.proxima.proxima
                if a == self._quantidade-1:
                    self._tail=c
                    self._tail.proximo = None
            else:
                self._head = self._head.proxima
                
            self._quantidade-=1
    def imprime(self):
        if self.eh_vazio() == False:
            c = self._head
            for d in range(self._quantidade):
                print(c.dados , end=" ")
                c = c.proxima
            print(" ")
        else:
            print("lista vazia")

    def copia(self):
        c = Encadeada()
        d = self._head
        if self.eh_vazio() == False:
            for b in range(self._quantidade):
                c.insere(d.dados)
                d = d.proxima
            return c
        else:
            print("lista vazia")
    def concatena(self,l):
        d = self._head
        for b in range(l._quantidade):
            self.insere(l.obtem_objeto(b))
b = Encadeada()
b.insere("a")
b.insere("b")
b.insere("c")
b.insere("d")
b.imprime()
b.remove(3)
b.imprime()
b.copia().imprime()
l = Encadeada()
l.insere("d")
l.insere(12)
l.insere("ahkbs")
b.concatena(l)
b.imprime()

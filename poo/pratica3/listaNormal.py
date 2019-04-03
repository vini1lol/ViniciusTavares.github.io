class Array:
    def __init__(self,t=5):
        self._capacidade = t
        self._dados=[None]*self._capacidade
        self._quantidade = 0
    def _aloca_memoria(self):
        a = [None]*(2*self._capacidade)
        for c in range(self._capacidade):
            a[c] = self._dados[c]
        self._capacidade = 2*self._capacidade
        self._dados = a
    def insere(self,ob):
        self._quantidade+=1
        if self._quantidade > self._capacidade:
           self._aloca_memoria()
        self._dados[self._quantidade-1]=ob
    def obtem_objeto(self,a):
        if a < self._quantidade:
            return self._dados[a]
        else:
            print("index não existente")
    def eh_vazio(self):
        if self._quantidade != 0:
            return False
        else:
            return True
    def remove(self,b):
        if self.eh_vazio() or b>=self._quantidade:
            print("lista Vazia ou index não existe")
        else:
            for c in range(b,self._quantidade):
                self._dados[c] = self._dados[c+1]
            self._quantidade-=1
    def imprime(self):
        if self.eh_vazio() == False:
            for c in range(self._quantidade):
                print(self._dados[c], end=' ')
            print("")
        else:
            print("lista vazia")
    def copia(self):
        c= Array()
        if self.eh_vazio() == False:
            for b in range(self._quantidade):
                c.insere(self._dados[b])
            return c
        else:
            print("lista vazia")
    def concatena(self,l):
        for c in range(l._quantidade):
            self.insere(l.obtem_objeto(c))
if __name__=="__main__":
    c = Array()
    c.insere(12)
    c.insere(['a',5,12,'d'])
    c.insere("canada")
    c.imprime()
    c.copia().imprime()
    l = Array()
    l.insere(10)
    l.insere("c")
    l.insere(["a",12,100,[5,"as"]])
    c.concatena(l)
    c.imprime()
    

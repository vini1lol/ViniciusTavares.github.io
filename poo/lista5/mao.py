import carta as ct
class Mao:
    def __init__(self,n):
        self.ncart =n;
        self.mao = str
    def imprimemao(self):
        c=ct.Carta()
        for i in range(n):
            self.mao[i]=c.gera()
        for i in range(n):
            for j in range(1,n):
                if self.mao[i] == self.mao[j]:
                    self.mao[j]=c.gera()
        for i in range(n):
            print(self,mao[i])
    def jogo(self):
        
                    

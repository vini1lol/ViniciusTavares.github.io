import random as R
class Carta:
    def __init__(self,car=range(1,53)):
        self.cat = car
    def imprime(self):
        c = R.choice(self.cat)
        if c==1 or c==14 or c==27 or c==40:
            print("ás de",end=' ')
        elif c==11 or c==24 or c==37 or c==50:
            print("valete de",end=' ')
        elif c==12 or c==25 or c==38 or c==51:
            print("dama de",end=' ')
        elif c==13 or c==26 or c==39 or c==52:
            print("rei de",end=' ')
        else:
            i=0
            for d in range(c):
                i+=1
                if i>13:
                    i=1
            print("{} de".format(i),end=' ')
        if c>0 and c<=13:
            print("espadas")
        elif c>13 and c<=26:
            print("paus")
        elif c>26 and c<=39:
            print("copas")
        elif c>39:
            print("ouros")
    def gera(self):
        c = R.choice(self.cat)
        if c==1 or c==14 or c==27 or c==40:
            s="ás de"
        elif c==11 or c==24 or c==37 or c==50:
            s="valete de"
        elif c==12 or c==25 or c==38 or c==51:
            s="dama de"
        elif c==13 or c==26 or c==39 or c==52:
            s="rei de"
        else:
            i=0
            for d in range(c):
                i+=1
                if i>13:
                    i=1
            s="{} de".format(i)
        if c>0 and c<=13:
            s+="espadas"
        elif c>13 and c<=26:
            s+="paus"
        elif c>26 and c<=39:
            s+="copas"
        elif c>39:
            s+="ouros"
        return s
if __name__=="__main__":          
    d = Carta()
    d.imprime()
    print(d.gera())

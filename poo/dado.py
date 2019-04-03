import random as R
class Dado:
    def __init__(self,num):
        self.faces = num
    def rolar(self):
        x=R.randint(1,self.faces)
        return x

a=int(input("Numero de faces: "))
c = Dado(a)
print("face {} do dado".format(c.rolar()))

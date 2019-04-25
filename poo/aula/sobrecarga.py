
class Pesso:
    def __init__(self,n='',i=15,a=2003):
        self._nome = n
        self._idade = i
        self._ano = a
    def __repr__(self):
        s = '{},{},{}'.format(self._nome,self._idade,self._ano)
        return s
    def __add__(self,b):
        if type(b) == Pesso:
            a = self._idade + b._idade
            c = Pesso(self._nome,a,self._ano)
            return c
if __name__=="__main__":
    a = Pesso("joao",46,1980)
    b = Pesso("rafa",4,2015)
    print(a+b)
    

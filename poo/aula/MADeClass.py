class Pessoa:
    _quant = 0
    def __init__(self,n=''):
        self._nome = n
        Pessoa._quant += 1
    @staticmethod
    def num_pessoas():
        return Pessoa._quant
    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self,n):
        if type(n) == str:
            self._nome = n
        else:
            print("Erro")

if __name__=="__main__":
    p1=Pessoa('jao')
    p2 = Pessoa('nata')
    print(p1.num_pessoas())
    p1.nome = 'sa'
    print(p1.nome)

class Robo:
    def __init__(self):
        self.__nome = ""
        self.__posicao = (10,10)
        self.__operacao = False
    def get_nome(self):
        return self.__nome
    def set_nome(self,nome):
        self.__nome = nome
    nome = property(get_nome,set_nome)
    def get_posicao(self):
        return self.__posicao
    def set_posicao(self,posicao):
        self.__posicao = posicao
    posicao = property(get_posicao,set_posicao)
    def get_operacao(self):
        return self.__operacao
    def set_operacao(self,operacao):
        self.__operacao = operacao
    operacao = property(get_operacao,set_operacao)
    def imprime(self):
        if self.__operacao == True:
            print("{} esta em operação na posição {}".format(self.__nome,self.__posicao))
        else:
            print("{} não esta em operação e esta na posição {}".format(self.__nome,self.__posicao))
    def move_para(self,posi):
        self.__posicao = posi
    def acha_mais_proxim(self,lista):
        robo = 0
        proximo=abs((lista[0].posicao[0]-self.posicao[0]))+abs((lista[0].posicao[1]-self.__posicao[1]))
        for c in range(1,len(lista)):
            s = abs((lista[c].posicao[0]-self.posicao[0]))+abs((lista[c].posicao[1]-self.__posicao[1]))
            if s  < proximo: 
                proximo = s
                robo = c
        print("o robo maior proximo de {} é o {}".format(self.__nome,lista[robo].nome))
    def move(self,tup):
        if type(tup)== tuple:
            if len(tup) == 2:
                if type(tup[0]) == float and type(tup[1]) == float:
                    self.__posicao = (self.__posicao[0]+tup[0],self.__posicao[1]+tup[1])
                    return self.__posicao
        else:
            print("valor errado")
a=Robo()
a.nome = "mat"
a.posicao = (10.2,8.3)
a.operacao = True
a.imprime()
t=(10.0,10.0)
a.move(t)
a.imprime()

        

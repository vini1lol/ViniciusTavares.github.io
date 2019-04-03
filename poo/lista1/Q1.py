class Fruta:
    def __init__(self):
        self.__tipo = "manga"
        self.__peso = 20
        self.__data = (10,2,2015)
    def get_tipo(self):
        return self.__tipo
    def set_tipo(self,tipo):
        if type(tipo) == str:
            self.__tipo = tipo
        else:
            print("ERRO, valor diferente de uma string")
    def get_peso(self):
        return self.__peso;
    def set_peso(self,peso):
        if type(peso) == int:
            self.__peso = peso
        else:
            print("ERRO, valor diferente de um inteiro")
    def get_data(self):
        return self.__data;
    def set_data(self,data):
        if type(data) == tuple:
            self.__data = data
        else:
            print("ERRO, valor diferente de uma tuple")
    tipo =  property(get_tipo,set_tipo)
    peso = property(get_peso,set_peso)
    data = property(get_data,set_data)
    def imprime(self):
        print(self.__tipo,self.__peso,self.__data)
    def tempo_coleta(self,data):
        tempo = [0,0,0]
        tempo[0] = data[0]-self.__data[0]
        tempo[1]= data[1]-self.__data[1]
        tempo[2]= data[2]-self.__data[2]
        print("{} dias,{} meses,{} anos des do dia {}".format(tempo[0],tempo[1],tempo[2],self.__data))
    def compara(self,a,b):
        if a.tipo == b.tipo:
            print("1 e",end=" ")
            if a.peso > b.peso:
                print("-1")
            elif a.peso < b.peso:
                print("1")
            else:
                    print("0")
        else:
            print("0 e 0")
        
a = Fruta()
a.tipo = "manga"
a.peso = 20
b = Fruta()
b.tipo = "manga"
b.peso = 20
a.imprime()
b.imprime()
a.compara(a,b)

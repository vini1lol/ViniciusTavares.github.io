class Fruta:
    def __init__(self,fruta = '',pe=0.0,dat=(10,5,2018)):
        self.__tipoFrut = fruta
        self.__peso = pe
        self.__data = dat
    def get_tipoFrut(self):
        return self.__tipoFrut
    def set_tipoFrut(self,t):
        self.__tipoFrut = t
        
    def get_peso(self):
        return self.__peso
    def set_peso(self,pe):
        self.__peso = pe
        
    def get_data(self):
        return self.__data
    def set_data(self,dat):
        self.__data = dat

    fruta = property(get_tipoFrut,set_tipoFrut)
    peso = property(get_peso,set_peso)
    data = property(get_data,set_data)

    def imprime(self):
        print("Tipo da fruta: {0} \nPeso: {1} Kg\nData de fabricação: {2}".format(self.__tipoFrut,self.__peso,self.__data))
    def tempo_coleta(self,dat):
        if dat[0] < self.__data[0]:
            mes = -1
            dia = (30-self.__data[0])+dat[0]
        else:
            mes = 0
            dia = dat[0]-self.__data[0]
        if dat[1] < self.__data[1]:
            mes += (12-self.__data[1])+dat[1]
            ano = (dat[2]-self.__data[2])-1
        else:
            mes += dat[1]-self.__data[1]
            ano = dat[2]-self.__data[2]
        print("A fruta foi produzida a: {} dias {} meses {} anos".format(dia,mes,ano))
        
p = Fruta()
p.fruta = "jaca"
p.peso = 10.0
p.data = (12,5,2018)
p.imprime()
da = (9,3,2019)
p.tempo_coleta(da)

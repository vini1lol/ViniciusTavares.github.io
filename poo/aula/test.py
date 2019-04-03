class Pessoa:
    def __init__(self):
        self.__nome = " " #membro privado (__)
        self.__idade = int
        self.__cep = int
    def get_nome(self):
        return self.__nome
    def set_nome(self,nome):
        if type(nome) == str:
            self.__nome = nome
        else:
            print("ERRO")
    def get_idade(self):
        return self.__idade
    def set_idade(self,idade):
        if type(idade) == int:
            self.__idade = idade
        else:
            print("Erro paramento não é um inteiro")
    def get_cep(self):
        return self.__cep
    def set_cep(self,cep):
        self.__cep = cep
    nome = property(get_nome,set_nome)
    idade = property(get_idade,set_idade)
    cep= property(get_cep,set_cep)
    
a = Pessoa()
a.nome="mat"
a.idade = 20
a.cep = 59152600
print(a.nome,end=",")
print(a.idade,end=",")
print(a.cep,end =".")

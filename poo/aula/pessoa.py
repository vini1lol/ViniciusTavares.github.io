# -*- coding: utf-8 -*-

class Pessoa:
    def __init__(self, nome='', idade=''):
        self._nome = nome
        self._idade = idade

if __name__ == "__main__":
    p1 = Pessoa()
    p1.nome = 'Jose'
    p1.idade = 30
    print('Nome com __repr__:')
    print(p1)
    p2 = Pessoa('Maria', 27)
    print('Nome com get: {}, idade com get: {}'.format(p2.nome, p2.idade))
    p3 = Pessoa('Pedro', 31)
    p4 = Pessoa('Ana', 25)
    p5 = Pessoa('Antonio', 28)
    print('Total de instancias de Pessoa:')
    print(Pessoa._num_pessoas)
    #print('Instancias:')
    #print(Pessoa._instancias)
    print('Instancias ordenadas por nome:')
    #Pessoa.ordena()
    print(Pessoa._instancias)
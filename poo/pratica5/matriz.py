# -*- coding: utf-8 -*-

class Matriz:
    """
    Modela uma matriz de tamanho nl x nc
    de números reais.
    """
    def __init__(self, nl, nc):
        self._nl = nl
        self._nc = nc
        self._dados = []
        self._inicializa()

    def _inicializa(self):
        for i in range(self._nl):
            self._dados.append([])
            for j in range(self._nc):
                self._dados[i].append(0.0)

    def __getitem__(self, pos):
        """
        Obtém o elemento na linha l e coluna c
        da matriz da forma A[l,c]
        (ou seja, pos é uma tupla: pos = (i,j)).
        """
        if type(pos) != tuple:
            print('pos deve ser do tipo tuple')
        else:
            l, c = pos
            if l >= self._nl or c >= self._nc:
                print('indice fora da matriz')
            else:
                return self._dados[l][c]

    def __setitem__(self, pos, v):
        """
        Atribui o elemento na linha l e coluna c
        da matriz da forma A[l,c] = v
        (ou seja, pos é uma tupla: pos = (i,j)).
        """
        if type(pos) != tuple:
            print('pos deve ser do tipo tuple')
        else:
            l, c = pos
            if l >= self._nl or c >= self._nc:
                print('indice fora da matriz')
            else:
                self._dados[l][c] = v
    def __repr__(self):
        """
        Imprime os dados em forma de matriz
        Ex:
        1 0.0 0.0
        0.0 1 0.0
        0.0 0 1
        """
        s = ''
        for c in range(self._nl):
            for i in range(self._nc):
                s+= " {}".format(self[c,i])
            s += "\n"
        return s;
    def __add__(self,a):
        """
        Soma duas matrizes e retorna uma matriz resuldado da soma
        """
        if type(a)!= Matriz:
            print("a deve ser do tipo matriz")
        elif self._nl == a._nl and self._nc == a._nc:
            b = Matriz(a._nl,a._nc)
            for c in range(self._nl):
                for i in range(self._nc):
                    b[c,i]= self._dados[c][i]+a[c,i]
            return b
        else:
            print("indices diferentes")
    def __iadd__(self,a):
        """
        Soma duas matrizes e armazena o resultado em self
        """
        if type(a)!= Matriz:
            print("a deve ser do tipo matriz")
        elif self._nl == a._nl and self._nc == a._nc:
            for c in range(self._nl):
                for i in range(self._nc):
                    self[c,i]= self._dados[c][i]+a[c,i]
            return self
        else:
            print("indices diferentes")
    def __sub__(self,a):
        """
        Subtrai duas matrizes e retorna uma matriz resultante
        """
        if type(a)!= Matriz:
            print("a deve ser do tipo matriz")
        elif self._nl == a._nl and self._nc == a._nc:
            b = Matriz(a._nl,a._nc)
            for c in range(self._nl):
                for i in range(self._nc):
                    b[c,i]= self._dados[c][i]-a[c,i]
            return b
        else:
            print("indices diferentes")
    def __isub__(self,a):
        """
        Subtrai duas matrizes e armazena o resultado em self
        """
        if type(a)!= Matriz:
            print("a deve ser do tipo matriz")
        elif self._nl == a._nl and self._nc == a._nc:
            for c in range(self._nl):
                for i in range(self._nc):
                    self[c,i]= self._dados[c][i]-a[c,i]
            return self
        else:
            print("indices diferentes")
    def __eq__(self,a):
        """
        Verifica se duas matrizes são iguais, se sim retorna True, caso
        contrario retorna False
        """
        if type(a)!= Matriz:
            print("a deve ser do tipo matriz")
        elif self._nl == a._nl and self._nc == a._nc:
            for c in range(self._nl):
                for i in range(self._nc):
                    if self._dados[c][i] != a[c,i]:
                        return False
            return True
        else:
            return False
    def __ne__(self,a):
        """
        Verifica se duas matrizes são diferentes, se sim retorna True,caso
        contrario retorna False
        """
        if type(a)!= Matriz:
            print("a deve ser do tipo matriz")
        elif self._nl == a._nl and self._nc == a._nc:
            for c in range(self._nl):
                for i in range(self._nc):
                    if self._dados[c][i] != a[c,i]:
                        return True
            return False
        else:
            return False
    def __mul__(self,a):
        """
        Multiplica duas Matrizes N x M e M x P e retorna o resultado
        como uma matriz N x P
        """
        if type(a)!= Matriz:
            print("a deve ser do tipo matriz")
        elif self._nc == a._nl:
            b = Matriz(self._nl,a._nc)
            for i in range(self._nl):
                for j in range(a._nc):
                    for k in range(self._nc):
                        b[i,j]+= self[i,k]*a[k,j]
            return b
        else:
            print("indices diferentes")
        
if __name__ == "__main__":
    a = Matriz(3, 3)
    print(a)
    a[0,0] = 1
    a[1,1] = 1
    a[2,2] = 1
    print('A:')
    print(a)
    b = Matriz(3, 3)
    b[0,2] = 3
    b[1,0] = -1
    b[1,1] = 2
    print('B:')
    print(b)
    a += b
    print('A += B:')
    print(a)
    c = Matriz(3,3)
    c = a - b
    print('A - B:')
    print(c)
    d = Matriz(3,3)
    d[0,0] = 1
    d[1,1] = 1
    d[2,2] = 1
    print('D:')
    print(d)
    print('C == D:')
    print(c == d)
    print(c!=d)
    e = b*d
    print('B*D:')
    print(e)

class celula:
    def __init__(self,a=None):
        self._dados=a
        self._proxima = None
        
    def get_proxima(self):
        return self._proxima
    def set_proxima(self,a):
        self._proxima = a
    proxima = property(get_proxima,set_proxima)
    def get_dados(self):
        return self._dados
    def set_dados(self,a):
        self._dados = a
    dados = property(get_dados,set_dados)
    def imprime(self):
        print(self._dados)

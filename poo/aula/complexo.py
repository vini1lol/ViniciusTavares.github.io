class complexo:
    def __int__(self,real = 0.0,imag = 0.0):
        self.re = real
        self.im = imag
    def get_re(self):
        return self.re
    def set_re(self,ree):
        self.re=ree
    def get_im(self):
        return self.im
    def set_im(self,imag):
        self.im=imag
    real = property(get_re,set_re)
    imagi = property(get_im,set_im)
    def zera(self):
        self.re = 0.0
        self.im = 0.0
    def modulo(self):
        

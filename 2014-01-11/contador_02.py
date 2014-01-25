#! -*- coding: utf-8 -*-

from contador_01 import Contador

class Contador2(Contador):
    
    def __init__(self, valor_inicial=0, incremento=1):
        super(Contador2, self).__init__(valor_inicial)
        # Esto es lo nuevo
        self.incremento = incremento
    
    def incrementar(self):
        #for x in range(self.incremento):
        #    super(Contador2, self).incrementar()
        self.valor += self.incremento
        
if __name__ == '__main__':

    c1 = Contador2(100, 10)
    print "Valor inicial: %d" % c1.valor
    for x in xrange(5):
        c1.incrementar()
    print "Valor final: %d" % c1.valor 


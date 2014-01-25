#! -*- coding: utf-8 -*-

class Contador(object):
    
    def __init__(self, valor_inicial=0):
        self.valor = valor_inicial
    
    def incrementar(self):
        self.valor += 1
        
if __name__ == '__main__':

    c1 = Contador()
    print "Valor inicial: %d" % c1.valor
    for x in xrange(5):
        c1.incrementar()
    print "Valor final: %d" % c1.valor 


#! -*- coding: utf-8 -*-

class Vocales(object):

    def __init__(self):
        self.generador = self.generador_vocales()
        self.iterador = self.generador.__iter__()
        
    def generador_vocales(self):
        yield 'a'
        yield 'e'
        yield 'i'
        yield 'o'
        yield 'u'
        

    def next(self):
        return self.iterador.next()
        
    def __iter__(self):
        return self
        
        
if __name__ == '__main__':
    for x in Vocales():
        print x

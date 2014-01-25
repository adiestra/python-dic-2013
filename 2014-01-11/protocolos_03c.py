#! -*- coding: utf-8 -*-

class Vocales(object):

    def __init__(self):
        self.generador = self.generador_vocales()
        
    def generador_vocales(self):
        yield 'a'
        yield 'e'
        yield 'i'
        yield 'o'
        yield 'u'
        

    def __iter__(self):
        return self.generador.__iter__()
        
        
if __name__ == '__main__':
    for x in Vocales():
        print x

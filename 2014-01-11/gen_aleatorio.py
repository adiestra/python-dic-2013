#! -*- coding: utf-8 -*-

def generador_enteros():
    from random import randint
    veces = randint(0, 100)
    for x in xrange(veces):
        yield randint(0, 100)
        
print [x for x in generador_enteros()]

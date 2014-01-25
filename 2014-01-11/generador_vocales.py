#! -*- coding: utf-8 -*-

def generador_vocales():
    yield 'a'
    yield 'e'
    yield 'i'
    yield 'o'
    yield 'u'
    

for v in generador_vocales():
    print v
    
print [v for v in generador_vocales()]

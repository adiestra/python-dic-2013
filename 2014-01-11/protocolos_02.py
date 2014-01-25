#! -*- coding: utf-8 -*-

def iterador_a_lista(obj):
    lista = []
    iterador = obj.__iter__()
    while True:
        try:
            elemento = iterador.next()
        except StopIteration:
            break
        lista.append(elemento)
    return lista
    
print iterador_a_lista([1, 2, 3])
print iterador_a_lista({'a':10, 'b':20})

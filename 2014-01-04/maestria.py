# -*- coding: utf-8 -*-
# Una funcion que recibe una funcion booleana
# como argumento. Esta funcione define un
# decorador. El decorador va a invocar a la 
# funcion booleana para saber si llama o no
# a la funcion decorada. 
# Los argumentos de la funciona booleana, son
# los mismos de la funcion decorada.
# Los argumentos no son conocidos.

def decoracion_condicional(fbool):
    def decorador(f):
        def aux(*args, **kwargs):
            if fbool(*args, **kwargs):
                return f(*args, **kwargs)
        return aux
    return decorador


def imprimir_argumentos(*args, **kwargs):
    print args
    print kwargs
    
    
def cardinalidades_distintas(*args, **kwargs):
    return len(args) != len(kwargs)
    
    
    
prueba = imprimir_argumentos
fbool = cardinalidades_distintas
decorador = decoracion_condicional(fbool)

funcion_decorada = decorador(prueba)

args = (1, 2, 3, 4)
kwargs = {'a': 10, 'b': 20, 'c': 30}

# funcion_decorada(*args, **kwargs)

@decoracion_condicional(cardinalidades_distintas)
def imprimir_argumentos_02(*args, **kwargs):
    print args
    print kwargs


imprimir_argumentos_02(*args, **kwargs)

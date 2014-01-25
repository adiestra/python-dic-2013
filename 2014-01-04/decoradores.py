# -*- coding: utf-8 -*-

def mayor_de_edad(f):
    def aux(*args, **kwargs):
        edad = kwargs.get('edad', None)
        if edad is not None and edad < 18:
            print "Menor de edad"
        else:
            return f(*args, **kwargs)
    return aux
    
def solo_nacionales(f):
    def aux(*args, **kwargs):
        pais = kwargs.get('pais', None)
        if pais is not None and pais != 'PERU':
            print "Extranjero!!!"
        else:
            return f(*args, **kwargs)
    return aux
    

def prueba(*args, **kwargs):
    print args
    print kwargs


#prueba(10, 20, pais='PERU', edad=36)

#(solo_nacionales(mayor_de_edad(prueba)))(10, 20, pais='PERU', edad=36)

f1 = prueba
f2 = mayor_de_edad(f1)
f3 = solo_nacionales(f2)

f3(10, 20, pais='PERU', edad=36)

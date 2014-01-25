#! -*- coding: utf-8 -*-

class Clase1(object):

    @classmethod
    def saludar(cls):
        print "Hola, soy la clase %s" % cls.__name__
        
        
       
class Clase2(Clase1):
    pass
    
    
obj1 = Clase1()
obj1.saludar()

obj2 = Clase2()
obj2.saludar()

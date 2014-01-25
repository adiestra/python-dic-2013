#! -*- coding: utf-8 -*-

class NombreClaseMixIn(object):

    def imprimir_nombre_clase(object):
        """Algo que quisieramos poder incluir
           a voluntad en cualquier otra clase"""
        print "Clase: %s" % (self.__class__.name)


# Una jerarquia de clases
        
class Vehiculo(object):
    pass
    
class Automovil(Vehiculo, NombreClaseMixIn):
    pass
    
    
# Otra jerarquia que no tiene nada que ver

class Documento(object):
    pass
    
class Factura(Documento, NombreClaseMixIn):
    pass

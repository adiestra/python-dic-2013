# -*- coding: utf-8 -*-


def mayor_de_edad(mayoria_edad):
    def decorador(f):
        def aux(edad):
            if edad >= mayoria_edad:
                return f(edad)
            else:
                print "Es menor de edad!"
        return aux
    return decorador
    
@mayor_de_edad(mayoria_edad=21)
def ir_al_cine(edad):
    print "Viendo pelicula!"
    
    
ir_al_cine(20)

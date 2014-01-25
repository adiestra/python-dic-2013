#! -*- coding: utf-8 -*-

class Coche(object):
    """Abstraccion de los objetos coche."""
    
    
    def __init__(self, gasolina):
        self.gasolina = gasolina
        print "Tenemos", gasolina, "litros"

    def arrancar(self):
        if self.gasolina > 0:
            print "Arranca"
        else:
            print "No arranca"

    def conducir(self):
        if self.gasolina > 0:
            self.gasolina -= 1
            print "Quedan", self.gasolina, "litros"
        else:
            print "No se mueve"
            
            
if __name__ == '__main__':
    # Instanciar un coche
    coche = Coche(10)
    for x in range(11):
        coche.conducir()

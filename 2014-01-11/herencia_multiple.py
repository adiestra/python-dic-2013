#! -*- coding: utf-8 -*-

# Una jerarquia de clases
        
class Vehiculo(object):
   
   def desplazarse(self):
       pass
    
    
# Otra jerarquia que no tiene nada que ver

class Activo(object):
    
    def calcular_depreciacion_anual(self):
        pass


# Quizas en una empresa un vehiculo se tiene
# que depreciar contablemente

    
class Automovil(Vehiculo, Activo):
    pass
    


# -*- coding: utf-8 -*-

class DiccionarioPersonalizado(dict):

    def __getitem__(self, key):
        if len(key) == 1:
            raise KeyError(
                u'La llave no puede '
                u'tener longitud 1'
            )
        return super(
            DiccionarioPersonalizado, 
            self
        ).__getitem__(key)
        
if __name__ == '__main__':

    d = DiccionarioPersonalizado()
    d['abc'] = 10
    d['b'] = 20
    
    print d['abc']
    print d['b']

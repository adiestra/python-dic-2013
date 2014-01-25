#! -*- coding: utf-8 -*-

class DiccionarioRaro(object):

    def __init__(self):
        self.contador = 0

    def __getitem__(self, key):
        return 10
        
    def __setitem__(self, key, value):
        pass
        
    def __contains__(self, key):
        return True
        
    def __delitem__(self, key):
        pass
        
    def __len__(self):
        return 10
        
    def __iter__(self):
        return self
        
    def next(self):
        if self.contador > 10:
            self.contador = 0
            raise StopIteration
        self.contador += 1
        return 10


if __name__ == '__main__':

    d1 = DiccionarioRaro()
    
    print d1['Peru']
    print d1['Chile']
    print d1['Argentina']
    
    d1['Mexico'] = 100
    print d1['Mexico']

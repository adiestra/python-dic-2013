#! -*- coding: utf-8 -*-

class Vocales(object):

    def __init__(self):
        self.vocales = ['a', 'e', 'i', 'o', 'u']
        self.cursor = 0

    def next(self):
        try:
            valor = self.vocales[self.cursor]
        except IndexError:
            raise StopIteration
        self.cursor += 1
        return valor
        
    def __iter__(self):
        return self
        
        
if __name__ == '__main__':
    for x in Vocales():
        print x

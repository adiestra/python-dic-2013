#! -*- coding: utf-8 -*-

def f10(veces=10):
    i = 0
    while i < veces:
        yield True
        yield False
        i += 1


for x in f10():
    print x

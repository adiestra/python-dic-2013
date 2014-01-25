#! -*- coding: utf-8 -*-

def mprange(n):
    res = []
    i = 0
    while i < n:
        res.append(i)
        i += 1
    return res
    
for x in range(5):
    print x
    
for x in mprange(5):
    print x

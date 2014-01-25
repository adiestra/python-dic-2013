#! -*- coding: utf-8 -*-

def mpxrange(n):
    i = 0
    while i < n:
        yield i
        i += 1
        
for x in xrange(5):
    print x
    
for x in mpxrange(5):
    print x

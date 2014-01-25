# -*- coding: utf-8 -*-

c = 0
a = 0

while True:
    try:
        valor = int(raw_input("Ingrese nota: "))
        if valor >= 0 and valor <= 20:
            a += valor
            c += 1
        else:
            if valor == -1:
                break
            else:
                print(u"Solo valores entre 0 y 20 incluídos")
    except ValueError:
        print("Ingrese solo numeros")
        
print "la suma es: ", a
print "el contador es igual: ",  c
print "el promedio es igual: ",  a/float(c)


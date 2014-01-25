# -*- coding: utf-8 -*-
#
# Imprimir los numeros enteros positivos del 1 al 100
# excepto aquellos que sean disivibles por 7 o por 13
#

i = 1
while i <= 100:
    # i no debe ser divisible ni por 7 ni por 13
    if (i % 7 != 0) and (i % 13 != 0):
        print i
    i += 1

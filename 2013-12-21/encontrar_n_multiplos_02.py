# -*- coding: utf-8 -*-

# Encontrar los primeros N múltiplos enteros de un
# número M dado.
#
# El ejemplo simula bucle do-while de C.
#

n = 4
m = 17

i = 0
contador_multiplos = 0

while True:
	if (i % m == 0):
		print "%d es un divisor de %d" % (i, m)
		contador_multiplos += 1
	i += 1
	if contador_multiplos <= n:
		continue
	else:
	    break

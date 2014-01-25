# -*- coding: utf-8 -*-

# Encontrar los primeros N múltiplos enteros de un
# número M dado.

n = 5
m = 17

i = 0
contador_multiplos = 0

while contador_multiplos < n:
	if (i % m == 0):
		print "%d es un divisor de %d" % (i, m)
		contador_multiplos += 1
	i += 1

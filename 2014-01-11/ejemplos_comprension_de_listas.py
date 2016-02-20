#! -*- coding: utf-8 -*-

# Sintaxis:
# [{expresion} for {elemento} in {secuencia} [if {filtro}]]

print [x**2 for x in range(5) if x % 2 == 0]

print [p.upper() for p in [u'Pistola', u'Pelota', u'Lápiz'] if len(p) % 2 == 1]

# Sin utilizar listas por comprensión

por_imprimir = []

for p in [u'Pistola', u'Pelota', u'Lápiz']:
    if len(p) % 2 == 1:
        por_imprimir.append(p.upper())

print por_imprimir

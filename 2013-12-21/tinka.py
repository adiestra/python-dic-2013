# -*- coding: utf-8 -*-

import sys
from random import randint

BOLILLA_MINIMA = 1
BOLILLA_MAXIMA = 45

if len(sys.argv) != 2:
    print "Uso correcto: %s <numero de jugadas> " % sys.argv[0]
    sys.exit(1)
  
try:
    num_jugadas = int(sys.argv[1])
except ValueError:
    print u"El número de jugadas debe ser entero"
    sys.exit(1)
  
if num_jugadas < 0:
    print u"El número de jugadas debe ser un entero positivo"
    sys.exit(1)


lista_jugadas = []    


# Generar todas las jugadas
while len(lista_jugadas) < num_jugadas:

    # Generar una jugada
    jugada = []

    while len(jugada)<7:
        bolilla = randint(BOLILLA_MINIMA, BOLILLA_MAXIMA)
        if bolilla not in jugada:
            jugada.append(bolilla)        

    jugada = sorted(jugada)
    
    # Si la jugada generada no exista ya en las jugadas aceptadas
    if jugada not in lista_jugadas:
        lista_jugadas.append(jugada)


# Imprimir jugadas


for jugada in lista_jugadas:
    bolillas_como_cadena = []
    for bolilla in jugada:
        bolillas_como_cadena.append(str(bolilla)) 
    print "-".join(bolillas_como_cadena)
    #print "-".join([str(b) for b in jugada])

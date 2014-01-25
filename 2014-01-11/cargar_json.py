#! -*- coding: utf-8 -*-

import json

def cargar_json(ruta):
    archivo = open(ruta)
    contenido = ''.join(archivo.readlines())
    return json.loads(contenido)
    
if __name__ == '__main__':
    d = cargar_json('prueba.json')
    print d

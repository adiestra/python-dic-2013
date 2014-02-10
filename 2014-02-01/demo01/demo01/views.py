#! -*- coding: utf8 -*-

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render

def home(request):
    return HttpResponse("<h1>Home</h1>")
    
    
def saludar(request, nombre):
    return HttpResponse(u"<h1>Hola, %s ¿Cómo estas?" % nombre)
    
def detalle_catalogo_old(request, cod_categoria, cod_producto):
    return HttpResponse(
        u"<p>Categoria:%d</p><p>Producto:%d</p>" % (
            int(cod_categoria), #fragmentos del url
            int(cod_producto) #siempre son cadenas
        )
    ) 
    
def detalle_catalogo(request, cod_categoria, cod_producto, plantilla='detalle_catalogo.html'):
    contexto = {
      'cod_categoria': cod_categoria,
      'cod_producto': cod_producto
    }
    #print locals()
    
    return render(request, plantilla, contexto)
    
def detalle_catalogo_03(request, cod_categoria, cod_producto, plantilla='detalle_catalogo.html'):
    item = {
      'categoria': cod_categoria,
      'producto': cod_producto
    }
    contexto = {
      'item': item
    }
    #print locals()
    
    return render(request, plantilla, contexto)
    
    
def catalogo(request, plantilla='catalogo.html'):
    items = [
        {
            'categoria': 1,
            'producto': 10,
            'descripcion': 'Shampoo',
            'precio': 0.40
        },
        {
            'categoria': 1,
            'producto': 11,
            'descripcion': 'Lapicero',
            'precio': 0.50
        },
        {
            'categoria': 2,
            'producto': 22,
            'descripcion': 'Gaseosa Inca Kola 3 Lt.',
            'precio': 8.00
        }
    ]
    #items = []
    contexto = {
      'items': items,
      'fragmento_html': "<script>alert('Hola');</script>"
    }
    #print locals()
    
    return render(request, plantilla, contexto)
    
    
def redirigir_a_google(request):
    return HttpResponseRedirect("http://www.google.com.pe")

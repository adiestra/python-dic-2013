# -*- encoding: utf8 -*-

from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from demo04.decorators import mi_login_required_403
from demo04.decorators import mi_login_required_redirect

def hola(request):
    mensaje = u"<h1>Hola</h1>"
    if request.user.is_authenticated():
        mensaje += u'<p>El usuario %s llegó al view</p>' % request.user.username
    else:
        mensaje += u'<p>Un usuario anonimo llegó al view</p>'
    return HttpResponse(mensaje)
    
    
def mostrar_ip(request):
    ip = request.ip # Que viene del middle PonerIpMiddleware
    return HttpResponse("<h1>Tu IP es %s</h1>" % ip)
    
#@login_required
#@mi_login_required_403
@mi_login_required_redirect
def dashboard(request):
    return render(request, 'dashboard.html')

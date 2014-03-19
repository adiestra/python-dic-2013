from django.http import HttpResponseForbidden
from django.http import HttpResponseRedirect
from django.core.exceptions import PermissionDenied
from django.conf import settings

def mi_login_required_403(f):
    def aux(request, *args, **kwargs):
        if not request.user.is_authenticated():
           #return HttpResponseForbidden("<h1>Prohibido</h1>")
           raise PermissionDenied
        return f(request, *args, **kwargs)
    return aux
    
    
def mi_login_required_redirect(f):
    def aux(request, *args, **kwargs):
        if not request.user.is_authenticated():
           return HttpResponseRedirect(settings.LOGIN_URL)
        return f(request, *args, **kwargs)
    return aux

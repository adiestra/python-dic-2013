from django.http import HttpResponse

class PonerIpMiddleware(object):

    def process_request(self, request):
        request.ip = request.META['REMOTE_ADDR']
        
class Devuelvo200AlToqueMiddleware(object):

    def process_request(self, request):
        return HttpResponse('<h1>Soy el middleware!!</h1>')
        
        
class AgregarCabeceraSaludoMiddleware(object):

    def process_response(self, request, response):
        response['X-Saludo'] = 'Chau'
        return response

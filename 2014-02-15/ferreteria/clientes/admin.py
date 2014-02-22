from django.contrib import admin
from clientes.models import Cliente

# Register your models here.


class ClienteAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'nombre', 'tipo_persona', 
        'documento', 'tipo_documento'
    )
    list_search = ('nombre', 'documento'),
    list_filter = ('tipo_persona', 'tipo_documento', )

admin.site.register(Cliente, ClienteAdmin)

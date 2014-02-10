from django.contrib import admin

from productos.models import Categoria
from productos.models import Producto

# Register your models here.

admin.site.register(Categoria)
admin.site.register(Producto)

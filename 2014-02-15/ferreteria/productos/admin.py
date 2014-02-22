from django.contrib import admin
from django.utils.translation import ugettext as _

from productos.models import Categoria
from productos.models import Producto

# Register your models here.


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'productos_en_categoria')
    
    def productos_en_categoria(self, instance):
        return instance.productos.count()
    productos_en_categoria.short_description = _(u'Productos')
    

admin.site.register(Categoria, CategoriaAdmin)


class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'categoria', 'precio', 'stock', )
    list_filter = ('categoria', )
    search_fields = ('nombre', )
     

admin.site.register(Producto, ProductoAdmin)

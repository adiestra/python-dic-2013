from django.contrib import admin

from ventas.models import Boleta, DetalleBoleta
from ventas.models import Factura, DetalleFactura

# Register your models here.

class DetalleBoletaInline(admin.StackedInline):
    model = DetalleBoleta

class BoletaAdmin(admin.ModelAdmin):
    readonly_fields = ('codigo', 'monto', )
    inlines = [DetalleBoletaInline]

admin.site.register(Boleta, BoletaAdmin)

class DetalleBoletaAdmin(admin.ModelAdmin):
    readonly_fields = ('precio_unitario', )


admin.site.register(DetalleBoleta, DetalleBoletaAdmin)

admin.site.register(Factura)
admin.site.register(DetalleFactura)

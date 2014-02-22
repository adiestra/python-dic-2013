# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext as _

from clientes.models import Cliente
from productos.models import Producto

from ventas import settings as ventas_settings

# Create your models here.

class DocumentoVenta(models.Model):

    cliente = models.ForeignKey(Cliente)

    monto = models.DecimalField(
        verbose_name=_(u'Monto'),
        max_digits=5,
        decimal_places=2
    )

    anulada = models.BooleanField(
        verbose_name=_(u'Anulada'),
        default=False
    )

    fecha_emision = models.DateTimeField(
        verbose_name=_(u'Fecha de emisión'),
        auto_now_add=True
    )

    class Meta:
        abstract = True
        
        
    def calcular_subtotal_general(self):
        resultado = None
        for detalle in self.detalles.all():
            if resultado is None:
                resultado = detalle.calcular_subtotal()
            else:
                resultado += detalle.calcular_subtotal()
        # resultado = sum([d.calcular_subtotal() for d in self.detalles.all()], 0.0)
        return resultado
        
        
class Detalle(models.Model):

    producto = models.ForeignKey(Producto)
    
    cantidad = models.PositiveIntegerField(
        verbose_name=_(u'Cantidad'),
        default=1
    )
    
    precio_unitario = models.DecimalField(
        verbose_name=_(u'Precio unitario'),
        max_digits=5, 
        decimal_places=2
    )
    
    class Meta:
        abstract = True
        
    def calcular_subtotal(self):
        return self.cantidad * self.precio_unitario
        
    def obtener_precio_unitario(self):
        return self.producto.precio
        
    def save(self, *args, **kwargs):
        self.precio_unitario = self.obtener_precio_unitario()
        return super(Detalle, self).save(*args, **kwargs)
        
        
class Boleta(DocumentoVenta):
    
    codigo = models.CharField(
        verbose_name=_(u'Número de boleta'),
        max_length=32,
        unique=True
    )
    
    class Meta:
        verbose_name = _(u'Boleta')
        verbose_name_plural = _(u'Boletas')
            
    @staticmethod
    def generar_codigo():
        num_boletas = Boleta.objects.count()
        return '%s-%06d' % (
            ventas_settings.PREFIJO_BOLETA,
            num_boletas + 1
        )
        
    def save(self, *args, **kwargs):
        if self.codigo is None:
            self.codigo = Boleta.generar_codigo()
        self.monto = self.calcular_subtotal_general()
        super(Boleta,self).save(*args, **kwargs)

    def __unicode__(self):
        return self.codigo

class DetalleBoleta(Detalle):

    boleta = models.ForeignKey(Boleta, 
        related_name='detalles'
    )

    class Meta:
        verbose_name = _(u'Detalle de boleta')
        verbose_name_plural = _(u'Detalles de boleta')


        
class Factura(DocumentoVenta):
    
    codigo = models.CharField(
        verbose_name=_(u'Número de factura'),
        max_length=32,
        unique=True
    )
    
    igv = models.DecimalField(
        verbose_name=_(u'I.G.V.'),
        max_digits=5,
        decimal_places=2
    )
    
    class Meta:
        verbose_name = _(u'Factura')
        verbose_name_plural = _(u'Facturas')


class DetalleFactura(Detalle):

    factura = models.ForeignKey(Factura,
        related_name='detalles'
    )

    class Meta:
        verbose_name = _(u'Detalle de factura')
        verbose_name_plural = _(u'Detalles de factura')


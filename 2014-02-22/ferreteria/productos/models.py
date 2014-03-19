# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext as _

# Create your models here.

class Categoria(models.Model):

    nombre = models.CharField(
        verbose_name=_(u'Nombre'),
        max_length=64,
        unique=True
    )
    
    fecha_creacion = models.DateTimeField(
        verbose_name=_(u'Fecha de creación'),
        auto_now_add=True
    )
    
    fecha_modificacion = models.DateTimeField(
        verbose_name=_(u'Fecha de modificación'),
        auto_now=True
    )
    
    def __unicode__(self):
        return self.nombre
    
    

class ProductoManager(models.Manager):
    
    def en_stock(self):
        return self.filter(stock__gte=1)


class Producto(models.Model):

    categoria = models.ForeignKey(Categoria,
        related_name='productos'
    )

    nombre = models.CharField(
        verbose_name=_(u'Nombre'),
        max_length=64,
        unique=True
    )
    
    precio = models.DecimalField(
        verbose_name=_(u'Precio'),
        max_digits=5, 
        decimal_places=2
    )
    
    stock = models.PositiveIntegerField(
        verbose_name=_('Cantidad en stock'),
        default=0
    )
    
    fecha_creacion = models.DateTimeField(
        verbose_name=_(u'Fecha de creación'),
        auto_now_add=True
    )
    
    fecha_modificacion = models.DateTimeField(
        verbose_name=_(u'Fecha de modificación'),
        auto_now=True
    )
    
    objects = ProductoManager()
    
    def __unicode__(self):
        return self.nombre
        
    class Meta:
        verbose_name = _(u'Producto')
        verbose_name_plural = _(u'Productos')

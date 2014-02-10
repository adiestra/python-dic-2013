# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.

class Categoria(models.Model):

    nombre = models.CharField(
        verbose_name=u'Nombre',
        max_length=64,
        unique=True
    )
    
    fecha_creacion = models.DateTimeField(
        verbose_name=u'Fecha de creación',
        auto_now_add=True
    )
    
    fecha_modificacion = models.DateTimeField(
        verbose_name=u'Fecha de modificación',
        auto_now=True
    )
    
    def __unicode__(self):
        return self.nombre
    
    

class Producto(models.Model):

    categoria = models.ForeignKey(Categoria)

    nombre = models.CharField(
        verbose_name=u'Nombre',
        max_length=64,
        unique=True
    )
    
    precio = models.DecimalField(
        verbose_name=u'Precio',
        max_digits=5, 
        decimal_places=2
    )
    
    stock = models.PositiveIntegerField(
        verbose_name='Cantidad en stock',
        default=0
    )
    
    fecha_creacion = models.DateTimeField(
        verbose_name=u'Fecha de creación',
        auto_now_add=True
    )
    
    fecha_modificacion = models.DateTimeField(
        verbose_name=u'Fecha de modificación',
        auto_now=True
    )
    
    def __unicode__(self):
        return self.nombre
    


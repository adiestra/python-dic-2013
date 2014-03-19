# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext as _

# Create your models here.

class Cliente(models.Model):

    TIPO_CLIENTE_CHOICES = (
        (1, _(u'Persona natural')),
        (2, _(u'Persona jurídica'))
    )
    
    TIPO_DOCUMENTO_CHOICES = (
        (1, _(u'RUC')),
        (2, _(u'DNI')),
        (3, _(u'Carnet de extranjería')),
        (4, _(u'Pasaporte'))
    )

    nombre = models.CharField(
        verbose_name=_(u'Nombre o Razón Social'),
        max_length = 64
    )
    
    tipo_persona = models.PositiveIntegerField(
        verbose_name=_(u'Tipo de persona'),
        choices=TIPO_CLIENTE_CHOICES
    )
    
    documento = models.CharField(
        verbose_name=_(u'Documento'),
        max_length = 32
    )
    
    tipo_documento = models.PositiveIntegerField(
        verbose_name=_(u'Tipo de documento'),
        choices=TIPO_DOCUMENTO_CHOICES
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
    
    class Meta:
        verbose_name = _(u'Cliente')
        verbose_name_plural = _(u'Clientes')
        unique_together = (('documento', 'tipo_documento'), )

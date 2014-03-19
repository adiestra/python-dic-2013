# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Factura.igv'
        db.add_column(u'ventas_factura', 'igv',
                      self.gf('django.db.models.fields.DecimalField')(default=0.0, max_digits=5, decimal_places=2),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Factura.igv'
        db.delete_column(u'ventas_factura', 'igv')


    models = {
        u'clientes.cliente': {
            'Meta': {'unique_together': "(('documento', 'tipo_documento'),)", 'object_name': 'Cliente'},
            'documento': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'fecha_creacion': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'fecha_modificacion': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'tipo_documento': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'tipo_persona': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
        u'ventas.boleta': {
            'Meta': {'object_name': 'Boleta'},
            'anulada': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'cliente': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['clientes.Cliente']"}),
            'codigo': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '32'}),
            'fecha_emision': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'monto': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'})
        },
        u'ventas.factura': {
            'Meta': {'object_name': 'Factura'},
            'anulada': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'cliente': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['clientes.Cliente']"}),
            'codigo': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '32'}),
            'fecha_emision': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'igv': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'monto': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'})
        }
    }

    complete_apps = ['ventas']
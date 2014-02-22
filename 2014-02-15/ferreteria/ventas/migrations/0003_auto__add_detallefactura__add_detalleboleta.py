# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'DetalleFactura'
        db.create_table(u'ventas_detallefactura', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('producto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['productos.Producto'])),
            ('cantidad', self.gf('django.db.models.fields.PositiveIntegerField')(default=1)),
            ('precio_unitario', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
            ('factura', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ventas.Factura'])),
        ))
        db.send_create_signal(u'ventas', ['DetalleFactura'])

        # Adding model 'DetalleBoleta'
        db.create_table(u'ventas_detalleboleta', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('producto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['productos.Producto'])),
            ('cantidad', self.gf('django.db.models.fields.PositiveIntegerField')(default=1)),
            ('precio_unitario', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
            ('boleta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ventas.Boleta'])),
        ))
        db.send_create_signal(u'ventas', ['DetalleBoleta'])


    def backwards(self, orm):
        # Deleting model 'DetalleFactura'
        db.delete_table(u'ventas_detallefactura')

        # Deleting model 'DetalleBoleta'
        db.delete_table(u'ventas_detalleboleta')


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
        u'productos.categoria': {
            'Meta': {'object_name': 'Categoria'},
            'fecha_creacion': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'fecha_modificacion': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'})
        },
        u'productos.producto': {
            'Meta': {'object_name': 'Producto'},
            'categoria': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'productos'", 'to': u"orm['productos.Categoria']"}),
            'fecha_creacion': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'fecha_modificacion': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'}),
            'precio': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'stock': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
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
        u'ventas.detalleboleta': {
            'Meta': {'object_name': 'DetalleBoleta'},
            'boleta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ventas.Boleta']"}),
            'cantidad': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'precio_unitario': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'producto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['productos.Producto']"})
        },
        u'ventas.detallefactura': {
            'Meta': {'object_name': 'DetalleFactura'},
            'cantidad': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'factura': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ventas.Factura']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'precio_unitario': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'producto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['productos.Producto']"})
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
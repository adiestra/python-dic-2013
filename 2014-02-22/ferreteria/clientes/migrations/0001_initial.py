# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Cliente'
        db.create_table(u'clientes_cliente', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('tipo_persona', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('documento', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('tipo_documento', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('fecha_creacion', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('fecha_modificacion', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'clientes', ['Cliente'])

        # Adding unique constraint on 'Cliente', fields ['documento', 'tipo_documento']
        db.create_unique(u'clientes_cliente', ['documento', 'tipo_documento'])


    def backwards(self, orm):
        # Removing unique constraint on 'Cliente', fields ['documento', 'tipo_documento']
        db.delete_unique(u'clientes_cliente', ['documento', 'tipo_documento'])

        # Deleting model 'Cliente'
        db.delete_table(u'clientes_cliente')


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
        }
    }

    complete_apps = ['clientes']
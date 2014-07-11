# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Calculo'
        db.create_table('campuskit_calculo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nun1', self.gf('django.db.models.fields.IntegerField')()),
            ('nun2', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('campuskit', ['Calculo'])


    def backwards(self, orm):
        # Deleting model 'Calculo'
        db.delete_table('campuskit_calculo')


    models = {
        'campuskit.blogabout': {
            'Meta': {'object_name': 'blogAbout'},
            'contenido': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'campuskit.calculo': {
            'Meta': {'object_name': 'Calculo'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nun1': ('django.db.models.fields.IntegerField', [], {}),
            'nun2': ('django.db.models.fields.IntegerField', [], {})
        },
        'campuskit.cliente': {
            'Meta': {'object_name': 'cliente'},
            'apellidos': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'status': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        'campuskit.producto': {
            'Meta': {'object_name': 'producto'},
            'descripcion': ('django.db.models.fields.TextField', [], {'max_length': '300'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'status': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        }
    }

    complete_apps = ['campuskit']
# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'cliente'
        db.create_table('campuskit_cliente', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('apellidos', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('status', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('campuskit', ['cliente'])

        # Adding model 'producto'
        db.create_table('campuskit_producto', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('descripcion', self.gf('django.db.models.fields.TextField')(max_length=300)),
            ('status', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('campuskit', ['producto'])

        # Adding model 'blogAbout'
        db.create_table('campuskit_blogabout', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('contenido', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('campuskit', ['blogAbout'])


    def backwards(self, orm):
        # Deleting model 'cliente'
        db.delete_table('campuskit_cliente')

        # Deleting model 'producto'
        db.delete_table('campuskit_producto')

        # Deleting model 'blogAbout'
        db.delete_table('campuskit_blogabout')


    models = {
        'campuskit.blogabout': {
            'Meta': {'object_name': 'blogAbout'},
            'contenido': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '100'})
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
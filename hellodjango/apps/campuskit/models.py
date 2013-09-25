#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.


class cliente(models.Model):
    nombre = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=200)
    status = models.BooleanField(default=True)

    def __unicode__(self):
        nombreCompleto = "%s %s" % (self.nombre, self.apellidos)
        return nombreCompleto


class producto(models.Model):
    """docstring for producto"""
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=300)
    status = models.BooleanField(default=True)

    def __unicode__(self):
        return self.nombre
'''
class Datos(models.Model):
            """docstring for Datos"""
    nombres = models.CharField(max_length=150)
    apellidos = models.CharField(max_length=150)
    numeros = models.IntegerField()
    direccion = models.CharField(max_length=150)

            def __unicode__(self):
                return "%s %S" % (self.nombres, self.apellidos)
'''

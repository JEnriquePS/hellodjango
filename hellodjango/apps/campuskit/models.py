#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models


class Calculo(models.Model):
    """calculadora"""
    nun1 = models.IntegerField()
    nun2 = models.IntegerField()
    nun = models.IntegerField()


class cliente(models.Model):
    nombre = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=200)
    status = models.BooleanField(default=True)

    def __unicode__(self):
        nombreCompleto = "%s %s" % (self.nombre, self.apellidos)
        return nombreCompleto


class producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=300)
    status = models.BooleanField(default=True)

    def __unicode__(self):
        return self.nombre


class blogAbout(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    #imagen = models.ImageField(upload_to='images')

    def __unicode__(self):
        return self.titulo

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.

class Datos(models.Model):
	"""docstring for Datos"""
	nombres = models.CharField(max_length=150)
	apellidos = models.CharField(max_length=150)
	numeros = models.IntegerField()
	direccion = models.CharField(max_length=150)

	def __unicode__(self):
		return "%s %S" % (self.nombres, self.apellidos)
		

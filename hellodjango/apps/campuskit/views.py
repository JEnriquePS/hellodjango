#!/usr/bin/env python
# -*- coding: utf-8 -*-

#from django.http import HttpResponse
#from django.template import loader, Context
from django.shortcuts import render_to_response


def index(request):
    return render_to_response("base.html")

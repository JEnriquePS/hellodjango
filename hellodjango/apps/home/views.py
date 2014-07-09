#from django.http import HttpResponse
#from datetime import datetime
from django.shortcuts import render_to_response
from django.template import RequestContext
from hellodjango.apps.campuskit.models import producto
from hellodjango.apps.home.forms import ContactForm


# def hora_actual_view(request):
#     """Clasico Funcion de la obtener la hora"""
#     ahora = datetime.now()
#     html = "<html><body> esta es la hora {}</body></html>".format(ahora)
#     return HttpResponse(html)


def jenriqueps_view(request):
    return render_to_response('home/jenriqueps.html',
                              context_instance=RequestContext(request)
                              )


def index_view(request):
    return render_to_response('home/index.html',
                              context_instance=RequestContext(request)
                              )


def about_view(request):
    mensaje = "esto es un mensaje desde mi vista"
    ctx = {'msj': mensaje}
    return render_to_response('home/about.html', ctx,
                              context_instance=RequestContext(request)
                              )


def productos_view(request):
    prod = producto.objects.filter(status=True)
    ctx = {'productos': prod}
    return render_to_response('home/productos.html', ctx,
                              context_instance=RequestContext(request))


def contacto_view(request):
    info_enviado = False
    email = ""
    titulo = ""
    texto = ""
    if request.method == "POST":
        formulario = ContactForm(request.POST)
        if formulario.is_valid():
            info_enviado = True
            email = formulario.cleaned_data['Email']
            titulo = formulario.cleaned_data['Titulo']
            texto = formulario.cleaned_data['Texto']
    else:
        formulario = ContactForm()
    ctx = {'form': formulario,
           'email': email,
           'titulo': titulo,
           'texto': texto,
           'info_enviado': info_enviado}
    return render_to_response('home/contacto.html', ctx,
                              context_instance=RequestContext(request))

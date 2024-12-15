from django.shortcuts import render, redirect
from platos.models import Plato

from django.core import serializers
from django.http import HttpResponse

# Create your views here.

def lista_platos(request):
    query = Plato.objects.filter(pais__icontains='Peru', precio__gt=40)[0:3]
    return render(request, 'platos/lista_platos.html', context={'data': query})

def eliminar_platos(request):
    plato = Plato.objects.filter(precio__lt=15)
    plato.delete()
    return redirect('lista_platos')


def listaplatosserializer(request):
    lista_platos_50 = serializers.serialize('json', Plato.objects.filter(precio__gte=50), fields=['nombre', 'pais', 'precio', 'procedencia'])
    return HttpResponse(lista_platos_50, content_type='application/json')
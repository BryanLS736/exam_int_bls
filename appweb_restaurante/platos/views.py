from django.shortcuts import render, redirect
from platos.models import Plato


# Create your views here.

def lista_platos(request):
    query = Plato.objects.filter(pais__icontains='Peru', precio__gt=40)[0:3]
    return render(request, 'platos/lista_platos.html', context={'data': query})

def eliminar_platos(request):
    plato = Plato.objects.filter(precio__lt=15)
    plato.delete()
    return redirect('lista_platos')

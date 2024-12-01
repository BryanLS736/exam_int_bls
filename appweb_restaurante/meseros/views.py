from django.shortcuts import render, redirect
from meseros.models import Mesero
from django.db.models import F

# Create your views here.

def lista_meseros(request):
    query =Mesero.objects.filter(nacionalidad__icontains='Peru', edad__lt=30)
    return render(request, 'meseros/lista_meseros.html', context={'data':query})

def meseros_aumentar_edad(request):
    edades = Mesero.objects.all().update(edad=F('edad')+5)
    return redirect('lista_meseros')

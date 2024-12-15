from django.shortcuts import render, redirect
from meseros.forms import MeseroForm
from meseros.models import Mesero
from django.db.models import F

from django.core import serializers
from django.http import HttpResponse

from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from meseros.serializers import MeseroSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

# Create your views here.

def lista_meseros_all(request):
    query = Mesero.objects.all()
    return render(request, 'meseros/lista_meseros_all.html', context={'data': query})


def lista_meseros(request):
    query =Mesero.objects.filter(nacionalidad__icontains='Peru', edad__lt=30)
    return render(request, 'meseros/lista_meseros.html', context={'data':query})


def meseros_aumentar_edad(request):
    edades = Mesero.objects.all().update(edad=F('edad')+5)
    return redirect('lista_meseros')


def listaserializer(request):
    lista_meseros_25 = serializers.serialize('json', Mesero.objects.filter(edad__gt=25), fields=['nombre', 'nacionalidad', 'edad', 'dni'])
    return HttpResponse(lista_meseros_25, content_type='application/json')


class ListaMeserosVBC(ListView):
    model = Mesero
    template_name = 'meseros/lista_meseros_vbc.html'


class CrearMeserosVBC(CreateView):
    model = Mesero
    form_class = MeseroForm
    template_name = 'meseros/crear_meseros.html'
    success_url = reverse_lazy('lista_meseros_vbc')


class EditarMeserosVBC(UpdateView):
    model = Mesero
    form_class = MeseroForm
    template_name = 'meseros/editar_meseros.html'
    success_url = reverse_lazy('meseros_all')


class EliminarMeserosVBC(DeleteView):
    model = Mesero
    template_name = 'meseros/eliminar_meseros.html'
    success_url = reverse_lazy('meseros_all')


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def mesero_api_view(request):
    if request.method == 'GET':
        query = Mesero.objects.all()
        serializer_class = MeseroSerializer(query,many=True)
        return Response(serializer_class.data, status=status.HTTP_202_ACCEPTED)

    elif request.method == 'POST':
        serializer_class = MeseroSerializer(data=request.data)

        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data, status=status.HTTP_201_CREATED)

        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def meseros_api_editar(request, pk):
    mesero = Mesero.objects.get(id=pk)

    if mesero:
        if request.method == 'GET':
            serializers_class = MeseroSerializer(mesero)
            return Response(serializers_class.data, status=status.HTTP_200_OK)

        elif request.method == 'PUT':
            serializers_class = MeseroSerializer(mesero, data=request.data)

            if serializers_class.is_valid():
                serializers_class.save()
                return Response(serializers_class.data, status=status.HTTP_202_ACCEPTED)

            return Response(serializers_class.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            mesero.delete()
            return Response(f'El mesero {mesero.nombre} ha sido eliminado por completo de la BD.', status=status.HTTP_202_ACCEPTED)

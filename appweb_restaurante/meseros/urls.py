from django.urls import path
from . import views

urlpatterns = [
    path('lista_meseros/', views.lista_meseros, name='lista_meseros'),
    path('meseros_aumentar_edad/', views.meseros_aumentar_edad, name='meseros_aumentar_edad'),
]

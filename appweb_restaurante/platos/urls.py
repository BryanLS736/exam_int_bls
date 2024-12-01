from django.urls import path
from . import views

urlpatterns = [
    path('lista_platos/', views.lista_platos, name='lista_platos'),
    path('eliminar_platos/', views.eliminar_platos, name='eliminar_platos'),
]

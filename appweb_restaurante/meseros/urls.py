from django.urls import path
from . import views

urlpatterns = [
    path('lista_meseros_all', views.lista_meseros_all, name='meseros_all'),
    path('lista_meseros/', views.lista_meseros, name='lista_meseros'),
    path('meseros_aumentar_edad/', views.meseros_aumentar_edad, name='meseros_aumentar_edad'),
    path('lista_serializer_meseros/', views.listaserializer, name='lista_serializer_meseros'),

    # Vistas basadas en clase
    path('lista_meseros_vbc', views.ListaMeserosVBC.as_view(), name='lista_meseros'),
    path('crear_meseros_vbc', views.CrearMeserosVBC.as_view(), name='crear_meseros'),
    path('editar_meseros_vbc/<int:pk>', views.EditarMeserosVBC.as_view(), name='editar_meseros'),
    path('eliminar_meseros_vbc/<int:pk>', views.EliminarMeserosVBC.as_view(), name='eliminar_meseros'),

    # Url rest_framework (DRF)
    path('mesero_view_drf', views.mesero_api_view, name='mesero_view_drf'),
    path('mesero_editar_drf/<int:pk>', views.meseros_api_editar, name='mesero_editar_drf'),
]

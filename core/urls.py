from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('catalogo/', views.catalogo, name='catalogo'),
    path('lugar/<int:lugar_id>/', views.detalle_lugar, name='detalle_lugar'),
    path('gestion/', views.gestion_lugares, name='gestion_lugares'),
    path('gestion/nuevo/', views.agregar_lugar, name='agregar_lugar'),
    path('gestion/editar/<int:lugar_id>/', views.editar_lugar, name='editar_lugar'),
    path('gestion/eliminar/<int:lugar_id>/', views.eliminar_lugar, name='eliminar_lugar'),
    path('accounts/registro/', views.registro, name='registro'),
]
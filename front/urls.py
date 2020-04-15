from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('distance', views.distance, name='distance'),
    path('distances', views.distanceSoap, name ='distances'),
    path('mesvoyages', views.mesvoyages, name='MesVoyages'),
    path('recherche', views.rechercher, name='Recherche'),
]
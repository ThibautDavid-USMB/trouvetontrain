from django.urls import path, include, re_path
from . import views

from django.urls import path, include, re_path
from spyne.protocol.soap import Soap11
from spyne.server.django import DjangoView
from .views import distance_service, app, Distance

urlpatterns = [
   re_path(r'^distance', DjangoView.as_view(
        services=[Distance], tns='trouvetontrain.api.distance.calcul',
        in_protocol=Soap11(validator='lxml'), out_protocol=Soap11(),
        cache_wsdl=False)),
]
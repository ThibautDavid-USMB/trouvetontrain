from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

#Import spyne module for soap
from spyne.server.django import DjangoApplication
from spyne.model.primitive import Double
from spyne.service import Service
from spyne.protocol.soap import Soap11
from spyne.application import Application
from spyne.decorator import rpc

from math import radians, sin, cos, atan2, sqrt


class Distance(Service):
    @rpc(Double, Double, Double, Double, _returns=Double)
    def calcul(self,lat1,long1,lat2,long2):
        # approximate radius of earth in km
        R = 6373.0

        lat1 = radians(lat1)
        long1 = radians(long1)

        lat2 = radians(lat2)
        long2 = radians(long2)

        deltalong = long2 - long1
        deltalat = lat2 - lat1

        a = sin(deltalat / 2)**2 + cos(lat1) * cos(lat2) * sin(deltalong / 2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))

        distance = R * c

        distance = round(distance, 2)

        return distance

app = Application([Distance],
    'trouvetontrain.api.distance.calcul',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11(),
)

distance_service = csrf_exempt(DjangoApplication(app))

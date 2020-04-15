from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render
from zeep import Client
from math import radians, sin, cos, sqrt, atan2
import requests

import json

def index(request):
    return render(request, 'index.html')

def distance(request):
    return render(request, 'distance.html')

def mesvoyages(request):
    return render(request, 'mesVoyages.html')

def recherche(request):
    return render(request, 'recherche.html')

def devise(request):
        search_result = {}
        
        #appel de notre api pour calculer le prix
        urlprix = 'http://localhost:5000/prix?distance='+distance+'&devise='+devise
        prixjson = requests.get(urlprix)
        prix = prixjson.json()

def rechercher(request):
    search_result = {}
    token_auth = '040b7667-1a01-437e-9f4a-4dc61ef3f405'
    if 'depart' and 'arriver' in request.GET:
        #récupération de l'oid et coord de la gare de depart
        depart = request.GET['depart']
        depart = depart.replace(" ","+")
        urldepart = 'https://ressources.data.sncf.com/api/records/1.0/search/?dataset=referentiel-gares-voyageurs&q='+depart
        departjson = requests.get(urldepart)
        departobj = departjson.json()
        departobj = departobj.get("records")
        departobj = departobj[0]
        departobj = departobj.get("fields")
        departoid = departobj.get("pltf_uic_code")
        departlong = departobj.get("pltf_longitude_entreeprincipale_wgs84")
        departlong = float(departlong)
        departlat = departobj.get("pltf_latitude_entreeprincipale_wgs84")
        departlat = float(departlat)

        #récupération de l'oid et coord de la gare d'arriver
        arriver = request.GET['arriver']
        arriver = arriver.replace(" ","+")
        urlarriver = 'https://ressources.data.sncf.com/api/records/1.0/search/?dataset=referentiel-gares-voyageurs&q='+arriver
        arriverjson = requests.get(urlarriver)
        arriverobj = arriverjson.json()
        arriverobj = arriverobj.get("records")
        arriverobj = arriverobj[0]
        arriverobj = arriverobj.get("fields")
        arriveroid = arriverobj.get("pltf_uic_code")
        arriverlong = arriverobj.get("pltf_longitude_entreeprincipale_wgs84")
        arriverlong = float(arriverlong)
        arriverlat = arriverobj.get("pltf_latitude_entreeprincipale_wgs84")
        arriverlat = float(arriverlat)

        #formatage de date pour l'api
        date = request.GET['datetimepicker4']
        date = date[12:16]+date[6:8]+date[9:11]+'T'+date[0:2]+date[3:5]+"00"

        #calcul de la distance
        R = 6373.137
        lat1 = radians(departlat)
        lon1 = radians(departlong)
        lat2 = radians(arriverlat)
        lon2 = radians(arriverlong)
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        distance = R * c
        
        #appel de notre api pour calculer le prix on recherche le prix en euro par défaut
        distance = str(distance)
        urlprix = 'http://localhost:5000/prix?distance='+distance+'&devise=euro'
        prixjson = requests.get(urlprix)
        prix = prixjson.json()

        #requetage de l'api sncf pour récupéré les 10 trajets après l'heure indiqué
        darriver = []
        ddepart = []

        dico = dict()
        for i in range(1,11):
            urltrajet = 'https://api.sncf.com/v1/coverage/sncf/journeys?from=stop_area%3AOCE%3ASA%3A'+str(departoid)+'&to=stop_area%3AOCE%3ASA%3A'+str(arriveroid)+'&datetime='+str(date)+'&datetime_represents=departure&data_freshness=realtime&key='+str(token_auth)
            trajetjson = requests.get(urltrajet)
            trajetobj = trajetjson.json()
            trajetobj = trajetobj.get("journeys")
            trajetobj = trajetobj[0]
            formatageddep = str(trajetobj.get("departure_date_time"))
            formatageddep = formatageddep[6:8]+"/"+formatageddep[4:6]+" à "+formatageddep[9:11]+"h"+formatageddep[12:14]
            dico["departure_date_time"+str(i)] = formatageddep
            formatagedarr = str(trajetobj.get("arrival_date_time")) 
            formatagedarr = formatagedarr[6:8]+"/"+formatagedarr[4:6]+" à "+formatagedarr[9:11]+"h"+formatagedarr[12:14]
            dico["arrival_date_time"+str(i)] = formatagedarr
            date = str(trajetobj.get("arrival_date_time"))
        
    #défniition d'un dictionnaire pour initialiser les variables dans mon template hmtl

    dico["depart"] = depart.replace("+", " ")
    dico["arriver"] = arriver.replace("+", " ")
    dico["prix"] = float(int(prix*100))/100
    dico["distance"] = round(float(distance),2)
        
    #on retourne le template recherche avec le dico en parametre pour initialiser les valeurs récupére de l'api sncf
    return render(request, 'recherche.html', dico)

#Appel de l'API Soap()

def distanceSoap(request):
    latd = request.GET['latd']
    longd = request.GET['longd']
    lata = request.GET['lata']
    longa = request.GET['longa']
    
    client = Client('http://localhost:8000/api/distance?wsdl')
    distance = client.service.calcul(latd,longd,lata,longa)
    #Mise des variables dans un dico pour l'associer au code html
    resultat = dict()
    resultat['distance'] = distance
    return render(request, 'distance.html', resultat)    
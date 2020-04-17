from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render
from .models import Trajet
#import des library pour le client SOAP
from zeep import Client
from math import radians, sin, cos, sqrt, atan2
import requests
import json

"""
#Création d'une classe pour enregistrer les données de recherche 
class ResultatRecherche:
    def __init__(self, depart, arriver, dateDepart, dateArriver, distance, prix):   
        self.depart = depart
        self.arriver = arriver
        self.dateDepart = dateDepart
        self.dateArriver = dateArriver
        self.distance = distance
        self.prix = prix
"""
def index(request):
    return render(request, 'index.html')

def distance(request):
    return render(request, 'distance.html')

def mesvoyages(request):
    trajets = Trajet.objects.filter(session=request.session.session_key)
    return render(request, 'mesVoyages.html', {'trajets' : trajets})

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
        depart = depart.replace(" - ","+")
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
        arriver = arriver.replace(" - ","+")
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

        #appel de l'API SOAP pour calculer la distance 
        client = Client('http://localhost:8000/api/distance?wsdl')
        distance = client.service.calcul(departlat,departlong,arriverlat,arriverlong)

        #appel de notre api pour calculer le prix on recherche le prix en euro par défaut
        distance = str(distance)
        urlprix = 'http://localhost:5000/prix?distance='+distance+'&devise=euro'
        prixjson = requests.get(urlprix)
        prix = prixjson.json()


        #requetage de l'api sncf pour récupéré les 10 trajets après l'heure indiqué
        darriver = []
        ddepart = []
        """
        listeTrajet = dict()
        trajet = dict()
        for i in range(1,11):
            urltrajet = 'https://api.sncf.com/v1/coverage/sncf/journeys?from=stop_area%3AOCE%3ASA%3A'+str(departoid)+'&to=stop_area%3AOCE%3ASA%3A'+str(arriveroid)+'&datetime='+str(date)+'&datetime_represents=departure&data_freshness=realtime&key='+str(token_auth)
            trajetjson = requests.get(urltrajet)
            trajetobj = trajetjson.json()
            trajetobj = trajetobj.get("journeys")
            trajetobj = trajetobj[0]
            formatageddep = str(trajetobj.get("departure_date_time"))
            formatageddep = formatageddep[6:8]+"/"+formatageddep[4:6]+" à "+formatageddep[9:11]+"h"+formatageddep[11:13]
            formatagedarr = str(trajetobj.get("arrival_date_time")) 
            formatagedarr = formatagedarr[6:8]+"/"+formatagedarr[4:6]+" à "+formatagedarr[9:11]+"h"+formatagedarr[11:13]
            #untrajet = ResultatRecherche(depart, arriver, formatageddep, formatagedarr, distance, prix)
            trajet["departure_date_time"] = formatageddep
            trajet["arrival_date_time"] = formatagedarr
            trajet["prix"] = float(int(prix*100))/100
            trajet["distance"] = round(float(distance),2)
            trajet["depart"] = depart.replace("+", " ")
            trajet["arriver"] = arriver.replace("+", " ")
            listeTrajet = {str(i): trajet}
            date = str(trajetobj.get("arrival_date_time"))

    """
        dico = dict()
        for i in range(1,11):
            urltrajet = 'https://api.sncf.com/v1/coverage/sncf/journeys?from=stop_area%3AOCE%3ASA%3A'+str(departoid)+'&to=stop_area%3AOCE%3ASA%3A'+str(arriveroid)+'&datetime='+str(date)+'&datetime_represents=departure&data_freshness=realtime&key='+str(token_auth)
            trajetjson = requests.get(urltrajet)
            trajetobj = trajetjson.json()
            trajetobj = trajetobj.get("journeys")
            trajetobj = trajetobj[0]
            formatageddep = str(trajetobj.get("departure_date_time"))
            formatageddep = formatageddep[6:8]+"/"+formatageddep[4:6]+" à "+formatageddep[9:11]+"h"+formatageddep[11:13]
            dico["departure_date_time"+str(i)] = formatageddep
            formatagedarr = str(trajetobj.get("arrival_date_time")) 
            formatagedarr = formatagedarr[6:8]+"/"+formatagedarr[4:6]+" à "+formatagedarr[9:11]+"h"+formatagedarr[12:14]
            dico["arrival_date_time"+str(i)] = formatagedarr
            date = str(trajetobj.get("arrival_date_time"))
        

    #défnition d'un dictionnaire pour initialiser les variables dans mon template hmtl

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


def suppression(request):
    #récupération des données du formulaire
    depart = request.GET['depart']
    arriver = request.GET['arriver']
    dateDepart = request.GET['departure_date_time']
    dateArriver = request.GET['departure_date_time']
    distance = request.GET['distance']
    prix = request.GET['prix']
  
    #filtre sur un objet trajet puis suppression
    Trajet.object.filter(depart=depart, arriver = arriver, datedepart=dateDepart, dateArriver=dateArriver, distance= distance, prix = prix, session=request.session.session_key).delete()

def enregistrement(request):
    #récupération des données du formulaire
    depart = request.GET['depart']
    arriver = request.GET['arriver']
    dateDepart = request.GET['departure_date_time']
    dateArriver = request.GET['departure_date_time']
    distance = request.GET['distance']
    prix = request.GET['prix']
  
    #création d'un objet trajet et enregistrement dans la BDD
    Trajet.object(depart=depart, arriver = arriver, datedepart=dateDepart, dateArriver=dateArriver, distance= distance, prix = prix, session=request.session.session_key)
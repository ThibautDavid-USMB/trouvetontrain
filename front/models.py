from django.db import models
from django.conf import settings

# Create your models here.

class Trajet(models.Model):
    depart = models.CharField(max_length=200)
    arriver = models.CharField(max_length=200)
    dateDepart = models.CharField(max_length=200)
    dateArriver = models.CharField(max_length=200)
    distance = models.CharField(max_length=200)
    prix =models.CharField(max_length=200)
    session = models.TextField()
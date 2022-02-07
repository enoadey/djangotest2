from django.db import models
import pandas as pd
from sqlalchemy import create_engine
from django.contrib.auth.models import User
import os
import csv
import psycopg2



from django.db.models import Sum, Max, Min, Avg, StdDev
from django.db.models.aggregates import StdDev
from django.views.generic import ListView

# Create your models here.
#from django.contrib.auth.models import User

class CustomBooleanField(models.BooleanField):
    def from_db_value(self, value, expression, connection, context):
        if value is None:
            return value
        return int(value) # return 0/1

# Create your models here.


class immo_bien1(models.Model):
    id = models.IntegerField(primary_key = True)
    id_lot = models.TextField()
    nb_piece = models.IntegerField()
    typologie = models.CharField(max_length=200)
    prix_tva_reduite = models.DecimalField(max_digits=50, decimal_places=2)
    prix_tva_normale = models.FloatField()
    prix_HT = models.FloatField()
    prix_m2_HT = models.FloatField()
    prix_m2_TTC = models.FloatField()
    surface = models.FloatField(blank=True, null=True)
    etage = models.IntegerField(blank=True, null=True)
    orientation = models.CharField(max_length=200)
    exterieur = models.CharField(max_length=200)
    balcony = CustomBooleanField(default=1)
    garden = models.BooleanField()
    parking = models.BooleanField()
    nom_programme = models.TextField(blank=True)
    ville = models.CharField(max_length=200)
    departement = models.CharField(max_length=200)
    date_fin_programme = models.TextField()
    adresse_entiere = models.TextField()
    promoteur = models.TextField(blank=True)
    date_extraction = models.CharField(max_length=200)
    
    def __str__(self):
        return self.id
class Meta:
        db_table="immo_bien1"

   
#def example(request):
    #_count=immo_bien.o
    # bjects.count()
    ##return data

# def example1(request):
#     #_count=immo_bien.o
#     # bjects.count()
#     data=immo_bien.objects.filter('ville').aggregate(sum=Sum('prix_m2_TTC'), max=Max('prix_m2_TTC'), min=Min('prix_m2_TTC'), avg=Avg('prix_m2_TTC'))
#     return data
# queryset = Customer.objects.aggregate(total_no_goods=Count('id'))

from django.db import models

# Create your models here.
from django.db import models
import pandas as pd
from django.urls import reverse, resolve

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


class immo_bienny(models.Model):

    id_lot = models.CharField(("id_lot"), max_length=255)
    typologie = models.CharField(("typologie"), max_length=150, default='', blank=True, null=False)
    nb_piece = models.IntegerField(("nb_piece"))
    prix_tva_reduite = models.FloatField(("prix_tva_reduite"))
    prix_tva_normale = models.FloatField(("prix_tva_normale"))
    prix_HT = models.FloatField(("prix_HT"))
    prix_m2_HT = models.FloatField(("prix_m2_HT"))
    prix_m2_TTC = models.FloatField(("prix_m2_TTC"))
    surface = models.FloatField(("surface"))
    etage = models.IntegerField(("etage"))
    orientation = models.CharField(("orientation"),max_length=30, default='', blank=True, null=False)
    exterieur = models.BooleanField(("exterieur"))
    balcony = CustomBooleanField(("balcony"),default=1)
    garden = models.BooleanField(("garden"))
    parking = models.BooleanField(("parking"))
    nom_programme = models.CharField(("nom_programme"),max_length=100, default='', blank=True, null=False)
    ville = models.CharField(("ville"),max_length=150, default='', blank=True, null=False)
    departement = models.IntegerField(("departement"))
    date_fin_programme = models.TextField("date_fin_programme ")
    adresse_entiere = models.TextField(("adresse_entiere"),max_length=150)
    promoteur = models.CharField(("promoteur"),max_length=150, default='', blank=True, null=False)
    date_extraction = models.TextField("date_extraction")
    #likes = models.ManyToManyField(User, related_name='like', default=None, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['id_lot', 
            'nb_piece', 'typologie', 'prix_tva_reduite',
             'prix_tva_normale', 'prix_HT', 'prix_m2_HT', 'prix_m2_TTC',
               'surface', 'etage', 'orientation', 'exterieur', 'balcony', 'garden',
               'parking', 'nom_programme', 'ville', 'departement', 'date_fin_programme',
               'adresse_entiere', 'promoteur', 'date_extraction' ], name='unique_immo_name')
        ]
        db_table = 'immo_bienny'

    # def get_absolute_url(self):
    #     return reverse('immo-detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.id_lot}, {self.typologie}'
        ###db_table="immo_bienny"

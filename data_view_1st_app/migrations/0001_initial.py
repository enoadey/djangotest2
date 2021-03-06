# Generated by Django 4.0 on 2021-12-19 11:39

import data_view.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='immo_bien1',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('id_lot', models.TextField()),
                ('nb_piece', models.IntegerField()),
                ('typologie', models.CharField(max_length=200)),
                ('prix_tva_reduite', models.DecimalField(decimal_places=2, max_digits=50)),
                ('prix_tva_normale', models.FloatField()),
                ('prix_HT', models.FloatField()),
                ('prix_m2_HT', models.FloatField()),
                ('prix_m2_TTC', models.FloatField()),
                ('surface', models.FloatField(blank=True, null=True)),
                ('etage', models.IntegerField(blank=True, null=True)),
                ('orientation', models.CharField(max_length=200)),
                ('exterieur', models.CharField(max_length=200)),
                ('balcony', data_view.models.CustomBooleanField(default=1)),
                ('garden', models.BooleanField()),
                ('parking', models.BooleanField()),
                ('nom_programme', models.TextField(blank=True)),
                ('ville', models.CharField(max_length=200)),
                ('departement', models.CharField(max_length=200)),
                ('date_fin_programme', models.TextField()),
                ('adresse_entiere', models.TextField()),
                ('promoteur', models.TextField(blank=True)),
                ('date_extraction', models.CharField(max_length=200)),
            ],
        ),
    ]

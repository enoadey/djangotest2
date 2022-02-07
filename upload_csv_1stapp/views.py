from django.shortcuts import render
from data_view.models import immo_bien1
from django.db.models import Sum

# Create your views here.
from .models import Csv
from django.shortcuts import render

# Create your views here.
from .forms import CsvModelForm
import csv
from .models import Csv
from django.contrib.auth.models import User
#from . import views

from .forms import CsvModelForm
import csv
from .models import Csv
from django.contrib.auth.models import User
from django.db.models import Sum, Max, Min, Avg, StdDev
from django.db.models.aggregates import StdDev
from django.views.generic import ListView
#from django.http import HttpResponse
#create your views here.

def upload_file_view(request):
    form =CsvModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form = CsvModelForm()
        obj = Csv.objects.get(activated=False)
        with open(obj.file_name.path, 'r') as f:
            reader = csv.reader(f)
          

            for i, row in enumerate(reader):
                if i==1:
                    pass
                else:
                    row = "".join(row)
                    row = row.replace(" ", "_")
                    row = row.replace(";", " ")
                    row = row.split()
                    #print(row)
                    #print(type(row))

                    immo_bien1.objects.create(
                    #id =row[0],
                    id_lot=row[1], 
                    nb_piece=row[2], 
                    typologie=row[3], 
                    prix_tva_reduite=row[4],
                    prix_tva_normale=row[5], 
                    prix_HT =row[6], 
                    prix_m2_HT =row[7], 
                    prix_m2_TTC=row[8], 
                    surface=row[9], 
                    etage=row[10], 
                    orientation=row[11],
                    exterieur=row[12], 
                    balcony=row[13],
                    garden=row[14], 
                    parking=row[15], 
                    nom_programme= row[16], 
                    ville=row[17], 
                    departement=row[18], 
                    date_fin_programme=row[19], 
                    adresse_entiere=row[20],
                    promoteur=row[21], 
                    date_extraction=row[22])
                #row=row+1

                    #def example(request):
    #_count=immo_bien.o
    # bjects.count()
    #data=immo_bien.objects.all().aggregate(sum=Sum('prix_m2_TTC'), max=Max('prix_m2_TTC'), min=Min('prix_m2_TTC'), avg=Avg('prix_m2_TTC'),   )

    #return render(request, 'basic_html', {"data":data})
                    
            obj.activated = True
            obj.save()
    return render(request, "upload_csv/upload.html", {'form': form})

# class Example(ListView):
    
#     model = immo_bien
#     template_name = "basic.html"
    
#     def get_context_data(self, *args, **kwargs):
#         context = super(Example, self).get_context_data(*args, **kwargs)
#         context['Avg_prix_m2_TTC/ville'] = immo_bien.objects.values('ville').annotate(avg=Avg('prix_m2_TTC').order_by())
#         return context  

#     def example(request):
#     #_count=immo_bien.o
#     # bjects.count()
#         data=immo_bien.objects.all().aggregate(sum=Sum('prix_m2_TTC'), max=Max('prix_m2_TTC'), min=Min('prix_m2_TTC'), avg=Avg('prix_m2_TTC'))
#         return data
    #return HttpResponse('drop a file here')
    #form =CsvModelForm(request.POST or None, request.FILES or None)s
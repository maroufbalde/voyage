from django.shortcuts import render, redirect
from .models import Avion
from .forms import FormAvion, AvionApi
from rest_framework import viewsets


# Create your views here.
def voyage(request) : 
    avion = Avion.objects.all()
    dic = {'Appareil': avion}
    return render(request, 'acceuil.html', dic)

#Formulaire
def AvionView(request):
    if request.method == 'POST':
        form = FormAvion(request.POST)
        if form.is_valid():
        # Traiter les donnees du formulaire
           # avionid = form.cleaned_data['avionid']
          #  marque= form.cleaned_data['marque']
           # model = form.cleaned_data['model']
          #  datefabric = form.cleaned_data['datefabric']
         #   datemisens = form.cleaned_data['datemisens']
         form.save()

        # Vous pouvez ajouter une logique pour traiter les donees ici
        # Par example, envoyer un mail, sauvegarder dans la base de donnees
        return redirect('success') 
    else:
       form = FormAvion()
    
    return render(request, 'formulaire.html', {'form': form})

#API
class AvionApiView(viewsets.ModelViewSet):
   queryset = Avion.objects.all()
   serializer_class = AvionApi
   

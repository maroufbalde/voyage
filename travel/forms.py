from django import forms
from .models import Avion
from rest_framework import serializers
class FormAvion(forms.ModelForm):
    class Meta:
        model = Avion
        fields = ['avionid', 'marque', 'model', 'datefabric', 'datemisens']


#API
class AvionApi(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Avion
        fields = ['avionid', 'marque', 'model', 'datefabric', 'datemisens']


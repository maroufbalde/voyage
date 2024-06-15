from django.db import models

# Create your models here.
class Avion(models.Model) :
    avionid = models.CharField(null=True)
    marque= models.CharField(null=True)
    model = models.CharField(null=True)
    datefabric = models.DateField(null=True)
    datemisens = models.DateField(null=True)
    def __str__(self) :
        return self.model

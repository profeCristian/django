from django.db import models

# Create your models here.

class Persona(models.Model):
    rut    = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=30, blank=True, null=True)
    edad   = models.IntegerField(blank=True, null=True)
    activo = models.IntegerField(blank=True, null=True)  
   
    def __str__(self):
        return self.rut+", "+ self.nombre+", "+str(self.edad)+", "+str(self.activo)


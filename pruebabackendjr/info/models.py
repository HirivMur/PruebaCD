from django.db import models

# Create your models here.
class Estado(models.Model):
    d_estado = models.CharField(max_length=30)

class Municipio(models.Model):
    D_mnpio = models.CharField(max_length=30)
    estado=models.ForeignKey(Estado, on_delete=models.CASCADE)
   
class Colonia(models.Model):
    d_asenta = models.CharField(max_length=30)
    d_tipo_asenta = models.CharField(max_length=30)
    d_CP = models.CharField(max_length=5, blank=True, null=True)
    municipio=models.ForeignKey(Municipio, on_delete=models.CASCADE)

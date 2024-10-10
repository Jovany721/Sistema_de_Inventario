from django.db import models




class Productos(models.Model):
    producto = models.CharField(max_length=70)
    cantidad = models.IntegerField()
    precio = models.IntegerField()
    

   
    
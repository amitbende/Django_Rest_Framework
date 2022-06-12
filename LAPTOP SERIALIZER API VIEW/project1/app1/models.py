from django.db import models

# Create your models here.
class Laptop(models.Model):
    laptop_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    processer = models.CharField(max_length=50)
    price = models.FloatField()
    

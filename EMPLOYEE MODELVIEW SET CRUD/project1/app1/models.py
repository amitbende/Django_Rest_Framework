from unicodedata import name
from django.db import models

# Create your models here.
class Employee(models.Model):

    def picture(instance, filename):
        return '/'.join(['images', str(instance, name), filename])

    eid =models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    salary = models.FloatField()
    address = models.CharField(max_length=100)
    picture = models.ImageField(upload_to = 'picture', blank = True)

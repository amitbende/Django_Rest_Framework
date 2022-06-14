from django.db import models

# Create your models here.
class Employee(models.Model):
    eid = models.IntegerField()
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    sal = models.FloatField()
    email = models.EmailField()

    def __str__(self):
        return self.name

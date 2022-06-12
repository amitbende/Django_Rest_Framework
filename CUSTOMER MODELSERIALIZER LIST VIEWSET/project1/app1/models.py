from unicodedata import name
from django.db import models

class Customer(models.Model):
    def pictureFile(instance, filename):
        return '/'.join(['images', str(instance, name), filename])

    cid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    product = models.CharField(max_length=50)
    price = models.FloatField()
    shop = models.CharField(max_length=50)
    photo = models.ImageField(upload_to="pictureFILE", blank=True, max_length =254)


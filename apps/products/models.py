from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):        
    code        = models.IntegerField( blank=False )
    name        = models.CharField( max_length=50, blank=True )
    description = models.TextField( blank=False)
    image       = models.ImageField()

    class Meta:
        db_table = "products"

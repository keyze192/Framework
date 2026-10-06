from django.db import models

class Manufacturer(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE
    )
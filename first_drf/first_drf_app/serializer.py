from rest_framework.serializers import ModelSerializer
from . import models

class ManufacturerSerializer(ModelSerializer):
    class Meta:
        model = models.Manufacturer
        fields = ['name', 'country']

class ProductSerializer(ModelSerializer):
    class Meta:
        model = models.Product
        fields = ['name', 'price', 'manufacturer']
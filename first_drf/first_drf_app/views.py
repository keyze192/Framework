from rest_framework.viewsets import ModelViewSet
from .models import Manufacturer, Product
from django.utils.decorators import method_decorator
from rest_framework.decorators import action
from .serializer import ManufacturerSerializer, ProductSerializer
from rest_framework.response import Response

class ManufacturerViewsets(ModelViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer

    @action(methods=['GET'], detail=False, url_path='russian')
    def russian_manufacturers_list(self, request):
        queryset = self.queryset().filter(country='Россия')
        serializer = self.get_serializer(queryset, many=True)
        return Responce(serializer.data)

class ProductViewsets(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
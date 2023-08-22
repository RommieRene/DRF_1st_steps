from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serializers import ProductSerializer,CategorySerializer
from .models import Product,Category



class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
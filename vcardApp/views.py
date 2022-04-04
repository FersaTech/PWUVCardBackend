from rest_framework import generics
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import CategorySerializer, ProductSerializer, OrderSerializer
from .models import CategoryModel, ProductModel, OrderModel

# Create your views here.

class CategoryAPIView(generics.ListAPIView):
    queryset = CategoryModel.objects.all()
    serializer = CategorySerializer


class ProductAPIView(generics.ListAPIView):
    queryset = ProductModel
    serializer = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
from rest_framework import serializers
from .models import CategoryModel, ProductModel, OrderModel

# Create your serializers here.

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = CategoryModel
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductModel
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderModel
        fields = "__all__"
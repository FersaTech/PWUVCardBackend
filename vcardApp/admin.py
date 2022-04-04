from django.contrib import admin
from .models import CategoryModel, ProductModel, OrderModel

# Register your models here.
admin.site.site_header = "Print With Us Admin"
admin.site.register(CategoryModel)
admin.site.register(ProductModel)
admin.site.register(OrderModel)
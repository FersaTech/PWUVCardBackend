import uuid
from django.db import models

# Create your models here.

class CategoryModel(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    name = models.CharField(verbose_name='Name of Category: ', max_length=50)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Categories"


# Shape choice for the cards
SHAPE_CHOICES = [
    ("rectangle", "Rectangle"),
    ("rounded", "Rounded")
]

# Finish choice for the cards
FINSIH_CHOICES = [
    ("matt", "Matt"),
    ("gloss", "Gloss"),
    ("non lamination", "Non Lamination")
]

# Quality of Paper
QUALITY_CHOICES = [
    ("standard", "Standard"),
    ("premium", "Premium")
]

# Thickness of Paper
THICKNESS_CHOICES = [
    ("250 GSM", "250 GSM"),
    ("300 GSM", "300 GSM")
]


class ProductModel(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    name = models.CharField(max_length=50, verbose_name='Name of Product')
    category = models.ForeignKey(CategoryModel, blank=True, null=True, related_name="catagories", on_delete=models.PROTECT)
    shape = models.CharField(max_length=20, choices=SHAPE_CHOICES, default="rectangle")
    finish = models.CharField(max_length=20, choices=FINSIH_CHOICES, default="matt")
    quality = models.CharField(max_length=20, choices=QUALITY_CHOICES, default="premium")
    thickness = models.CharField(max_length=20, choices=THICKNESS_CHOICES, default="250 GSM")
    price = models.FloatField(default=0.0)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Products"


class OrderModel(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    product = models.ForeignKey(ProductModel, blank=False, null=False, related_name='product', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    price = models.FloatField(default=0.0)

    def __str__(self):
        return self.product.name
    
    def save(self, *args, **kwargs):
        val = self.product.price * self.quantity
        gst = val * 0.18
        self.price = val + gst
        super().save()
    
    class Meta:
        verbose_name_plural = "Orders"

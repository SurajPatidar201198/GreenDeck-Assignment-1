from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=500,null=True)
    brand_name = models.CharField(max_length=500,null=True)
    regular_price_value = models.CharField(max_length=500,null=True)
    offer_price_value = models.CharField(max_length=500,null=True)
    currency = models.CharField(max_length=500,null=True)
    classification_l1 = models.CharField(max_length=500,null=True)
    classification_l2 = models.CharField(max_length=500,null=True)
    classification_l3 = models.CharField(max_length=500,null=True)
    classification_l4 = models.CharField(max_length=500,null=True)
    image_url = models.CharField(max_length=500,null=True)
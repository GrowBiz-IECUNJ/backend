from django.db import models
from products.models import Product

class Vendor(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    product_name = models.ForeignKey(Product, on_delete=models.CASCADE, default=False)
    

    def __str__(self):
        return self.name
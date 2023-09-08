from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='GrowBiz/foto_produk/', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    stock = models.PositiveIntegerField()

    def __str__(self):
        return self.name

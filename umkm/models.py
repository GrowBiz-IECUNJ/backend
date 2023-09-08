from django.db import models
from products.models import Product
from vendor.models import Vendor

SEX_CHOICES = [
    ('Female', 'Female'),
    ('Male', 'Male'),
    ('Others', 'Others')
]

class UMKM(models.Model):
    owner_name = models.CharField(max_length=200)
    email = models.EmailField()
    birth_date = models.DateField()
    owner_contact = models.BigIntegerField()
    sex = models.CharField(max_length=10, choices=SEX_CHOICES, default='')
    owner_resume = models.FileField(upload_to='GrowBiz/UMKM/', max_length=254, blank=True)
    owner_country = models.CharField(max_length=100)
    owner_city = models.CharField(max_length=100)
    store_name = models.CharField(max_length=200)
    store_contact = models.BigIntegerField()
    store_handphone_number = models.BigIntegerField()
    nomor_induk_berusaha = models.BigIntegerField()
    kode_BLI = models.BigIntegerField()
    beginning_capital = models.BigIntegerField()
    store_channel = models.CharField(max_length=100)
    store_channel_photo = models.ImageField(upload_to='GrowBiz/UMKM/', default=False, blank=True)
    store_milestone = models.TextField()
    business_type = models.CharField(max_length=100)
    challenges = models.TextField()
    products = models.ForeignKey(Product, on_delete=models.CASCADE, default=False)
    vendors = models.ForeignKey(Vendor, on_delete=models.CASCADE, default=False)

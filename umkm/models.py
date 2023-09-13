from django.db import models
from products.models import Product
from vendor.models import Vendor

SEX_CHOICES = [("Female", "Female"), ("Male", "Male"), ("Others", "Others")]


class UMKM(models.Model):
    # owner_resume = models.FileField(
    #     upload_to="GrowBiz/UMKM/", max_length=254, blank=True
    # )
    store_name = models.CharField(max_length=200)
    store_contact = models.CharField(max_length=200)
    nomor_induk_berusaha = models.CharField(max_length=200)
    kode_BLI = models.CharField(max_length=200)
    beginning_capital = models.CharField(max_length=200)
    store_channel = models.CharField(max_length=100)
    # store_channel_photo = models.ImageField(upload_to="GrowBiz/UMKM/", blank=True)
    store_milestone = models.TextField()
    business_type = models.CharField(max_length=100)
    challenges = models.TextField()
    # products = models.ForeignKey(Product, on_delete=models.CASCADE, default=False)
    # vendors = models.ForeignKey(Vendor, on_delete=models.CASCADE, default=False)

from django.db import models

class Workshop(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    registration = models.URLField(max_length=200)
    photo = models.ImageField(upload_to='product_photos/')
    places = models.CharField(max_length=100)
    link_meeting = models.URLField(max_length=200)
    contact_person = models.BigIntegerField()
    speaker_name = models.CharField(max_length=100)
    speaker_description = models.TextField()

    def __str__(self):
        return self.title
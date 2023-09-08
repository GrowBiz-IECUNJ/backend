from django.db import models

class Investor(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="GrowBiz/Investor/")
    description = models.TextField()

    def __str__(self):
        return self.name

class Portfolio(models.Model):
    title = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="GrowBiz/Portfolio/")
    description = models.TextField()

    def __str__(self):
        return self.title
    
class Incubation(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="GrowBiz/incubation/")
    business_category = models.CharField(max_length=100)
    description = models.TextField()
    criteria = models.TextField()
    investor = models.ManyToManyField(Investor, blank=True)
    portfolio = models.ManyToManyField(Portfolio, blank=True)

    def __str__(self):
        return self.name







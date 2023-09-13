from django.db import models


class Wallet(models.Model):
    amount_of_money = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=20)
    date = models.DateField()
    description = models.TextField()

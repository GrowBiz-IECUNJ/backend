from django.db import models

TYPE_CHOICES = [
    ('Pemasukan', 'Pemasukan'),
    ('Pengeluaran', 'Pengeluaran')
]
    
class Wallet(models.Model):
    income = models.BigIntegerField()
    outcome = models.BigIntegerField()
    balance = models.BigIntegerField()
    date = models.DateField()
    type = models.CharField(max_length=15, choices=TYPE_CHOICES, default='')
    description = models.TextField()
    amount_of_money = models.DecimalField(max_digits=10, decimal_places=2)

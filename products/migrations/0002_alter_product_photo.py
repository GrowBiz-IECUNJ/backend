# Generated by Django 4.2.4 on 2023-09-03 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=models.ImageField(blank=True, upload_to='GrowBiz/foto_produk/'),
        ),
    ]

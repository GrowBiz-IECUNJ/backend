# Generated by Django 4.2.4 on 2023-09-03 06:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('umkm', '0005_alter_umkm_owner_resume_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='umkm',
            name='owner_resume',
        ),
        migrations.RemoveField(
            model_name='umkm',
            name='store_channel_photo',
        ),
    ]

from rest_framework import serializers
from .models import UMKM

class UMKMSerializer(serializers.ModelSerializer):
    class Meta:
        model = UMKM
        fields = '__all__'
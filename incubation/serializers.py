from rest_framework import serializers
from .models import Incubation, Portfolio, Investor

class IncubationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incubation
        fields = '__all__'

class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = '__all__'

class InvestorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Investor
        fields = '__all__'
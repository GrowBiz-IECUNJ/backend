from rest_framework import generics
from .models import Incubation, Portfolio, Investor
from .serializers import IncubationSerializer, PortfolioSerializer, InvestorSerializer


class IncubationListAPIView(generics.ListAPIView):
    queryset = Incubation.objects.all()
    serializer_class = IncubationSerializer


class IncubationDetailAPIView(generics.ListAPIView):
    serializer_class = IncubationSerializer

    def get_queryset(self):
        incubation_id = self.kwargs["id"]

        return Incubation.objects.filter(id=incubation_id)


class PortfolioAPIView(generics.ListAPIView):
    serializer_class = PortfolioSerializer

    def get_queryset(self):
        portfolio_id = self.kwargs["portfolio_id"]

        return Portfolio.objects.filter(id=portfolio_id)


class InvestorAPIView(generics.ListAPIView):
    serializer_class = InvestorSerializer

    def get_queryset(self):
        investor_id = self.kwargs["id"]

        return Investor.objects.filter(id=investor_id)

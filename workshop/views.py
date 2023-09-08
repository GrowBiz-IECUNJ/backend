from rest_framework import generics, status
from rest_framework.response import Response
from .models import Workshop
from .serializers import WorkshopSerializer

class WorkshopListAPIView(generics.ListAPIView):
    queryset = Workshop.objects.all()
    serializer_class = WorkshopSerializer
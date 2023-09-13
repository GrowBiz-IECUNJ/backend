from django.urls import path
from .views import WorkshopListAPIView

urlpatterns = [
    path("workshop/", WorkshopListAPIView.as_view(), name="umkm-workshop"),  # done
]

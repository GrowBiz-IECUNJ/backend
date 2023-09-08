from django.urls import path
from .views import VendorListAPIView, VendorDetail

urlpatterns = [
    path('vendor/', VendorListAPIView.as_view(), name='umkm-vendor'),
    path('vendor/<int:pk>/update/', VendorDetail.as_view(), name='umkm-vendor-update'),
]
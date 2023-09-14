from django.urls import path
from .views import VendorListAPIView, VendorDetail

urlpatterns = [
    path("vendor/", VendorListAPIView.as_view(), name="umkm-vendor"),  # done
    path("vendor/<int:pk>/update/", VendorDetail.as_view(), name="umkm-vendor-update"),
    path(
        "vendor/<int:pk>/delete/",
        VendorListAPIView.as_view(),
        name="umkm-vendor-delete",
    ),  # done
]

from django.urls import path
from .views import ProductListAPIView, ProductDetail, ProductsDetail

urlpatterns = [
    path("product/", ProductListAPIView.as_view(), name="umkm-product"),
    path(
        "product/<int:pk>/update/", ProductDetail.as_view(), name="umkm-product-update"
    ),
    path("product/<int:id>/", ProductsDetail.as_view(), name="umkm-product"),
]

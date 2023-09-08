from django.urls import path
from .views import WalletListAPIView, WalletDetail

urlpatterns = [
    path('wallet/', WalletListAPIView.as_view(), name='umkm-wallet'),
    path('vendor/<int:pk>/update/', WalletDetail.as_view(), name='umkm-vendor-update'),
]
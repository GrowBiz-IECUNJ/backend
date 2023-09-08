from django.urls import path
from .views import UMKMListAPIView, UMKMDetail

urlpatterns = [
    path('profile/', UMKMListAPIView.as_view(), name='umkm-profile'),
    path('profile/<int:pk>/update/', UMKMDetail.as_view(), name='umkm-profile-update'),
]
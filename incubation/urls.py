from django.urls import path
from .views import IncubationListAPIView, PortfolioAPIView, InvestorAPIView

urlpatterns = [
    path('incubation/', IncubationListAPIView.as_view(), name='incubation-list'),
    path('incubation/investor/<int:id>/', InvestorAPIView.as_view(), name='incubation-list'),
    path('incubation/portfolio/<int:portfolio_id>/', PortfolioAPIView.as_view(), name='incubation-list'),
]
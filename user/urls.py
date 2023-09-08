from django.urls import path
from .views import RegistrationView, LoginView, LogoutView, ChangePasswordView, UserDetail, GetUser
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('register', RegistrationView.as_view(), name='register'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('change-password', ChangePasswordView.as_view(), name='change-password'),
    path('token-refresh', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('detail', UserDetail.as_view(), name='detail'),
    path('getuser', GetUser.as_view(), name='detail'),
]
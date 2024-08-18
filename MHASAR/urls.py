from . import views
from .views import UserProfileView 
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

app_name = 'MHASAR'

urlpatterns = [
    path('register/',views.RegisterView.as_view(),name="register"),
    path('login/',views.LoginAPIView.as_view(),name="login"),
    path('logout/', views.LogoutAPIView.as_view(), name="logout"),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('profile/', UserProfileView.as_view(), name='user-profile'),
]
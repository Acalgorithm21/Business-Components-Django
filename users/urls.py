from django.urls import path
from .views import UserCreateView, UserUpdateView, UserLoginView, getCurrentUser, LogoutView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


urlpatterns = [
    path('users/', UserCreateView.as_view(), name='user_create'),
    path('users/login/', UserLoginView.as_view(), name='user_login'),
    path('users/logout/', LogoutView.as_view(), name='user_logout'),
    path('users/me/', getCurrentUser, name='me'),
]
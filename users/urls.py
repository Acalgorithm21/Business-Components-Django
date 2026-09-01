from django.urls import path
from .views import UserCreateView, UserUpdateView, UserLoginView, getCurrentUser, LogoutView, UserListView, \
    DeleteUserView
from rest_framework_simplejwt.views import (
    TokenRefreshView, TokenObtainPairView,
)

urlpatterns = [
    path('users/', UserCreateView.as_view(), name='user_create'),
    path('users/login/', UserLoginView.as_view(), name='user_login'),
    path('users/logout/', LogoutView.as_view(), name='user_logout'),
    path('users/me/', getCurrentUser, name='me'),
    path('users/all/', UserListView.as_view(), name='list_users'),
    path('users/<int:pk>/', DeleteUserView.as_view(), name='delete_user'),
    path('users/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
]
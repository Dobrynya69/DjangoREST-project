from django.urls import path, include, re_path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import *

urlpatterns = [
    path('jwt/token/', TokenObtainPairView.as_view()),
    path('jwt/token/refresh/', TokenRefreshView.as_view()),
    path('auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    path('images/plus/all/', ImageViewSet.as_view({'get': 'images'})),
    path('images/<pk>/', ImageViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})),
    path('images/', ImageViewSet.as_view({'get': 'list', 'post': 'create'})),
]

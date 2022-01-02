from collections import OrderedDict

from django.urls import path, include
from rest_framework.routers import APIRootView

from djoser.views import TokenCreateView, TokenDestroyView
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView, TokenVerifyView)

urlpatterns = [
    path('', include('rest_framework.urls')),

    path('token/login/', TokenCreateView.as_view(), name="token-login"),
    path('token/logout/', TokenDestroyView.as_view(), name="token-logout"),
    path('jwt/create/', TokenObtainPairView.as_view(), name='jwt-create'),
    path('jwt/refresh/', TokenRefreshView.as_view(), name='jwt-refresh'),
    path('jwt/verify/', TokenVerifyView.as_view(), name='jwt-verify'),

    path('', APIRootView.as_view(
        api_root_dict=OrderedDict({
            'token/login/': 'token-login',
            'token/logout/': 'token-logout',
            'jwt/create/': 'jwt-create',
            'jwt/refresh/': 'jwt-refresh',
            'jwt/verify/': 'jwt-verify',
        })
    ), name='auth-root'),
]

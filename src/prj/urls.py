import os

from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('prj.auth_urls')),
]

from rest_framework import routers
from djoser import views as djoser_views

if settings.DEBUG or os.environ.get('DJANGO_BROWSE_API', ''):
    router = routers.DefaultRouter(trailing_slash=False)
else:
    router = routers.SimpleRouter(trailing_slash=False)

router.register("users", djoser_views.UserViewSet)

urlpatterns += [
    path('api/', include(router.urls)),
]

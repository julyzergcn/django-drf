from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('prj.auth_urls')),
]

from rest_framework.routers import DefaultRouter
from djoser import views as djoser_views

router = DefaultRouter()
router.register("users", djoser_views.UserViewSet)

urlpatterns += [
    path('api/', include(router.urls)),
]

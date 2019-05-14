from rest_framework.authtoken import views
from django.urls import path, include
from rest_framework import routers
from . views import *
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('rest-auth/', include('rest_auth.urls')),
]

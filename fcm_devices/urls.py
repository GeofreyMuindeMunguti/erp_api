# your_app/urls.py
from django.urls import path, include

from rest_framework import routers
from fcm.views import DeviceViewSet


router = routers.DefaultRouter()
router.register(r'devices', DeviceViewSet)

urlpatterns = [
    path('', include(router.urls))

]
from django.urls import path, include
from rest_framework import routers

from . import urls
from . import views

router = routers.DefaultRouter()
router.register(r'ftthproject', views.FTTHProjectViewSet)


urlpatterns = (
    # urls for DRF API
    path('', include(router.urls)),
)


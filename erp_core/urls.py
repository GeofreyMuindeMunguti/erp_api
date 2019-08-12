from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'mainsite', views.MainSiteViewSet)


urlpatterns = (
    # urls for Django Rest Framework API
    path('', include(router.urls)),
)

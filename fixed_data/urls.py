from django.urls import path, include
from rest_framework import routers

from . import views
from . import views

router = routers.DefaultRouter()
router.register(r'client', views.ClientViewSet)
router.register(r'technology', views.TechnologyViewSet)
router.register(r'service', views.ServiceViewSet)
router.register(r'building', views.BuildingViewSet)
router.register(r'link', views.LinkViewSet)


urlpatterns = (
    # urls for Django Rest Framework API
    path('', include(router.urls)),
)

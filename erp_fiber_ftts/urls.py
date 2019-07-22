from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from django.urls import path, include
from .views import *



router = DefaultRouter()

router.register(r'FttsSiteViewSet', views.FttsSiteViewSet)
router.register(r'FttsCommercialTeamViewSet', views.FttsCommercialTeamViewSet)

""" ENDPOINTS FOR FRONTEND"""


urlpatterns = [
    path('', include(router.urls)),

]

from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from erp_construction.models import *
from users.models import *
from django.urls import path, include
from .views import *



router = DefaultRouter()

router.register(r'FttsCommercialTeamViewSet', views.FttsCommercialTeamViewSet)
router.register(r'FttsProcurementTeamViewSet', views.FttsProcurementTeamViewSet)
router.register(r'SitePoleInstallationViewSet', views.SitePoleInstallationViewSet)
router.register(r'SiteTrenchingViewSet', views.SiteTrenchingViewSet)
router.register(r'SiteBackfillingViewSet', views.SiteBackfillingViewSet)
router.register(r'SiteCableInstallationViewSet', views.SiteCableInstallationViewSet)
router.register(r'FttsCivilTeamViewSet', views.FttsCivilTeamViewSet)

""" ENDPOINTS FOR FRONTEND"""


urlpatterns = [
    path('', include(router.urls)),

]

from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from erp_construction.models import *
from users.models import *
from django.urls import path, include
from .views import *



router = DefaultRouter()

router.register(r'fttsproject', views.FTTSProjectViewSet)
router.register(r'FttsCommercialTeam', views.FttsCommercialTeamViewSet)
router.register(r'FttsProcurementTeam', views.FttsProcurementTeamViewSet)

router.register(r'SitePoleInstallation', views.SitePoleInstallationViewSet)
router.register(r'SiteTrenching', views.SiteTrenchingViewSet)
router.register(r'SiteBackfilling', views.SiteBackfillingViewSet)
router.register(r'SiteCableInstallation', views.SiteCableInstallationViewSet)
router.register(r'sitemanholeinstallation', views.SiteManHoleInstallationViewSet)
router.register(r'FttsCivilTeam', views.FttsCivilTeamViewSet)

router.register(r'SiteTerminalInHse', views.SiteTerminalInHseViewSet)
router.register(r'SiteInterception', views.SiteInterceptionViewSet)
router.register(r'SiteIntegration', views.SiteIntegrationViewSet)
router.register(r'SiteAsBuilt', views.SiteAsBuiltViewSet)
router.register(r'FttsInstallationTeam', views.FttsInstallationTeamViewSet)
router.register(r'dailycivilworkproduction', views.DailyCivilWorkProductionViewSet)
router.register(r'fttscasualdailyregister', views.FTTSCasualDailyRegisterViewSet)


""" ENDPOINTS FOR FRONTEND"""


urlpatterns = [
    path('', include(router.urls)),

]
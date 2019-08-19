from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from erp_construction.models import *
from users.models import *
from django.urls import path, include
from .views import *



router = DefaultRouter()
router.register(r'ftthproject', views.FTTHProjectViewSet)

router.register(r'ftthinterceptionpoints', views.FtthInterceptionPointViewSet)
router.register(r'ftthsurveyphotos', views.ftthSurveyPhotosViewSet)
router.register(r'ftthsurveys', views.ftthSurveyViewSet)

router.register(r'FtthPoleInstallation', views.FtthPoleInstallationViewSet)
router.register(r'FtthTrenching', views.FtthTrenchingViewSet)
router.register(r'FtthBackfilling', views.FtthBackfillingViewSet)
router.register(r'FtthCableInstallation', views.FtthCableInstallationViewSet)
router.register(r'FtthCivilTeam', views.FtthCivilTeamViewSet)

router.register(r'FtthSplicingEnclosure', views.FtthSplicingEnclosureViewSet)
router.register(r'FtthSplicingFAT', views.FtthSplicingFATViewSet)
router.register(r'FtthSplicingFDT', views.FtthSplicingFDTViewSet)
router.register(r'FtthSplicing', views.FtthSplicingViewSet)
router.register(r'FtthPowerLevels', views.FtthPowerLevelsViewSet)
router.register(r'FtthOTDRTraces', views.FtthOTDRTracesViewSet)
router.register(r'FtthSignalTesting', views.FtthSignalTestingViewSet)
router.register(r'FtthInstallationTeam', views.FtthInstallationTeamViewSet)

""" ENDPOINTS FOR FRONTEND"""


urlpatterns = [
    path('', include(router.urls)),

]

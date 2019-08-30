from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from erp_ftth.models import *
from users.models import *
from django.urls import path, include
from .views import *
from .ftthfiles import filesviews


router = DefaultRouter()
router.register(r'ftthproject', views.FTTHProjectViewSet)

router.register(r'ftthinterceptionpoints', views.FtthInterceptionPointViewSet)
router.register(r'ftthsurveyphotos', views.ftthSurveyPhotosViewSet)
router.register(r'ftthsurveys', views.ftthSurveyViewSet)

router.register(r'FtthCommercialTeam', views.FtthCommercialTeamViewSet)
router.register(r'FtthProcurementTeam', views.FtthProcurementTeamViewSet)

router.register(r'FtthPoleInstallationImage', views.FtthPoleInstallationImageViewSet)
router.register(r'DailyFtthPoleInstallation', views.DailyFtthPoleInstallationViewSet)
router.register(r'FtthPoleInstallation', views.FtthPoleInstallationViewSet)

router.register(r'FtthTrenchingImage', views.FtthTrenchingImageViewSet)
router.register(r'DailyFtthTrenching', views.DailyFtthTrenchingViewSet)
router.register(r'FtthTrenching', views.FtthTrenchingViewSet)

router.register(r'FtthBackfillingImage', views.FtthBackfillingImageViewSet)
router.register(r'DailyFtthBackfilling', views.DailyFtthBackfillingViewSet)
router.register(r'FtthBackfilling', views.FtthBackfillingViewSet)

router.register(r'FtthCableInstallationImage', views.FtthCableInstallationImageViewSet)
router.register(r'DailyFtthCableInstallation', views.DailyFtthCableInstallationViewSet)
router.register(r'FtthCableInstallation', views.FtthCableInstallationViewSet)

router.register(r'FtthCivilTeam', views.FtthCivilTeamViewSet)

router.register(r'FtthSplicingEnclosureImage', views.FtthSplicingEnclosureImageViewSet)
router.register(r'DailyFtthSplicingEnclosure', views.DailyFtthSplicingEnclosureViewSet)
router.register(r'FtthSplicingEnclosure', views.FtthSplicingEnclosureViewSet)

router.register(r'FtthSplicingFATImage', views.FtthSplicingFATImageViewSet)
router.register(r'DailyFtthSplicingFAT', views.DailyFtthSplicingFATViewSet)
router.register(r'FtthSplicingFAT', views.FtthSplicingFATViewSet)

router.register(r'FtthSplicingFDTImage', views.FtthSplicingFDTImageViewSet)
router.register(r'DailyFtthSplicingFDT', views.DailyFtthSplicingFDTViewSet)
router.register(r'FtthSplicingFDT', views.FtthSplicingFDTViewSet)

router.register(r'FtthSplicing', views.FtthSplicingViewSet)

router.register(r'FtthCoreProvisionImage', views.FtthCoreProvisionImageViewSet)
router.register(r'DailyFtthCoreProvision', views.DailyFtthCoreProvisionViewSet)
router.register(r'FtthCoreProvision', views.FtthCoreProvisionViewSet)

router.register(r'FtthPowerLevelsImage', views.FtthPowerLevelsImageViewSet)
router.register(r'DailyFtthPowerLevels', views.DailyFtthPowerLevelsViewSet)
router.register(r'FtthPowerLevels', views.FtthPowerLevelsViewSet)

router.register(r'FtthOTDRTracesImage', views.FtthOTDRTracesImageViewSet)
router.register(r'DailyFtthOTDRTraces', views.DailyFtthOTDRTracesViewSet)
router.register(r'FtthOTDRTraces', views.FtthOTDRTracesViewSet)

router.register(r'FtthSignalTesting', views.FtthSignalTestingViewSet)

router.register(r'FtthIssues', views.FtthIssuesViewSet)
router.register(r'FtthInstallationTeam', views.FtthInstallationTeamViewSet)
router.register(r'FtthTeam', views.FtthTeamViewSet)

""" ENDPOINTS FOR FRONTEND"""


urlpatterns = [
    path('', include(router.urls)),

      # FILES (PER SITE) ENDPOINTS

    path('files/<int:pk>/', filesviews.FTTHProjectGetView.as_view()),# Main

    # path('files/<int:pk>/commercialteamtiles/', filesviews.FttsCommercialTeamFilesView.as_view()),
    # Civil works
    path('files/<int:pk>/poleinstallation/', filesviews. FtthPoleInstallationilesView.as_view()),
    path('files/<int:pk>/trenching/', filesviews.FtthTrenchingSubTaskFilesView.as_view()),
    
    path('files/<int:pk>/backfilling/', filesviews.FtthBackfillingSubTaskFilesView.as_view()),
    # path('files/<int:pk>/sitemanholeinstall/', filesviews.ManHoleInstallationFilesView.as_view()),


]

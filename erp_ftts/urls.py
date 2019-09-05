from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from erp_ftts.models import *
from users.models import *
from django.urls import path, include
from .views import *
from .fttsfiles import filesviews
from erp_ftts.monitoring import *



router = DefaultRouter()
router.register(r'fttsproject', views.FTTSProjectViewSet)
router.register(r'fttssite', views.FttsSiteViewSet)

router.register(r'interceptionpoints', views.InterceptionPointViewSet)
router.register(r'fttsSurveyPhotos', views.fttsSurveyPhotosViewSet)
router.register(r'fttssurveys', views.fttsSurveyViewSet)

router.register(r'FttsCommercialTeam', views.FttsCommercialTeamViewSet)
router.register(r'FttsProcurementTeam', views.FttsProcurementTeamViewSet)
router.register(r'FttsCertificates', views.FttsCertificatesViewSet)

router.register(r'SiteTrenchingImage', views.SiteTrenchingImageViewSet)
router.register(r'DailySiteTrenching', views.DailySiteTrenchingViewSet)
router.register(r'SiteTrenching', views.SiteTrenchingViewSet)

router.register(r'SiteDuctInstallationImage', views.SiteDuctInstallationImageViewSet)
router.register(r'DailySiteDuctInstallation', views.DailySiteDuctInstallationViewSet)
router.register(r'SiteDuctInstallation', views.SiteDuctInstallationViewSet)

router.register(r'ManHoleInstallationImage', views.ManHoleInstallationImageViewSet)
router.register(r'DailyManHoleInstallation', views.DailyManHoleInstallationViewSet)
router.register(r'sitemanholeinstallation', views.SiteManHoleInstallationViewSet)

router.register(r'SiteCableInstallationImage', views.SiteCableInstallationImageViewSet)
router.register(r'DailySiteCableInstallation', views.DailySiteCableInstallationViewSet)
router.register(r'SiteCableInstallation', views.SiteCableInstallationViewSet)

router.register(r'FttsAccessApprovalCivil', views.FttsAccessApprovalCivilViewSet)
router.register(r'FttsHealthDocumentsCivilTeam', views.FttsHealthDocumentsCivilTeamViewSet)

router.register(r'FttsCivilTeam', views.FttsCivilTeamViewSet)

router.register(r'SiteTerminalInHseImage', views.SiteTerminalInHseImageViewSet)
router.register(r'DailySiteTerminalInHse', views.DailySiteTerminalInHseViewSet)
router.register(r'SiteTerminalInHse', views.SiteTerminalInHseViewSet)

router.register(r'SiteInterceptionImage', views.SiteInterceptionImageViewSet)
router.register(r'DailySiteInterception', views.DailySiteInterceptionViewSet)
router.register(r'SiteInterception', views.SiteInterceptionViewSet)

router.register(r'FttsAccessApprovalInstallation', views.FttsAccessApprovalInstallationViewSet)
router.register(r'FttsHealthDocsInstallationTeam', views.FttsHealthDocsInstallationTeamViewSet)

router.register(r'FttsIssues', views.FttsIssuesViewSet)
router.register(r'FttsInstallationTeam', views.FttsInstallationTeamViewSet)
router.register(r'FttsTeam', views.FttsTeamViewSet)

router.register(r'dailycivilworkproduction', views.DailyCivilWorkProductionViewSet)
router.register(r'casualdailyregister', views.CasualDailyRegisterViewSet)
router.register(r'fttscasualdailyregister', views.FTTSCasualDailyRegisterViewSet)


""" ENDPOINTS FOR FRONTEND"""


urlpatterns = [
    path('', include(router.urls)),
    # ENDPOINTS FOR DASHBOARD
    path('fttsproject/<int:pk>/fttssites', FttsSiteListView.as_view()),

    path('fttstaskstatus/', FttsTaskStatusView.as_view()),
    path('fttstimesheetsummary/', FttsTimesheetSummaryView.as_view()),
    path('fttsissuestatus/', FttsIssueStatusView.as_view()),

    # path('turnaroundtime/', TurnAroundTimeView.as_view()),
    # path('totalpurchaseprders/', TotalPurchaseOrdersView.as_view()),
    # path('revenueperproject/<int:pk>', RevenueDetailView.as_view()),
    # path('revenue/', RevenueListView.as_view()),

    # FILES (PER SITE) ENDPOINTS

    path('files/<int:pk>/', filesviews.FttsSiteFilesView.as_view()),# Main

    path('files/<int:pk>/commercialteamtiles/', filesviews.FttsCommercialTeamASubTaskFilesView.as_view()),
    # Civil works

    # path('files/<int:pk>/siteductinstalls/', filesviews.SiteDuctInstallationFilesView.as_view()),
    # path('files/<int:pk>/sitemanholeinstall/', filesviews.ManHoleInstallationFilesView.as_view()),
    path('files/<int:pk>/sitesurvey/', filesviews.FttsSurveyPhotosASubTaskFilesView.as_view()),
    path('files/<int:pk>/sitetrenchings/', filesviews.SiteTrenchingASubTaskFilesView.as_view()),
    path('files/<int:pk>/siteductinstall/', filesviews.SiteDuctASubTaskFilesView.as_view()),
    path('files/<int:pk>/manholeinstallation/', filesviews.ManHoleInstallationASubTaskFilesView.as_view()),
    path('files/<int:pk>/sitecableinstallation/', filesviews.SiteCableInstallationASubTaskFilesView.as_view()),
    path('files/<int:pk>/siteterminalinhses/', filesviews.SiteTerminalInHseASubTaskFilesView.as_view()),
    path('files/<int:pk>/siteinterception/', filesviews.SiteInterceptionASubTaskFilesView.as_view()),


]

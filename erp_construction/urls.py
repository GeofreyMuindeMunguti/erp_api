from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from django.urls import path, include

router = DefaultRouter()

router.register(r'projects', views.ProjectViewSet)
router.register(r'commercialteamtasks', views.CommercialTeamViewSet)
router.register(r'procurementteamtasks', views.ProcurementTeamViewSet)
router.register(r'healthdocscivil', views.HealthDocCivilViewSet)
router.register(r'accessapprovalscivil', views.AccessApprovalCivilViewSet)
router.register(r'foundationimages', views.FoundationImageViewSet)
router.register(r'slabsimages', views.SlabsImageViewSet)
router.register(r'sitewallingimages', views.SiteWallingImageViewSet)
router.register(r'civilteamtasks', views.CivilTeamViewSet)
router.register(r'installationteams', views.InstallationTeamViewSet)
router.register(r'healthdocumentsinstallationteams', views.HealthDocumentsInstallationTeamViewset)
router.register(r'accessapprovalinstallations', views.AccessApprovalInstallationViewSet)
router.register(r'rfandlinkimages', views.RFAndLinkImageViewSet)
router.register(r'electricalimages', views.ElectricalImageViewSet)
router.register(r'kplcsolarsmages', views.KPLCSolarImageViewSet)


urlpatterns = [
    path('', include(router.urls)),
]

from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from django.urls import path, include
from .views import CivilProgressView, CommercialTeamProgressView, ProcurementTeamView


router = DefaultRouter()

router.register(r'projects', views.ProjectViewSet)
router.register(r'Icons', views.ProjectIconViewSet)
router.register(r'commercialteamtasks', views.CommercialTeamViewSet)
router.register(r'procurementteamtasks', views.ProcurementTeamViewSet)
router.register(r'healthdocscivil', views.HealthDocCivilViewSet)
router.register(r'accessapprovalscivil', views.AccessApprovalCivilViewSet)
router.register(r'civilteamtasks', views.CivilTeamViewSet)
router.register(r'foundationimages', views.FoundationImageViewSet)
router.register(r'setclearingimages', views.SetSiteClearingImageViewSet)
router.register(r'sitewallingimages', views.SiteWallingImageViewSet)
router.register(r'towerbaseimages', views.TowerBaseImageViewSet)
router.register(r'bindingimages', views.BindingImageViewSet)
router.register(r'steelfixformworkimages', views.SteelFixFormworkImageViewSet)
router.register(r'concretepourcuringimages', views.ConcretePourCuringImageViewSet)
router.register(r'installationteams', views.InstallationTeamViewSet)
router.register(r'healthdocumentsinstallationteams', views.HealthDocumentsInstallationTeamViewset)
router.register(r'accessapprovalinstallations', views.AccessApprovalInstallationViewSet)
router.register(r'rfandlinkimages', views.RFAndLinkImageViewSet)
router.register(r'electricalimages', views.ElectricalImageViewSet)
router.register(r'kplcsolarsmages', views.KPLCSolarImageViewSet)
router.register(r'slabsimages', views.SlabsImageViewSet)


urlpatterns = [
    path('', include(router.urls)),
    # ENDPOINTS FOR DASHBOARD
    path('commercialprogress/<int:pk>', CommercialTeamProgressView.as_view()),
    path('procurementprogress/<int:pk>', ProcurementTeamView.as_view()),
    path('civilprogress/<int:pk>', CivilProgressView.as_view())
]

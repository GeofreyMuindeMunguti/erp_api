from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from django.urls import path, include
from .views import *
from .progress import *
from .monitoring import *
from .scorecard import *
from .flag import *


router = DefaultRouter()

router.register(r'projects', views.ProjectViewSet)
router.register(r'category', views.CategoryViewSet)
router.register(r'Icons', views.ProjectIconViewSet)
router.register(r'projectcosting', views.ProjectCostingViewSet)
router.register(r'projectpos', views.ProjectPOSViewSet)
router.register(r'commercialteamtasks', views.CommercialTeamViewSet)
router.register(r'procurementteamtasks', views.ProcurementTeamViewSet)
router.register(r'healthdocscivil', views.HealthDocCivilViewSet)
router.register(r'accessapprovalscivil', views.AccessApprovalCivilViewSet)
router.register(r'civilteamtasks', views.CivilTeamViewSet)

router.register(r'foundationimages', views.FoundationImageViewSet)
router.register(r'setclearingimages', views.SetSiteClearingImageViewSet)
router.register(r'towerbaseimages', views.TowerBaseImageViewSet)
router.register(r'bindingimages', views.BindingImageViewSet)
router.register(r'steelfixformworkimages', views.SteelFixFormworkImageViewSet)
router.register(r'concretepourimages', views.ConcretePourImageViewSet)
router.register(r'concretecuringperiod', views.ConcreteCuringPeriodImageViewSet)


router.register(r'excavation', views.ExcavationImageViewSet)
router.register(r'bs241concretepourcuringperiod', views.bs241ConcretePourCuringPeriodImageViewSet)
router.register(r'bs241generatorslabs', views.BS241AndGeneatorSlabsImageViewSet)


router.register(r'foundationfootpour', views.FoundFootPourImageViewSet)
router.register(r'blockworkpanelconstruct', views.BlockworkPanelConstImageViewSet)
router.register(r'gateinstallation', views.GateInstallationImageViewSet)
router.register(r'razorelectricfence', views.RazorElectricFenceImageViewSet)
router.register(r'boundarywall', views.BoundaryWallImageViewSet)

router.register(r'towererection', views.TowerErectionImageViewSet)
router.register(r'towerpaint', views.TowerPaintImageViewSet)
router.register(r'cableways', views.CableWaysImageViewSet)
router.register(r'antennacoaxinstallation', views.AntennaCoaxInstallImageViewSet)
router.register(r'towerantennacoax', views.TowerAntennaCoaxImageViewSet)

router.register(r'kpi', views.KpiViewSet)
router.register(r'tasks', views.TaskViewSet)
router.register(r'subtasks', views.SubTaskViewSet)

router.register(r'installationteams', views.InstallationTeamViewSet)
router.register(r'electricaltasks', views.ElectricalTasksViewSet)
router.register(r'generatortasks', views.GeneratorInstallationViewSet)
router.register(r'earthingtasks', views.EarthingViewSet)
router.register(r'reticulationtasks', views.ReticulationAPSViewSet)
router.register(r'undergroundtasks', views.UndergroundTasksViewSet)
router.register(r'telecomtasks', views.TelecomTasksViewSet)
router.register(r'mwinstallationtasks', views.MWInstallationTasksViewSet)
router.register(r'btsinstallationtasks', views.BTSInstallationTasksViewSet)
router.register(r'healthdocumentsinstallationteams', views.HealthDocumentsInstallationTeamViewset)
router.register(r'accessapprovalinstallations', views.AccessApprovalInstallationViewSet)
router.register(r'kplcsolarsmages', views.KPLCSolarImageViewSet)

""" ENDPOINTS FOR FRONTEND"""


urlpatterns = [
    path('', include(router.urls)),
    # ENDPOINTS FOR DASHBOARD
    path('commercialprogress/<int:pk>', CommercialTeamProgressView.as_view()),
    path('procurementprogress/<int:pk>', ProcurementProgressTeamView.as_view()),
    path('civilprogress/<int:pk>', CivilProgressView.as_view()),
    path('installationprogress/<int:pk>', InstallationProgressView.as_view()),
    path('foundationprogress/<int:pk>', FoundationTaskProgressView.as_view()),
    path('btsgenprogress/<int:pk>', BTSandGenTaskProgressView.as_view()),
    path('boundarywallprogress/<int:pk>', BoundaryTaskProgressView.as_view()),
    path('towerprogress/<int:pk>', TowerTaskProgressView.as_view()),
    path('electricalprogress/<int:pk>', ElectricalTaskProgressView.as_view()),
    path('telecomprogress/<int:pk>', TelecomTaskProgressView.as_view()),
    path('taskstatus/', TaskStatusView.as_view()),
    path('timesheetsummary/', TimesheetSummaryView.as_view()),
    path('issuestatus/', IssueStatusView.as_view()),
    path('turnaroundtime/', TurnAroundTimeView.as_view()),
    path('totalpurchaseprders/', TotalPurchaseOrdersView.as_view()),
    path('revenueperproject/<int:pk>', RevenueDetailView.as_view()),
    path('revenue/', RevenueListView.as_view()),
    # path('procurementsum/<int:pk>', ProcurementSumView.as_view())
]

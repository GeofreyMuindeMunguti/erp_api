from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from django.urls import path, include
from .views import *
from .progress import *
from .monitoring import *
from .scorecard import *
from .btsfiles import filesviews



router = DefaultRouter()

router.register(r'btsproject', views.BtsProjectViewSet)
router.register(r'btssite', views.BtsSiteViewSet)
router.register(r'category', views.CategoryViewSet)
router.register(r'Icons', views.ProjectIconViewSet)
router.register(r'projectcosting', views.ProjectCostingViewSet)
router.register(r'projectpos', views.ProjectPOSViewSet)
router.register(r'BtsBudget',views.BtsBudgetViewSet)

router.register(r'commercialteamtasks', views.CommercialTeamViewSet)
router.register(r'procurementteamtasks', views.ProcurementTeamViewSet)

router.register(r'healthdocscivil', views.HealthDocCivilViewSet)
router.register(r'accessapprovalscivil', views.AccessApprovalCivilViewSet)
router.register(r'civilteamtasks', views.CivilTeamViewSet)

router.register(r'category', views.CategoryViewSet)
router.register(r'Icons', views.ProjectIconViewSet)
router.register(r'projectcosting', views.ProjectCostingViewSet)
router.register(r'projectpos', views.ProjectPOSViewSet)
router.register(r'commercialteamtasks', views.CommercialTeamViewSet)
router.register(r'procurementteamtasks', views.ProcurementTeamViewSet)
router.register(r'healthdocscivil', views.HealthDocCivilViewSet)
router.register(r'accessapprovalscivil', views.AccessApprovalCivilViewSet)
router.register(r'civilteamtasks', views.CivilTeamViewSet)

router.register(r'foundationimages', views.FoundationTaskViewSet)
router.register(r'setclearingsubtasks', views.SiteClearingSubTaskViewSet)
router.register(r'setclearingdays', views.SiteClearingDateViewSet)
router.register(r'setclearingimages', views.SiteClearingImageViewSet)

router.register(r'towerbasesubtasks', views.TowerBaseSubTaskViewSet)
router.register(r'towerbasedays', views.TowerBaseDateViewSet)
router.register(r'towerbaseimages', views.TowerBaseImageViewSet)

router.register(r'blindingsubtasks', views.BlindingSubTaskViewSet)
router.register(r'blindingdates', views.BlindingDateViewSet)
router.register(r'blindingimages', views.BlindingImageViewSet)

router.register(r'steelfixformworkimages', views.SteelFixFormworkSubtaskViewSet)
router.register(r'steelfixformworkimages', views.SteelFixFormworkDateViewSet)
router.register(r'steelfixformworkimages', views.SteelFixFormworkImageViewSet)

router.register(r'concretepourimages', views.ConcretePourSubTaskViewSet)
router.register(r'concretepourimages', views.ConcretePourDateViewSet)
router.register(r'concretepourimages', views.ConcretePourImageViewSet)

router.register(r'concretecuringperiodsubtask', views.ConcreteCuringPeriodSubTaskViewSet)
router.register(r'concretecuringperioddate', views.ConcreteCuringPeriodDateViewSet)
router.register(r'concretecuringperiodimage', views.ConcreteCuringPeriodImageViewSet)

router.register(r'excavation', views.ExcavationSubTaskViewSet)
router.register(r'excavationdates', views.ExcavationDateViewSet)
router.register(r'excavationimages', views.ExcavationImageViewSet)

router.register(r'bs241concretepourcuringperiodsubtask', views.Bs241ConcretePourCuringPeriodSubTaskViewSet)
router.register(r'bs241concretepourcuringperioddates', views.BS241ConcretePourCuringPeriodDateViewSet)
router.register(r'bs241concretepourcuringperiodimages', views.Bs241ConcretePourCuringPeriodImageViewSet)

router.register(r'bs241generatorslabs', views.BS241AndGeneatorSlabTaskViewSet)

router.register(r'foundationfootpour', views.FoundFootPourSubtaskViewSet)
router.register(r'foundationfootpourdate', views.FoundFootPourDateViewSet)
router.register(r'foundationfootpourimage', views.FoundFootPourImageViewSet)

router.register(r'blockworkpanelconstruct', views.BlockworkPanelConstSubtaskViewSet)
router.register(r'blockworkpanelconstructdates', views.BlockworkPanelConstDateViewSet)
router.register(r'blockworkpanelconstructimages', views.BlockworkPanelConstImageViewSet)

router.register(r'gateinstallation', views.GateInstallationSubtaskViewSet)
router.register(r'gateinstallationdates', views.GateInstallationDateViewSet)
router.register(r'gateinstallationimages', views.GateInstallationImageViewSet)

router.register(r'razorelectricfence', views.RazorElectricFenceSubtaskViewSet)
router.register(r'razorelectricfencedates', views.RazorElectricFenceDateViewSet)
router.register(r'razorelectricfenceimages', views.RazorElectricFenceImageViewSet)

router.register(r'boundarywall', views.BoundaryWallTaskViewSet)
router.register(r'towerantennacoax', views.TowerAntennaCoaxTaskViewSet)

router.register(r'towererection', views.TowerErectionSubtaskViewSet)
router.register(r'towererectiondates', views.TowerErectionDateViewSet)
router.register(r'towererectionimages', views.TowerErectionImageViewSet)

router.register(r'towerpaint', views.TowerPaintSubtaskViewSet)
router.register(r'towerpaintdates', views.TowerPaintDateViewSet)
router.register(r'towerpaintimages', views.TowerPaintImageViewSet)

router.register(r'cableways', views.CableWaysSubtaskViewSet)
router.register(r'cablewaysdates', views.CableWaysDateViewSet)
router.register(r'cablewaysimages', views.CableWaysImageViewSet)

router.register(r'antennacoaxinstallation', views.AntennaCoaxInstallSubtaskViewSet)
router.register(r'antennacoaxinstallation', views.AntennaCoaxInstallDateViewSet)
router.register(r'antennacoaxinstallation', views.AntennaCoaxInstallImageViewSet)

router.register(r'kpi', views.KpiViewSet)
router.register(r'tasks', views.TaskViewSet)
router.register(r'subtasks', views.SubTaskViewSet)

router.register(r'issues', views.IssueViewSet)

router.register(r'installationteams', views.InstallationTeamViewSet)
router.register(r'electricaltasks', views.ElectricalTaskViewSet)

router.register(r'generatortasks', views.GeneratorInstallationViewSet)
router.register(r'generatortasksdates', views.GeneratorInstallationDateViewSet)
router.register(r'generatortasksimages', views.GeneratorInstallationImageViewSet)

router.register(r'earthingtasks', views.EarthingSubtaskViewSet)
router.register(r'earthingtaskdates', views.EarthingDatesViewSet)
router.register(r'earthingtaskimages', views.EarthingImagesViewSet)

router.register(r'reticulationtasks', views.ReticulationAPSViewSet)
router.register(r'reticulationtaskdates', views.ReticulationAPSDatesViewSet)
router.register(r'reticulationtaskimages', views.ReticulationAPSImagesViewSet)

router.register(r'undergroundtasks', views.UndergroundTasksViewSet)
router.register(r'undergroundtaskdates', views.UndergroundTaskDatesViewSet)
router.register(r'undergroundtaskimages', views.UndergroundTaskImagesViewSet)

router.register(r'telecomtasks', views.TelecomTaskViewSet)

router.register(r'mwinstallationtasks', views.MWInstallationTasksViewSet)
router.register(r'mwinstallationtaskdates', views.MWInstallationTaskDatesViewSet)
router.register(r'mwinstallationtaskimages', views.MWInstallationTaskImagesViewSet)

router.register(r'btsinstallationtasks', views.BTSInstallationTasksViewSet)
router.register(r'btsinstallationtaskdates', views.BTSInstallationTaskDatesViewSet)
router.register(r'btsinstallationtaskimages', views.BTSInstallationTaskImagesViewSet)

router.register(r'kplcsolarsmages', views.KPLCSolarImageViewSet)

router.register(r'healthdocumentsinstallationteams', views.HealthDocumentsInstallationTeamViewset)
router.register(r'accessapprovalinstallations', views.AccessApprovalInstallationViewSet)
router.register(r'warrantyCertificates', views.WarrantyCertificateViewSet)
router.register(r'testCetificates', views.TestCetificateViewSet)

""" ENDPOINTS FOR FRONTEND"""


urlpatterns = [
    path('', include(router.urls)),
    # ENDPOINTS FOR DASHBOARD
    path('projectprogress/<int:pk>', ProjectProgressView.as_view()),
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

    #PROJECT FILES # allow  GET Method only

    path('files/', filesviews.FilesView.as_view()), # Retrieve all projects files :: TO DO

    path('files/<int:pk>/', filesviews.BtsSiteFilesView.as_view()), # main url path to retrieve files per project

    path('files/<int:pk>/siteclearingimages/', filesviews.SiteClearingSubTaskFilesView.as_view()),
    path('files/<int:pk>/towerbaseimages/', filesviews.TowerBaseSubTaskFilesView.as_view()),
    path('files/<int:pk>/bindingimages/', filesviews.BlindingSubTaskView.as_view()),
    path('files/<int:pk>/steelfixformworkimages/', filesviews.SteelFixFormworkFilesView.as_view()),
    path('files/<int:pk>/concretepourimages/', filesviews.ConcretePourFilesView.as_view()),
    path('files/<int:pk>/concretecuringimages/', filesviews.ConcreteCuringPeriodFilesView.as_view()),

    path('files/<int:pk>/excavationimages/', filesviews.ExcavationFilesView.as_view()),
    path('files/<int:pk>/concretepourcuringperiodimages/', filesviews.BS241ConcretePourCuringPeriodFilesView.as_view()),

    path('files/<int:pk>/foundfootpourimage/', filesviews.FoundFootPourFilesView.as_view()),
    path('files/<int:pk>/blockworkpanelconstimages/', filesviews.BlockworkPanelConstFilesView.as_view()),
    path('files/<int:pk>/gateinstallationimages/', filesviews.GateInstallationFilesView.as_view()),
    path('files/<int:pk>/razorelectricfenceimages/', filesviews.RazorElectricFenceFilesView.as_view()),

    path('files/<int:pk>/towererectionimages/', filesviews.TowerErectionFilesView.as_view()),
    path('files/<int:pk>/towerpaintimages/', filesviews.TowerPaintFilesView.as_view()),
    path('files/<int:pk>/cablewaysimages/', filesviews.CableWaysFilesView.as_view()),
    path('files/<int:pk>/antennacoaxinstallimages/', filesviews.AntennaCoaxInstallFilesView.as_view()),

    path('files/<int:pk>/undergroundtasks/', filesviews.UndergroundTaskFilesView.as_view()),

    path('taskstatus/', TaskStatusView.as_view()),
    path('timesheetsummary/', TimesheetSummaryView.as_view()),
    path('issuestatus/', IssueStatusView.as_view()),
    path('turnaroundtime/', TurnAroundTimeView.as_view()),
    path('totalpurchaseprders/', TotalPurchaseOrdersView.as_view()),
    path('revenueperproject/<int:pk>', RevenueDetailView.as_view()),
    path('revenue/', RevenueListView.as_view()),


]

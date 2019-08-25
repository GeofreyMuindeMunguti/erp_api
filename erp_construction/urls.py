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
# router.register(r'category', views.CategoryViewSet)
# router.register(r'Icons', views.ProjectIconViewSet)
# router.register(r'projectcosting', views.ProjectCostingViewSet)
# router.register(r'projectpos', views.ProjectPOSViewSet)
# router.register(r'commercialteamtasks', views.CommercialTeamViewSet)
# router.register(r'procurementteamtasks', views.ProcurementTeamViewSet)
# router.register(r'healthdocscivil', views.HealthDocCivilViewSet)
# router.register(r'accessapprovalscivil', views.AccessApprovalCivilViewSet)
# router.register(r'civilteamtasks', views.CivilTeamViewSet)


# TASK[1] : Foundation Building
router.register(r'foundationimages', views.FoundationCreationTaskViewSet)
         # SubTask (1): Site-Clearing Subtask 
router.register(r'setclearingsubtasks', views.SiteClearingSubTaskViewSet)
router.register(r'setclearingdays', views.SiteClearingDateViewSet)
router.register(r'setclearingimages', views.SiteClearingImageViewSet)

         # SubTask (2): Tower-Base Subtask
router.register(r'towerbasesubtasks', views.TowerBaseSubTaskViewSet)
router.register(r'towerbasedays', views.TowerBaseDateViewSet)
router.register(r'towerbaseimages', views.TowerBaseImageViewSet)

         # SubTask (3): Blinding Subtask
router.register(r'blindingsubtasks', views.BlindingSubTaskViewSet)
router.register(r'blindingdates', views.BlindingDateViewSet)
router.register(r'blindingimages', views.BlindingImageViewSet)

         # SubTask (4): Steel Fix Subtask
router.register(r'steelfixformworkimages', views.SteelFixFormworkSubtaskViewSet)
router.register(r'steelfixformworkimages', views.SteelFixFormworkDateViewSet)
router.register(r'steelfixformworkimages', views.SteelFixFormworkImageViewSet)

         # SubTask (4): Steel Fix Subtask
router.register(r'concretepourimages', views.ConcretePourSubTaskViewSet)
router.register(r'concretepourimages', views.ConcretePourDateViewSet)
router.register(r'concretepourimages', views.ConcretePourImageViewSet)

         # SubTask (4): Concrete Curing Period Subtask
router.register(r'concretecuringperiodsubtask', views.ConcreteCuringPeriodSubTaskViewSet)
router.register(r'concretecuringperioddate', views.ConcreteCuringPeriodDateViewSet)
router.register(r'concretecuringperiodimage', views.ConcreteCuringPeriodImageViewSet)


# TASK[2] : Excavation & Generator

# router.register(r'excavation', views.ExcavationImageViewSet)
# router.register(r'bs241concretepourcuringperiod', views.bs241ConcretePourCuringPeriodImageViewSet)
# router.register(r'bs241generatorslabs', views.BS241AndGeneatorSlabsImageViewSet)


# router.register(r'foundationfootpour', views.FoundFootPourImageViewSet)
# router.register(r'blockworkpanelconstruct', views.BlockworkPanelConstImageViewSet)
# router.register(r'gateinstallation', views.GateInstallationImageViewSet)
# router.register(r'razorelectricfence', views.RazorElectricFenceImageViewSet)
# router.register(r'boundarywall', views.BoundaryWallImageViewSet)

# router.register(r'towerantennacoax', views.TowerAntennaCoaxImageViewSet)
# router.register(r'towererection', views.TowerErectionImageViewSet)
# router.register(r'towerpaint', views.TowerPaintImageViewSet)
# router.register(r'cableways', views.CableWaysImageViewSet)
# router.register(r'antennacoaxinstallation', views.AntennaCoaxInstallImageViewSet)


# router.register(r'kpi', views.KpiViewSet)
# router.register(r'tasks', views.TaskViewSet)
# router.register(r'subtasks', views.SubTaskViewSet)

# router.register(r'issues', views.IssuesViewSet)
# router.register(r'installationteams', views.InstallationTeamViewSet)
# router.register(r'electricaltasks', views.ElectricalTasksViewSet)
# router.register(r'generatortasks', views.GeneratorInstallationViewSet)
# router.register(r'earthingtasks', views.EarthingViewSet)
# router.register(r'reticulationtasks', views.ReticulationAPSViewSet)
# router.register(r'undergroundtasks', views.UndergroundTasksViewSet)
# router.register(r'telecomtasks', views.TelecomTasksViewSet)
# router.register(r'mwinstallationtasks', views.MWInstallationTasksViewSet)
# router.register(r'btsinstallationtasks', views.BTSInstallationTasksViewSet)
# router.register(r'healthdocumentsinstallationteams', views.HealthDocumentsInstallationTeamViewset)
# router.register(r'accessapprovalinstallations', views.AccessApprovalInstallationViewSet)
# router.register(r'kplcsolarsmages', views.KPLCSolarImageViewSet)
# router.register(r'warrantyCertificates', views.WarrantyCertificateViewSet)
# router.register(r'testCetificates', views.TestCetificateViewSet)

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
    #Paths to retrieve individual files
    # path('files/<int:pk>/commercialteamfiles/', filesviews.CommercialTeamFilesView.as_view()),
    # path('files/<int:pk>/procurementteamfiles/', filesviews.ProcurementTeamFilesView.as_view()),
    # path('files/<int:pk>/projectpurchaseorders/', filesviews.ProjectPurchaseOrdersView.as_view()),
    # path('files/<int:pk>/projectcostingfile/', filesviews.ProjectCostingFileView.as_view()),

    path('files/<int:pk>/siteclearingimages/', filesviews.SiteClearingSubTaskFilesView.as_view()),
    path('files/<int:pk>/towerbaseimages/', filesviews.TowerBaseSubTaskFilesView.as_view()),
    # path('files/<int:pk>/bindingimages/', filesviews.BindingImagesView.as_view()),
    # path('files/<int:pk>/steelfixformworkimages/', filesviews.SteelFixFormworkImagesView.as_view()),
    # path('files/<int:pk>/concretepourimages/', filesviews.ConcretePourImagesView.as_view()),
    # path('files/<int:pk>/concretecuringimages/', filesviews.ConcreteCuringImagesView.as_view()),

    # path('files/<int:pk>/excavationimages/', filesviews.ExcavationImagesView.as_view()),
    # path('files/<int:pk>/concretepourcuringperiodimages/', filesviews.BS241ConcreteCuringPeriodImagesView.as_view()),

    # path('files/<int:pk>/foundfootpourimage/', filesviews.FoundFootPourImageView.as_view()),
    # path('files/<int:pk>/blockworkpanelconstimages/', filesviews.BlockworkPanelConstImagesView.as_view()),
    # path('files/<int:pk>/gateinstallationimages/', filesviews.GateInstallationImagesView.as_view()),
    # path('files/<int:pk>/razorelectricfenceimages/', filesviews.RazorElectricFenceImagesView.as_view()),

    # path('files/<int:pk>/towererectionimages/', filesviews.TowerErectionImagesView.as_view()),
    # path('files/<int:pk>/towerpaintimages/', filesviews.TowerPaintImagesView.as_view()),
    # path('files/<int:pk>/cablewaysimages/', filesviews.CableWaysImagesView.as_view()),
    # path('files/<int:pk>/antennacoaxinstallimages/', filesviews.AntennaCoaxInstallImagesView.as_view()),

    # path('files/<int:pk>/healthdocumentsfilescivilteam/', filesviews.HealthDocumentsFilesCivilTeamView.as_view()),
    # path('files/<int:pk>/accessapprovalfilecivil/', filesviews.AccessApprovalFileCivilView.as_view()),
    # path('files/<int:pk>/healthdocumentsfilesinstallationteam/', filesviews.HealthDocumentsFilesInstallationTeamView.as_view()),
    # path('files/<int:pk>/accessapprovalfileinstallation/', filesviews.AccessApprovalFileInstallationView.as_view()),

    # path('files/<int:pk>/undergroundtasks/', filesviews.UndergroundTasksFilesView.as_view()),
    # path('files/<int:pk>/reticulationapsinstallationfiles/', filesviews.ReticulationAPSinstallationFilesView.as_view()),
    # path('files/<int:pk>/electricalearthingimages/', filesviews.ElectricalEarthingImagesView.as_view()),
    # path('files/<int:pk>/generatorinstallationimages/', filesviews.GeneratorInstallationImagesView.as_view()),
    # path('files/<int:pk>/kplcsolar/', filesviews.KPLCSolarImagesView.as_view()),

    # path('files/<int:pk>/btsinstallationtaskimages/', filesviews.BTSinstallationTaskImagesView.as_view()),
    # path('files/<int:pk>/mwinstallationtaskimages/', filesviews.MWInstallationTaskImagesView.as_view()),
    # path('files/<int:pk>/installationteamfiles/', filesviews.InstallationTeamFilesView.as_view()),
    # path('files/<int:pk>/issueimages/', filesviews.IssueImageView.as_view()),

    path('taskstatus/', TaskStatusView.as_view()),
    path('timesheetsummary/', TimesheetSummaryView.as_view()),
    path('issuestatus/', IssueStatusView.as_view()),
    path('turnaroundtime/', TurnAroundTimeView.as_view()),
    path('totalpurchaseprders/', TotalPurchaseOrdersView.as_view()),
    path('revenueperproject/<int:pk>', RevenueDetailView.as_view()),
    path('revenue/', RevenueListView.as_view()),





    # Daily Subtask Images  # TO DO > Better Url paths
    # path('setclearingsubtasks/<int:pk>/setclearingday/', views.DailySiteClearingList.as_view()),
    # path('setclearingsubtasks/<int:pk>/setclearingday/<int:day_pk>/seteclearingimage/', views.SiteClearingImageView.as_view()),


        #PROJECT FILES # allow  GET Method only

    # path('files/', filesviews.FilesView.as_view()), # Retrieve all projects files :: TO DO

    # path('files/<int:pk>/', filesviews.BtsSiteFilesView.as_view()), # main url path to retrieve files per project
    #Paths to retrieve individual files
    # path('files/<int:pk>/commercialteamfiles/', filesviews.CommercialTeamFilesView.as_view()),
    # path('files/<int:pk>/procurementteamfiles/', filesviews.ProcurementTeamFilesView.as_view()),
    # path('files/<int:pk>/projectpurchaseorders/', filesviews.ProjectPurchaseOrdersView.as_view()),
    # path('files/<int:pk>/projectcostingfile/', filesviews.ProjectCostingFileView.as_view()),

    # path('files/<int:pk>/siteclearingimages/', filesviews.SiteClearingSubTaskFilesView.as_view()),
    # path('files/<int:pk>/towerbaseimages/', filesviews.TowerBaseSubTaskView.as_view()),
    # path('files/<int:pk>/bindingimages/', filesviews.BindingImagesView.as_view()),
    # path('files/<int:pk>/steelfixformworkimages/', filesviews.SteelFixFormworkImagesView.as_view()),
    # path('files/<int:pk>/concretepourimages/', filesviews.ConcretePourImagesView.as_view()),
    # path('files/<int:pk>/concretecuringimages/', filesviews.ConcreteCuringImagesView.as_view()),

    # path('files/<int:pk>/excavationimages/', filesviews.ExcavationImagesView.as_view()),
    # path('files/<int:pk>/concretepourcuringperiodimages/', filesviews.BS241ConcreteCuringPeriodImagesView.as_view()),

    # path('files/<int:pk>/foundfootpourimage/', filesviews.FoundFootPourImageView.as_view()),
    # path('files/<int:pk>/blockworkpanelconstimages/', filesviews.BlockworkPanelConstImagesView.as_view()),
    # path('files/<int:pk>/gateinstallationimages/', filesviews.GateInstallationImagesView.as_view()),
    # path('files/<int:pk>/razorelectricfenceimages/', filesviews.RazorElectricFenceImagesView.as_view()),

    # path('files/<int:pk>/towererectionimages/', filesviews.TowerErectionImagesView.as_view()),
    # path('files/<int:pk>/towerpaintimages/', filesviews.TowerPaintImagesView.as_view()),
    # path('files/<int:pk>/cablewaysimages/', filesviews.CableWaysImagesView.as_view()),
    # path('files/<int:pk>/antennacoaxinstallimages/', filesviews.AntennaCoaxInstallImagesView.as_view()),

    # path('files/<int:pk>/healthdocumentsfilescivilteam/', filesviews.HealthDocumentsFilesCivilTeamView.as_view()),
    # path('files/<int:pk>/accessapprovalfilecivil/', filesviews.AccessApprovalFileCivilView.as_view()),
    # path('files/<int:pk>/healthdocumentsfilesinstallationteam/', filesviews.HealthDocumentsFilesInstallationTeamView.as_view()),
    # path('files/<int:pk>/accessapprovalfileinstallation/', filesviews.AccessApprovalFileInstallationView.as_view()),

    # path('files/<int:pk>/undergroundtasks/', filesviews.UndergroundTasksFilesView.as_view()),
    # path('files/<int:pk>/reticulationapsinstallationfiles/', filesviews.ReticulationAPSinstallationFilesView.as_view()),
    # path('files/<int:pk>/electricalearthingimages/', filesviews.ElectricalEarthingImagesView.as_view()),
    # path('files/<int:pk>/generatorinstallationimages/', filesviews.GeneratorInstallationImagesView.as_view()),
    # path('files/<int:pk>/kplcsolar/', filesviews.KPLCSolarImagesView.as_view()),

    # path('files/<int:pk>/btsinstallationtaskimages/', filesviews.BTSinstallationTaskImagesView.as_view()),
    # path('files/<int:pk>/mwinstallationtaskimages/', filesviews.MWInstallationTaskImagesView.as_view()),
    # path('files/<int:pk>/installationteamfiles/', filesviews.InstallationTeamFilesView.as_view()),
    # path('files/<int:pk>/issueimages/', filesviews.IssueImageView.as_view()),

]

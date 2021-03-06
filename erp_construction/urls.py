from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from django.urls import path, include
from .views import *
from .progress import *
from .monitoring import *
from .scorecard import *
from erp_construction.btsfiles import filesviews  # UploadToProjectDir ,UploadToProjectDirDate ,UploadToProjectDirSubTask ,UploadToProjectDirImage
from erp_construction.btsfiles.filesserializers import *

file_path = 'BTSProjects'



router = DefaultRouter()

router.register(r'btsproject', views.BtsProjectViewSet)
router.register(r'IRROF7Free', views.IRROF7FreeViewSet)
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

router.register(r'foundationimages', views.FoundationImageViewSet)
###Geo_changes
router.register(r'setclearingimages', views.SetSiteClearingImageViewSet)
router.register(r'setclearingimagesdaily', views.SiteClearingImageDailyViewSet)
router.register(r'setclearingdates', views.SiteClearingDateViewSet)
####end
###Geo_changes
router.register(r'towerbaseimages', views.TowerBaseImageViewSet)
router.register(r'towerbaseimagesdaily', views.TowerBaseImageDailyViewSet)
router.register(r'towerbasedates', views.TowerBaseDateViewSet)
###end

##Geo_Changes
router.register(r'bindingimages', views.BindingImageViewSet)
router.register(r'bindingimagesdaily', views.BindingImageDailyViewSet)
router.register(r'bindingdates', views.BindingDateViewSet)

###End
##Geo_changes
router.register(r'steelfixformworkimages', views.SteelFixFormworkImageViewSet)
router.register(r'steelfixformworkimagesdaily', views.SteelFixFormworkImageDailyViewSet)
router.register(r'steelfixformworkdates', views.SteelFixFormworkDateViewSet)
###End
###Geo_changes
router.register(r'concretepourimages', views.ConcretePourImageViewSet)
router.register(r'concretepourimagesdaily', views.ConcretePourImageDailyViewSet)
router.register(r'concretepourdate', views.ConcretePourDateViewSet)
###End

###Geo_changes
router.register(r'ConcreteCuringPeriodDocs', views.ConcreteCuringPeriodDocsViewSet)
router.register(r'ConcreteCuringPeriodImage', views.ConcreteCuringPeriodImageViewSet)
router.register(r'ConcreteCuringPeriodImageDaily', views.ConcreteCuringPeriodImageDailyViewSet)
router.register(r'ConcreteCuringPeriodDate', views.ConcreteCuringPeriodDateViewSet)

###End
router.register(r'concretecuringperiod', views.ConcreteCuringPeriodImageViewSet)
###Geo_changes
router.register(r'DeliveryOfMaterialandEquipement', views.DeliveryOfMaterialandEquipementViewSet)
router.register(r'DeliveryOfMaterialandEquipementdaily', views.DeliveryOfMaterialandEquipementDailyViewSet)
router.register(r'DeliveryOfMaterialandEquipementdates', views.DeliveryOfMaterialandEquipementDateViewSet)

##End
###Geo_change
router.register(r'excavation', views.ExcavationImageViewSet)
router.register(r'excavationimagedaily', views.ExcavationImageDailyViewSet)
router.register(r'excavationdate', views.ExcavationDateViewSet)
####

##Geo_changes
router.register(r'bs241concretepourcuringperiod', views.bs241ConcretePourCuringPeriodImageViewSet)
router.register(r'bs241concretepourcuringperiodimagedaily', views.bs241ConcretePourCuringPeriodImageDailyViewSet)
router.register(r'bs241concretepourcuringperioddates', views.bs241ConcretePourCuringPeriodDateViewSet)
###End

####Geo_changes
router.register(r'BS241Image', views.BS241ImageViewSet)
router.register(r'BS241Imagedaily', views.BS241ImageDailyViewSet)
router.register(r'BS241Date', views.BS241DateViewSet)
###End
router.register(r'bs241generatorslabs', views.BS241AndGeneatorSlabsImageViewSet)

###Geo_changes
router.register(r'GenExcavationImage', views.GenExcavationImageViewSet)
router.register(r'GenExcavationImageDaily', views.GenExcavationImageDailyViewSet)
router.register(r'GenExcavationDate', views.GenExcavationDateViewSet)

router.register(r'GenConcretePourCuringPeriodImage', views.GenConcretePourCuringPeriodImageViewSet)
router.register(r'GenConcretePourCuringPeriodImageDaily', views.GenConcretePourCuringPeriodImageDailyViewSet)
router.register(r'GenConcretePourCuringPeriodDate', views.GenConcretePourCuringPeriodDateViewSet)

router.register(r'GenCableConduitsSettingImage', views.GenCableConduitsSettingImageViewSet)
router.register(r'GenCableConduitsSettingImageDaily', views.GenCableConduitsSettingImageDailyViewSet)
router.register(r'GenCableConduitsSettingDate', views.GenCableConduitsSettingDateViewSet)

###End
router.register(r'GeneatorSlabsImage', views.GeneatorSlabsImageViewSet)

router.register(r'fabricationRooftopImages', views.FabricationRooftopImageViewSet)
router.register(r'fabricationQualityInspectionImages', views.FabricationQualityInspectionImageViewSet)
router.register(r'fabricationSteelDeckImages', views.FabricationSteelDeckImageViewSet)
router.register(r'galvanisationImages', views.GalvanisationImageViewSet)

router.register(r'hackingExistingColumnsImages', views.HackingExistingColumnsImageViewSet)
router.register(r'formworkColumnsConcretePourCuringImages', views.FormworkColumnsConcretePourCuringImageViewSet)
router.register(r'deliveryToSiteImages', views.DeliveryToSiteImageViewSet)
router.register(r'liftingHoistingFreeIssueImages', views.LiftingHoistingFreeIssueImageViewSet)
router.register(r'fenceInstallationImages', views.FenceInstallationImageViewSet)
router.register(r'siteRestorationImages', views.SiteRestorationImageViewSet)
router.register(r'installationRooftopImages', views.InstallationRooftopImageViewSet)

router.register(r'foundationfootpour', views.FoundFootPourImageViewSet)
router.register(r'bwconcretepourcuringperiod', views.BWConcretePourCuringPeriodImageViewSet)
router.register(r'excavationstripfoundations', views.ExcavationstripFoundationsImageViewSet)
router.register(r'bwcableconduits', views.BWCableConduitsImageViewSet)
router.register(r'bwblinding', views.BWBlindingImageViewSet)
router.register(r'blockworkpanelconstruct', views.BlockworkPanelConstImageViewSet)
router.register(r'gateinstallation', views.GateInstallationImageViewSet)
router.register(r'razorelectricfence', views.RazorElectricFenceImageViewSet)
router.register(r'boundarywall', views.BoundaryWallImageViewSet)

router.register(r'ManholeSettingExcavationImage', views.ManholeSettingExcavationImageViewSet)
router.register(r'ManholeBlinding', views.ManholeBlindingViewSet)
router.register(r'ManholeBlockwork', views.ManholeBlockworkViewSet)
router.register(r'ManholeSettingOutConstructionImage', views.ManholeSettingOutConstructionImageViewSet)

router.register(r'towererection', views.TowerErectionImageViewSet)
router.register(r'towerpaint', views.TowerPaintImageViewSet)
router.register(r'cableways', views.CableWaysImageViewSet)
router.register(r'cableinstallation', views.CableInstallationImageViewSet)
router.register(r'earthinstallation', views.EarthInstallationImageViewSet)
router.register(r'aviationlightsinstallation', views.AviationLightsInstallationImageViewSet)
router.register(r'towerdelivery', views.TowerDeliveryImageViewSet)
router.register(r'antennacoaxinstallation', views.AntennaCoaxInstallImageViewSet)
router.register(r'towerantennacoax', views.TowerAntennaCoaxImageViewSet)


router.register(r'kpi', views.KpiViewSet)
router.register(r'tasks', views.TaskViewSet)
router.register(r'subtasks', views.SubTaskViewSet)

router.register(r'issues', views.IssuesViewSet)
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

    # path('files/', filesviews.FilesView.as_view()), # Retrieve all projects files :: TO DO
    #
    # path('files/<int:pk>/', filesviews.SiteFilesView.as_view()), # main url path to retrieve files per project
    #Paths to retrieve individual files
    path('files/<int:pk>/commercialteamfiles/', filesviews.CommercialTeamFilesView.as_view()),
    path('files/<int:pk>/procurementteamfiles/', filesviews.ProcurementTeamFilesView.as_view()),
    path('files/<int:pk>/projectpurchaseorders/', filesviews.ProjectPurchaseOrdersView.as_view()),
    path('files/<int:pk>/projectcostingfile/', filesviews.ProjectCostingFileView.as_view()),

    path('files/<int:pk>/siteclearingimages/', filesviews.SiteClearingFilesView.as_view()),
    path('files/<int:pk>/towerbaseimages/', filesviews.TowerBaseImagesView.as_view()),
    path('files/<int:pk>/bindingimages/', filesviews.BindingImagesView.as_view()),
    path('files/<int:pk>/steelfixformworkimages/', filesviews.SteelFixFormworkImagesView.as_view()),
    path('files/<int:pk>/concretepourimages/', filesviews.ConcretePourImagesView.as_view()),
    path('files/<int:pk>/concretecuringimages/', filesviews.ConcreteCuringImagesView.as_view()),

    path('files/<int:pk>/excavationimages/', filesviews.ExcavationImagesView.as_view()),
    path('files/<int:pk>/concretepourcuringperiodimages/', filesviews.ConcreteCuringPeriodImagesView.as_view()),

    path('files/<int:pk>/foundfootpourimage/', filesviews.FoundFootPourImageView.as_view()),
    path('files/<int:pk>/bwcableconduitsimage/', filesviews.BWCableConduitsImageView.as_view()),
    path('files/<int:pk>/bwblindingimage/', filesviews.BWBlindingImageView.as_view()),
    path('files/<int:pk>/excavationstripfoundationsimage/', filesviews.ExcavationstripFoundationsImageView.as_view()),
    path('files/<int:pk>/bwconcretepourcuringperiodimage/', filesviews.BWConcretePourCuringPeriodImageView.as_view()),

    path('files/<int:pk>/blockworkpanelconstimages/', filesviews.BlockworkPanelConstImagesView.as_view()),
    path('files/<int:pk>/gateinstallationimages/', filesviews.GateInstallationImagesView.as_view()),
    path('files/<int:pk>/razorelectricfenceimages/', filesviews.RazorElectricFenceImagesView.as_view()),

    path('files/<int:pk>/towererectionimages/', filesviews.TowerErectionImagesView.as_view()),
    path('files/<int:pk>/towerpaintimages/', filesviews.TowerPaintImagesView.as_view()),
    path('files/<int:pk>/aviationlightsinstallationimages/', filesviews.AviationLightsInstallationImageView.as_view()),
    path('files/<int:pk>/earthinstallationimages/', filesviews.EarthInstallationImageView.as_view()),
    path('files/<int:pk>/cableinstallationimages/', filesviews.CableInstallationImageView.as_view()),
    path('files/<int:pk>/towerdeliveryimages/', filesviews.TowerDeliveryImageView.as_view()),
    path('files/<int:pk>/cablewaysimages/', filesviews.CableWaysImagesView.as_view()),

    path('files/<int:pk>/antennacoaxinstallimages/', filesviews.AntennaCoaxInstallImagesView.as_view()),

    path('files/<int:pk>/healthdocumentsfilescivilteam/', filesviews.HealthDocumentsFilesCivilTeamView.as_view()),
    path('files/<int:pk>/accessapprovalfilecivil/', filesviews.AccessApprovalFileCivilView.as_view()),
    path('files/<int:pk>/healthdocumentsfilesinstallationteam/', filesviews.HealthDocumentsFilesInstallationTeamView.as_view()),
    path('files/<int:pk>/accessapprovalfileinstallation/', filesviews.AccessApprovalFileInstallationView.as_view()),

    path('files/<int:pk>/undergroundtasks/', filesviews.UndergroundTasksFilesView.as_view()),
    path('files/<int:pk>/reticulationapsinstallationfiles/', filesviews.ReticulationAPSinstallationFilesView.as_view()),
    path('files/<int:pk>/electricalearthingimages/', filesviews.ElectricalEarthingImagesView.as_view()),
    path('files/<int:pk>/generatorinstallationimages/', filesviews.GeneratorInstallationImagesView.as_view()),
    path('files/<int:pk>/kplcsolar/', filesviews.KPLCSolarImagesView.as_view()),

    path('files/<int:pk>/btsinstallationtaskimages/', filesviews.BTSinstallationTaskImagesView.as_view()),
    path('files/<int:pk>/mwinstallationtaskimages/', filesviews.MWInstallationTaskImagesView.as_view()),
    path('files/<int:pk>/installationteamfiles/', filesviews.InstallationTeamFilesView.as_view()),
    path('files/<int:pk>/issueimages/', filesviews.IssueImageView.as_view()),

    path('files/<int:pk>/galvanisationImages/', filesviews.GalvanisationImageFilesView.as_view()),
    path('files/<int:pk>/fabricationsteeldeckimages/', filesviews.FabricationSteelDeckImageFilesView.as_view()),
    path('files/<int:pk>/fabricationqualityinspectionimages/', filesviews.FabricationQualityInspectionImageFilesView.as_view()),

    path('files/<int:pk>/hackingexistingcolumnsimages/', filesviews.HackingExistingColumnsImageFilesView.as_view()),
    path('files/<int:pk>/formworkcolumnsconcretepourcuringimages/', filesviews.FormworkColumnsConcretePourCuringImageFilesView.as_view()),
    path('files/<int:pk>/deliverytositeimage/', filesviews.DeliveryToSiteImageFilesView.as_view()),
    path('files/<int:pk>/liftinghoistingfreeissueimage/', filesviews.LiftingHoistingFreeIssueImageFilesView.as_view()),
    path('files/<int:pk>/fenceinstallationimage/', filesviews.FenceInstallationImageFilesView.as_view()),
     path('files/<int:pk>/siterestorationimage/', filesviews.SiteRestorationImageFilesView.as_view()),

    path('taskstatus/', TaskStatusView.as_view()),
    path('timesheetsummary/', TimesheetSummaryView.as_view()),
    path('issuestatus/', IssueStatusView.as_view()),
    path('turnaroundtime/', TurnAroundTimeView.as_view()),
    path('totalpurchaseprders/', TotalPurchaseOrdersView.as_view()),
    path('revenueperproject/<int:pk>', RevenueDetailView.as_view()),
    path('revenue/', RevenueListView.as_view()),

]

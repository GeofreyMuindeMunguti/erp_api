"""Extract files and images per project.
"""
#---------
# Imports
#---------
from rest_framework import serializers  #, exceptions
from erp_construction.models import *

excluded_fields = ("id","site_name","site_number","BTS_type","site_owner","final_acceptance_cert_comment","created_at",
           "updated_at", "is_active","icon", "location", "created_by","geotech_file","access_letter","approved_drawing","final_acceptance_cert","project_name",)


############################ PROJECT FILES SERIALIZERS ###############################################

#|||||||||| Site Crearing Images|||||

class SiteClearingSubTaskFilesSerializer(serializers.ModelSerializer):
    #siteclearingdates =SiteClearingDateFilesSerializer(many = True,read_only =True)

    class Meta:
        model = SetSiteClearingImage
        fields = ('id','project_name_id','setting_site_clearing_image_1','setting_site_clearing_image_2','setting_site_clearing_image_3','setting_site_clearing_comment',)

class SiteClearingFilesSerializer(serializers.ModelSerializer):
    setsiteclearingimage = SiteClearingSubTaskFilesSerializer(read_only =True)

    class Meta:
        model = BtsSite
        exclude = excluded_fields



#|||||||||| TowerBaseSubTask  Files  Images|||||



class TowerBaseImagesASerializer(serializers.ModelSerializer):

    class Meta:
        model = TowerBaseImage
        fields = ('towerbase_image_1', 'towerbase_image_2', 'towerbase_image_3',)

class TowerBaseImagesSerializer(serializers.ModelSerializer):
    towerbaseimage = TowerBaseImagesASerializer(read_only =True)

    class Meta:
        model = BtsSite
        exclude = excluded_fields


#|||||||||| BindingSubTask  Files  Images|||||
class BindingImagesASerializer(serializers.ModelSerializer):

    class Meta:
        model = BindingImage
        fields = ('binding_image_1','binding_image_2','binding_image_3',)

class BindingImagesSerializer(serializers.ModelSerializer):
    bindingimage = BindingImagesASerializer(read_only =True)

    class Meta:
        model = BtsSite
        exclude = excluded_fields

#|||||||||| SteelFix SubTask  Files  Images|||||

class SteelFixFormworkImagesASerializer(serializers.ModelSerializer):

    class Meta:
        model = SteelFixFormworkImage
        fields = ('steel_fix_formwork_image_1', 'steel_fix_formwork_image_2', 'steel_fix_formwork_image_3', 'steel_fix_formwork_comment',)

class SteelFixFormworkImagesSerializer(serializers.ModelSerializer):
    steelfixformworkimage = SteelFixFormworkImagesASerializer(read_only =True)

    class Meta:
        model = BtsSite
        exclude = excluded_fields

#|||||||||| Concreate pour Images|||||


class ConcretePourImagesASerializer(serializers.ModelSerializer):

    class Meta:
        model = ConcretePourImage
        fields = ('concrete_pour_curing_image_1', 'concrete_pour_curing_image_2', 'concrete_pour_curing_image_3', 'concrete_pour_curing_comment',)

class ConcretePourImagesSerializer(serializers.ModelSerializer):
    concretepourimage = ConcretePourImagesASerializer(read_only =True)

    class Meta:
        model = BtsSite
        exclude =excluded_fields


#|||||||||| Concreate curing period Images|||||


class ConcreteCuringImagesASerializer(serializers.ModelSerializer):

    class Meta:
        model = ConcreteCuringPeriodImage
        fields = ('concrete_pour_curing_period_image_1', 'concrete_pour_curing_period_image_2', 'concrete_pour_curing_period_image_3', 'concrete_pour_curing_period_comment',)

class ConcreteCuringImagesSerializer(serializers.ModelSerializer):
    concretecuringperiodimage = ConcreteCuringImagesASerializer(read_only =True)

    class Meta:
        model = BtsSite
        exclude = excluded_fields

#GENERATOR FOUNDATION
#|||||||||| Excavation Images|||||

class ExcavationImagesASerializer(serializers.ModelSerializer):

    class Meta:
        model = ExcavationImage
        fields = ('excavation_image_1','excavation_image_2','excavation_image_3','excavation_comment')


class ExcavationImagesSerializer(serializers.ModelSerializer):
    excavationimage = ExcavationImagesASerializer(read_only =True)

    class Meta:
        model = BtsSite
        exclude = excluded_fields


#|||||||||| BS241ConcreteImages|||||


class ConcreteCuringPeriodImagesASerializer(serializers.ModelSerializer):

    class Meta:
        model = BS241ConcretePourCuringPeriodImage
        fields = ('bs241_concrete_pour_curing_period_image_1', 'bs241_concrete_pour_curing_period_image_2','bs241_concrete_pour_curing_period_image_3', 'bs241_concrete_pour_curing_period_comment',)

class ConcreteCuringPeriodImagesSerializer(serializers.ModelSerializer):
    bs241concretepourcuringperiodimage = ConcreteCuringPeriodImagesASerializer(read_only =True)

    class Meta:
        model = BtsSite
        exclude =excluded_fields

#  BOUNDARY WALL

#|||||||||| BS241ConcreteImages|||||

class FoundFootPourImagesASerializer(serializers.ModelSerializer):

    class Meta:
        model = FoundFootPourImage
        fields = ('foundfootpour_image_1', 'foundfootpour_image_2','foundfootpour_image_3', 'foundfootpour_comment',)

class FoundFootPourImagesSerializer(serializers.ModelSerializer):
    foundfootpourimage = FoundFootPourImagesASerializer(read_only =True)

    class Meta:
        model = BtsSite
        exclude = excluded_fields

#|||||||||| BlockworkPanel Images|||||

class BlockworkPanelConstImagesASerializer(serializers.ModelSerializer):

    class Meta:
        model = BlockworkPanelConstImage
        fields = ('blockwallpanelconst_image_1', 'blockwallpanelconst_image_2', 'blockwallpanelconst_image_3', 'blockwallpanelconst_comment',)

class BlockworkPanelConstImagesSerializer(serializers.ModelSerializer):
    blockworkpanelconstimage = BlockworkPanelConstImagesASerializer(read_only =True)

    class Meta:
        model = BtsSite
        exclude = excluded_fields

#|||||||||| GateInstallation Images|||||
class GateInstallationImagesASerializer(serializers.ModelSerializer):

    class Meta:
        model = GateInstallationImage
        fields = ('gateinstallation_image_1', 'gateinstallation_image_2', 'gateinstallation_image_3','gateinstallation_comment',)

class GateInstallationImagesSerializer(serializers.ModelSerializer):
    gateinstallationimage = GateInstallationImagesASerializer(read_only =True)

    class Meta:
        model = BtsSite
        exclude = excluded_fields

#||||||||||  RazorElectric Images|||||

class RazorElectricFenceImagesASerializer(serializers.ModelSerializer):

    class Meta:
        model = RazorElectricFenceImage
        fields = ('razorelectricfance_image_1', 'razorelectricfance_image_2', 'razorelectricfance_image_3', 'razorelectricfance_comment',)

class RazorElectricFenceImagesSerializer(serializers.ModelSerializer):
    razorelectricfenceimage = RazorElectricFenceImagesASerializer(read_only =True)

    class Meta:
        model = BtsSite
        exclude = excluded_fields

#||||||||||  RazorElectric Images|||||

#TOWER & ANTENNA_COAXs
#||||||||||  TowerErection Images|||||

class TowerErectionImagesASerializer(serializers.ModelSerializer):

    class Meta:
        model = TowerErectionImage
        fields = ('tower_erection_image_1','tower_erection_image_2','tower_erection_image_3','tower_erection_comment',)

class TowerErectionImagesSerializer(serializers.ModelSerializer):
    towererectionimage = TowerErectionImagesASerializer(read_only =True)

    class Meta:
        model = BtsSite
        exclude = excluded_fields

#||||||||||  TowerPaint Images|||||


class TowerPaintImagesASerializer(serializers.ModelSerializer):

    class Meta:
        model = TowerPaintImage
        fields = ('tower_painting_image_1','tower_painting_image_2','tower_painting_image_3',)

class TowerPaintImagesSerializer(serializers.ModelSerializer):
    towerpaintimage = TowerPaintImagesASerializer(read_only =True)

    class Meta:
        model = BtsSite
        exclude = excluded_fields


class CableWaysImagesASerializer(serializers.ModelSerializer):

    class Meta:
        model = CableWaysImage
        fields = ('cable_ways_image_1','cable_ways_image_2','cable_ways_image_3',)

class CableWaysImagesSerializer(serializers.ModelSerializer):
    cablewaysimage = CableWaysImagesASerializer(read_only =True)

    class Meta:
        model = BtsSite
        exclude = excluded_fields

class AntennaCoaxInstallImagesASerializer(serializers.ModelSerializer):

    class Meta:
        model = AntennaCoaxInstallImage
        fields = ('antenna_coax_installation_image_1','antenna_coax_installation_image_2','antenna_coax_installation_image_3',)

class AntennaCoaxInstallImagesSerializer(serializers.ModelSerializer):
    antennacoaxinstallimage = AntennaCoaxInstallImagesASerializer(read_only =True)

    class Meta:
        model = BtsSite
        exclude = excluded_fields
#END

class ProjectPurchaseOrdersFileSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProjectPurchaseOrders
        fields = ('po_file',)


class ProjectCostingFileSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProjectCosting
        fields = ('project_costing_file',)


class CommercialTeamFilesSerializer(serializers.ModelSerializer):

    class Meta:
        model = CommercialTeam
        fields = ('approved_quote_file','initial_invoice',)


class ProcurementTeamFilesSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProcurementTeam
        fields = ('po_steel', 'po_subcontractors', 'po_electrical_materials')


class HealthDocumentsFilesCivilTeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = HealthDocumentsCivilTeam
        fields = ('job_hazard_form', 'incident_notification_form', 'toolbox_meeting_form', 'communication_plan_form', 'safety_picture')


class AccessApprovalFileCivilSerializer(serializers.ModelSerializer):

    class Meta:
        model = AccessApprovalCivil
        fields = ('access_approval',)


class HealthDocumentsFilesAInstallationTeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = HealthDocumentsInstallationTeam
        fields = ('job_hazard_form', 'incident_notification_form', 'toolbox_meeting_form', 'communication_plan_form', 'safety_picture')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class HealthDocumentsFilesInstallationTeamSerializer(serializers.ModelSerializer):
    healthdocumentsinstallationteam = HealthDocumentsFilesAInstallationTeamSerializer(read_only =True)

    class Meta:
        model = BtsSite
        exclude = excluded_fields


class AccessApprovalFileInstallationSerializer(serializers.ModelSerializer):

    class Meta:
        model = AccessApprovalInstallation
        fields = ('access_approval',)
        read_only_fields = ('created_at', 'updated_at', 'is_active')

#||||||||||  TowerPaint Images|||||

class UndergroundTasksFilesASerializer(serializers.ModelSerializer):

    class Meta:
        model = UndergroundTasks
        fields = ('Underground_ducting_and_manholes_image_1','Underground_ducting_and_manholes_image_2','Underground_ducting_and_manholes_image_3',)

class UndergroundTasksFilesSerializer(serializers.ModelSerializer):
    undergroundtasks = UndergroundTasksFilesASerializer(read_only =True)

    class Meta:
        model = BtsSite
        exclude = excluded_fields
#||||||||||  ReticulationAPS Images|||||

class ReticulationAPSinstallationFilesASerializer(serializers.ModelSerializer):

    class Meta:
        model = ReticulationAPSinstallation
        fields = ('Electricalreticulation_APSInstallation_image_1','Electricalreticulation_APSInstallation_image_2','Electricalreticulation_APSInstallation_image_3')

class ReticulationAPSinstallationFilesSerializer(serializers.ModelSerializer):
    reticulationapsinstallation = ReticulationAPSinstallationFilesASerializer(read_only =True)

    class Meta:
        model = BtsSite
        exclude = excluded_fields
#||||||||||  ElectricalEarthing Images|||||

class ElectricalEarthingImagesASerializer(serializers.ModelSerializer):

    class Meta:
        model = ElectricalEarthing
        fields = ('Earthing_connections_and_testing_image_1','Earthing_connections_and_testing_image_2','Earthing_connections_and_testing_image_3',)

class ElectricalEarthingImagesSerializer(serializers.ModelSerializer):
    electricalearthing = ElectricalEarthingImagesASerializer(read_only =True)

    class Meta:
        model = BtsSite
        exclude = excluded_fields
#|||||||||| GeneratorInstallation Images|||||

class GeneratorInstallationImagesASerializer(serializers.ModelSerializer):

    class Meta:
        model = GeneratorInstallation
        fields = ('Generator_and_Fuel_Tank_Installation_image_1','Generator_and_Fuel_Tank_Installation_image_2','Generator_and_Fuel_Tank_Installation_image_3','before_fuel_image_1','before_fuel_image_2','after_fuel_image_1','after_fuel_image_2')

class GeneratorInstallationImagesSerializer(serializers.ModelSerializer):
    generatorinstallation = GeneratorInstallationImagesASerializer(read_only =True)

    class Meta:
        model = BtsSite
        exclude = excluded_fields
#||||||||||  KPLCSolar Images|||||

class KPLCSolarImagesASerializer(serializers.ModelSerializer):

    class Meta:
        model = KPLCSolarImage
        fields = ('kplc_solar_installation_image_1','kplc_solar_installation_image_2','kplc_solar_installation_image_3',)

class KPLCSolarImagesSerializer(serializers.ModelSerializer):
    kplcsolarimage = KPLCSolarImagesASerializer(read_only =True)

    class Meta:
        model = BtsSite
        exclude = excluded_fields

#||||||||||  BTSinstallation Images|||||

class BTSinstallationTaskImagesASerializer(serializers.ModelSerializer):

    class Meta:
        model = BTSinstallationTask
        fields = ('BTSinstallation_image_1','BTSinstallation_image_2','BTSinstallation_image_3',)

class BTSinstallationTaskImagesSerializer(serializers.ModelSerializer):
    btsinstallationtask = BTSinstallationTaskImagesASerializer(read_only =True)

    class Meta:
        model = BtsSite
        exclude = excluded_fields

#||||||||||  MWInstallation Images|||||
class MWInstallationTaskImagesASerializer(serializers.ModelSerializer):

    class Meta:
        model = MWInstallationTask
        fields = ('MWinstallation_image_1','MWinstallation_image_2','MWinstallation_image_3',)

class MWInstallationTaskImagesSerializer(serializers.ModelSerializer):
    mwinstallationtask = MWInstallationTaskImagesASerializer(read_only =True)

    class Meta:
        model = BtsSite
        exclude = excluded_fields

#||||||||||  InstallationTeamF Images|||||
class InstallationTeamFilesASerializer(serializers.ModelSerializer):

    class Meta:
        model = InstallationTeam
        fields = ('as_built', 'signoff', 'rfi_document', 'snag_document', 'conditional_acceptance_cert',)

class InstallationTeamFilesSerializer(serializers.ModelSerializer):
    installationteam = InstallationTeamFilesASerializer(read_only =True)

    class Meta:
        model = BtsSite
        exclude = excluded_fields

#||||||||||  TowerPaint Images|||||
class IssueImageASerializer(serializers.ModelSerializer):

    class Meta:
        model = Issues
        fields = ('issue_image', 'issue_sorted_image',)

class IRROF7FreeFilesSerializer(serializers.ModelSerializer):

    class Meta:
        model = IRROF7Free
        fields = ('tower_complete', 'free_issue_material', 'link_material',)


class IssueImageSerializer(serializers.ModelSerializer):
    issues = IssueImageASerializer(read_only =True)

    class Meta:
        model = BtsSite
        exclude = excluded_fields


################### Main Project Serializer################################

class SiteFilesSerializer(serializers.ModelSerializer):

    '''
    Main Serializer class : to access all serializers classes above
    :: facilitate serialization of all images and files per project
    :: Files that need not to be serialized can be commented out
     e.g
       # setsiteclearingimage = SiteClearingFilesSerializer ( read_only =True)
    :: More field can be added from the excluded one by removing from exlude variable

      '''

    setsiteclearingimage = SiteClearingSubTaskFilesSerializer(read_only =True)
    towerbaseimage = TowerBaseImagesASerializer(read_only =True)
    bindingimage = BindingImagesASerializer(read_only =True)
    steelfixformworkimage = SteelFixFormworkImagesASerializer(read_only=True)
    concretepourimage = ConcretePourImagesASerializer(read_only=True)
   # concretecuringimage = ConcreteCuringImagesASerializer(read_only=True)
    concretecuringperiodimage = ConcreteCuringImagesASerializer(read_only =True)

    excavationimage = ExcavationImagesASerializer(read_only=True)
    bs241concretepourcuringperiodimage = ConcreteCuringPeriodImagesASerializer(read_only =True)
   # concretepourcuringieriodimage = ConcreteCuringPeriodImagesSerializer(read_only=True)

    foundfootpourimage = FoundFootPourImagesASerializer(read_only=True)
    blockworkpanelconstimage = BlockworkPanelConstImagesASerializer(read_only=True)
    gateinstallationimage = GateInstallationImagesASerializer(read_only=True)
    razorelectricfenceimage = RazorElectricFenceImagesASerializer(read_only=True)

    towererectionimage = TowerErectionImagesASerializer(read_only=True)
    towerpaintimage = TowerPaintImagesASerializer(read_only=True)
    cablewaysimage = CableWaysImagesASerializer(read_only=True)
    antennacoaxinstallimage = AntennaCoaxInstallImagesASerializer(read_only=True)

    undergroundtasks = UndergroundTasksFilesASerializer(read_only=True)
    reticulationapsinstallation = ReticulationAPSinstallationFilesASerializer(read_only=True)
    electricalearthing = ElectricalEarthingImagesASerializer(read_only =True)
    generatorinstallation = GeneratorInstallationImagesASerializer(read_only=True)
    kplcsolarimage = KPLCSolarImagesASerializer(read_only=True)

    btsinstallationtask = BTSinstallationTaskImagesSerializer(read_only=True)
    mwinstallationtask = MWInstallationTaskImagesSerializer(read_only=True)
    installationteam = InstallationTeamFilesSerializer(read_only =True)



    class Meta:
        model = BtsSite
       # fields = ('__all__')
        exclude = ("id","site_name","site_number","BTS_type","site_owner","final_acceptance_cert_comment","created_at",
           "updated_at", "is_active","icon", "location", "created_by")



################### Main Project Serializer################################

class SiteFilesCSerializer(serializers.ModelSerializer):

    projectpurchaseorders = ProjectPurchaseOrdersFileSerializer(read_only=True)
    projectcosting = ProjectCostingFileSerializer(read_only=True)
    commercialteam = CommercialTeamFilesSerializer(read_only=True)
    procurementteam = ProcurementTeamFilesSerializer(read_only=True)

    accessapprovalcivil = AccessApprovalFileCivilSerializer(read_only=True)

    class Meta:
        model = BtsSite
       # fields = ('__all__')
        exclude = ("id","site_name","site_number","BTS_type","site_owner","final_acceptance_cert_comment","created_at",
           "updated_at", "is_active","icon", "location", "created_by")

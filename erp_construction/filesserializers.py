from rest_framework import serializers  #, exceptions
from .models import *



############################ PROJECT FILES SERIALIZERS ###############################################


class SiteClearingFilesSerializer(serializers.ModelSerializer):

    class Meta:
        model = SetSiteClearingImage
        fields = ('setting_site_clearing_image_1','setting_site_clearing_image_2','setting_site_clearing_image_3',)
       # read_only_fields = ('created_at', 'updated_at', 'is_active')

class TowerBaseImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = TowerBaseImage
        fields = ('towerbase_image_1','towerbase_image_1','towerbase_image_1',)
       # read_only_fields = ('created_at', 'updated_at', 'is_active')

class BindingImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = BindingImage
        fields = ('binding_image_1','binding_image_2','binding_image_3',)
       # read_only_fields = ('created_at', 'updated_at', 'is_active')

class SteelFixFormworkImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = SteelFixFormworkImage
        fields = ('steel_fix_formwork_image_1','steel_fix_formwork_image_2','steel_fix_formwork_image_3',)
        #read_only_fields = ('created_at', 'updated_at', 'is_active')
class ConcretePourCuringImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = ConcretePourCuringImage
        fields = ('concrete_pour_curing_image_1','concrete_pour_curing_image_2','concrete_pour_curing_image_3',)
       # read_only_fields = ('created_at', 'updated_at', 'is_active')

#GENERATOR FOUNDATION
class ExcavationImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = ExcavationImage
        fields = ('excavation_image_1','excavation_image_2','excavation_image_3',)
        #read_only_fields = ('created_at', 'updated_at', 'is_active')

#GENERATOR FOUNDATION
class ExcavationImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = ExcavationImage
        fields = ('excavation_image_1','excavation_image_2','excavation_image_3',)
        #read_only_fields = ('created_at', 'updated_at', 'is_active')

class ConcretePourCuringPeriodImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = ConcretePourCuringPeriodImage
        fields = ('concrete_pour_curing_image_1','concrete_pour_curing_image_2','concrete_pour_curing_image_1',)
       # read_only_fields = ('created_at', 'updated_at', 'is_active')


#  BOUNDARY WALL 

class FoundFootPourImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = FoundFootPourImage
        fields = ('foundfootpour_image_1','foundfootpour_image_2','foundfootpour_image_3',)
      #  read_only_fields = ('created_at', 'updated_at', 'is_active')

class BlockworkPanelConstImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = BlockworkPanelConstImage
        fields = ('blockwallpanelconst_image_1','blockwallpanelconst_image_2','blockwallpanelconst_image_3',)
       # read_only_fields = ('created_at', 'updated_at', 'is_active')

class GateInstallationImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = GateInstallationImage
        fields = ('gateinstallation_image_1','gateinstallation_image_2','gateinstallation_image_3',)
        #read_only_fields = ('created_at', 'updated_at', 'is_active')

class RazorElectricFenceImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = RazorElectricFenceImage
        fields = ('razorelectricfance_image_1','razorelectricfance_image_2','razorelectricfance_image_3')
       # read_only_fields = ('created_at', 'updated_at', 'is_active')


#TOWER & ANTENNA_COAXs 

class TowerErectionImagesSerializer(serializers.ModelSerializer):

    class Meta:   
        model = TowerErectionImage
        fields = ('tower_erection_image_1','tower_erection_image_2','tower_erection_image_3',)
        #read_only_fields = ('created_at', 'updated_at', 'is_active')

class TowerPaintImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = TowerPaintImage
        fields = ('tower_painting_image_1','tower_painting_image_2','tower_painting_image_3',)
       # read_only_fields = ('created_at', 'updated_at', 'is_active')

class CableWaysImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = CableWaysImage
        fields = ('cable_ways_image_1','cable_ways_image_2','cable_ways_image_3',)
        #read_only_fields = ('created_at', 'updated_at', 'is_active')

class AntennaCoaxInstallImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = AntennaCoaxInstallImage
        fields = ('antenna_coax_installation_image_1','antenna_coax_installation_image_2','antenna_coax_installation_image_3',)
       # read_only_fields = ('created_at', 'updated_at', 'is_active')
class TowerAntennaCoaxImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = TowerAntennaCoaxImage
        fields = ('antenna_coax_installation_image_1','antenna_coax_installation_image_2','antenna_coax_installation_image_3',)
        #read_only_fields = ('created_at', 'updated_at', 'is_active')
#END

class ProjectPurchaseOrdersFileSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProjectPurchaseOrders
        fields = ('po_file',)
       # read_only_fields = ('created_at', 'updated_at', 'is_active')


class ProjectCostingFileSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProjectCosting
        fields = ('project_costing_file',)
       # read_only_fields = ('created_at', 'updated_at', 'is_active')


class CommercialTeamFilesSerializer(serializers.ModelSerializer):

    class Meta:
        model = CommercialTeam
        fields = ('approved_quote_file','initial_invoice',)
       # read_only_fields = ('created_at', 'updated_at', 'is_active')

class ProcurementTeamFilesSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProcurementTeam
        fields = ('po_steel','po_subcontractors',)
       # read_only_fields = ('created_at', 'updated_at', 'is_active')



class HealthDocumentsFilesCivilTeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = HealthDocumentsCivilTeam
        fields = ('job_hazard_form','incident_notification_form','toolbox_meeting_form','communication_plan_form',)
       # read_only_fields = ('created_at', 'updated_at', 'is_active')

class AccessApprovalFileCivilSerializer(serializers.ModelSerializer):

    class Meta:
        model = AccessApprovalCivil
        fields = ('access_approval',)
       # read_only_fields = ('created_at', 'updated_at', 'is_active')


class UndergroundTasksFilesSerializer(serializers.ModelSerializer):

    class Meta:
        model = UndergroundTasks
        fields = ('Underground_ducting_and_manholes_image_1','Underground_ducting_and_manholes_image_2','Underground_ducting_and_manholes_image_3',)
        #read_only_fields = ('created_at', 'updated_at', 'is_active')



class ReticulationAPSinstallationFilesSerializer(serializers.ModelSerializer):

    class Meta:
        model = ReticulationAPSinstallation
        fields = ('Electricalreticulation_APSInstallation_image_1','Electricalreticulation_APSInstallation_image_2','Electricalreticulation_APSInstallation_image_3')
       # read_only_fields = ('created_at', 'updated_at', 'is_active')


class ElectricalEarthingImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = ElectricalEarthing
        fields = ('Earthing_connections_and_testing_image_1','Earthing_connections_and_testing_image_2','Earthing_connections_and_testing_image_3',)
        #read_only_fields = ('created_at', 'updated_at', 'is_active')


class GeneratorInstallationImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = GeneratorInstallation
        fields = ('Generator_and_Fuel_Tank_Installation_image_1','Generator_and_Fuel_Tank_Installation_image_2','Generator_and_Fuel_Tank_Installation_image_3','before_fuel_image_1','before_fuel_image_2','after_fuel_image_1','after_fuel_image_2')
       # read_only_fields = ('created_at', 'updated_at', 'is_active')

class KPLCSolarImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = KPLCSolarImage
        fields = ('kplc_solar_installation_image_1','kplc_solar_installation_image_2','kplc_solar_installation_image_3',)
      #  read_only_fields = ('created_at', 'updated_at', 'is_active')

class BTSinstallationTaskImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = BTSinstallationTask
        fields = ('BTSinstallation_image_1','BTSinstallation_image_2','BTSinstallation_image_3',)
      #  read_only_fields = ('created_at', 'updated_at', 'is_active')



class MWInstallationTaskImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = MWInstallationTask
        fields = ('MWinstallation_image_1','MWinstallation_image_2','MWinstallation_image_3',)
       # read_only_fields = ('created_at', 'updated_at', 'is_active')

class InstallationTeamFilesSerializer(serializers.ModelSerializer):

    class Meta:
        model = InstallationTeam
        fields = ('as_built','signoff','rfi_document','snag_document','conditional_acceptance_cert',)
       # read_only_fields = ('created_at', 'updated_at', 'is_active')

################### Main Project Serializer################################

class ProjectFilesSerializer(serializers.ModelSerializer):
    ''' Main Serializer class : to access all serializers classes above to get all images  and files per project '''

    setsiteclearingimage = SiteClearingFilesSerializer ( read_only =True)
    towerbaseimage = TowerBaseImagesSerializer(read_only=True)
    bindingimage = BindingImagesSerializer(read_only=True)

    steelfixformworkimage =SteelFixFormworkImagesSerializer(read_only=True)
    concretepourcuringimage = ConcretePourCuringImagesSerializer(read_only=True)
    excavationimage =ExcavationImagesSerializer(read_only=True)

    concretepourcuringieriodimage =ConcretePourCuringPeriodImagesSerializer(read_only=True)
    foundfootpourimage= FoundFootPourImagesSerializer(read_only=True)
    blockworkpanelconstimage= BlockworkPanelConstImagesSerializer(read_only=True)

    gateinstallationimage= GateInstallationImagesSerializer(read_only=True)
    razorelectricfenceimage =RazorElectricFenceImagesSerializer(read_only=True)
    towererectionimage =TowerErectionImagesSerializer(read_only=True)
    towerpaintimage = TowerPaintImagesSerializer(read_only=True)

    cablewaysimage= CableWaysImagesSerializer(read_only=True)
    antennacoaxinstallimage =AntennaCoaxInstallImagesSerializer(read_only=True)
    towerantennacoaximage = TowerAntennaCoaxImageSerializer(read_only=True)
    projectpurchaseorders =ProjectPurchaseOrdersFileSerializer(read_only=True)

    healthdocumentscivilteam =HealthDocumentsFilesCivilTeamSerializer(many = True,read_only =True)
    accessapprovalcivil=AccessApprovalFileCivilSerializer(many = True,read_only=True)

    undergroundtasks= UndergroundTasksFilesSerializer(read_only=True)
    reticulationapsinstallation = ReticulationAPSinstallationFilesSerializer(read_only=True)
    electricalearthing = ElectricalEarthingImagesSerializer(read_only =True)
    generatorinstallation = GeneratorInstallationImagesSerializer(read_only=True)

    kplcsolarimage = KPLCSolarImagesSerializer(read_only=True)
    btsinstallationtask = BTSinstallationTaskImagesSerializer(read_only=True)
    mwinstallationtask = MWInstallationTaskImagesSerializer(read_only=True)
    installationteam = InstallationTeamFilesSerializer(read_only =True)


    class Meta:
        model = Project
       # fields = ('__all__')
        exclude = ("id","project_name","site_number","BTS_type","site_owner","geotech_file","access_letter",
           "approved_drawing","final_acceptance_cert","final_acceptance_cert_comment","created_at",
           "updated_at", "is_active","icon", "location", "created_by")

        #fields = ('geotech_file','access_letter','approved_drawing','final_acceptance_cert','setsiteclearingimage',
        #'towerbaseimage','bindingimage','steelfixformworkimage','concretepourcuringimage')
        #read_only_fields = ('created_at', 'updated_at', 'is_active')

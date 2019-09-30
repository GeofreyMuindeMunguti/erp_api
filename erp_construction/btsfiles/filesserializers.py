"""Extract files and images per project.
"""
#---------
# Imports
#---------
from rest_framework import serializers  #, exceptions
from erp_construction.models import *


############################ PROJECT FILES SERIALIZERS ###############################################


class SiteClearingFilesSerializer(serializers.ModelSerializer):

    class Meta:
        model = SetSiteClearingImage
        fields = ('setting_site_clearing_image_1','setting_site_clearing_image_2','setting_site_clearing_image_3',)


class TowerBaseImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = TowerBaseImage
        fields = ('towerbase_image_1', 'towerbase_image_2', 'towerbase_image_3',)


class BindingImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = BindingImage
        fields = ('binding_image_1','binding_image_2','binding_image_3',)


class SteelFixFormworkImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = SteelFixFormworkImage
        fields = ('steel_fix_formwork_image_1','steel_fix_formwork_image_2','steel_fix_formwork_image_3',)


class ConcretePourImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = ConcretePourImage
        fields = ('concrete_pour_curing_image_1','concrete_pour_curing_image_2','concrete_pour_curing_image_3',)


class ConcreteCuringImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = ConcreteCuringPeriodImage
        fields = ('concrete_pour_curing_period_image_1','concrete_pour_curing_period_image_2','concrete_pour_curing_period_image_3',)


#GENERATOR FOUNDATION


class ExcavationImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = ExcavationImage
        fields = ('excavation_image_1','excavation_image_2','excavation_image_3',)


class ConcreteCuringPeriodImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = BS241ConcretePourCuringPeriodImage
        fields = ('bs241_concrete_pour_curing_period_image_1','bs241_concrete_pour_curing_period_image_2','bs241_concrete_pour_curing_period_image_3',)


#  BOUNDARY WALL

class FoundFootPourImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = FoundFootPourImage
        fields = ('foundfootpour_image_1','foundfootpour_image_2','foundfootpour_image_3',)

class BWCableConduitsImageSerializer(serializers.ModelSerializer):
     class Meta:
        model = BWCableConduitsImage
        fields = ('bw_cable_conduits_image_1','bw_cable_conduits_image_2','bw_cable_conduits_image_3',)

class BWBlindingImageSerializer(serializers.ModelSerializer):
     class Meta:
        model = BWBlindingImage
        fields = ('bw_blinding_image_1','bw_blinding_image_2','bw_blinding_image_3',)

class ExcavationstripFoundationsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExcavationstripFoundationsImage
        fields = ('excavationstrip_foundations_image_1','excavationstrip_foundations_image_2','excavationstrip_foundations_image_3',)

class BWConcretePourCuringPeriodImageSerializer(serializers.ModelSerializer):
      class Meta:
        model = BWConcretePourCuringPeriodImage
        fields = ('bw_concrete_pour_curing_period_image_1','bw_concrete_pour_curing_period_image_2','bw_concrete_pour_curing_period_image_3',)


class BlockworkPanelConstImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = BlockworkPanelConstImage
        fields = ('blockwallpanelconst_image_1','blockwallpanelconst_image_2','blockwallpanelconst_image_3',)


class GateInstallationImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = GateInstallationImage
        fields = ('gateinstallation_image_1','gateinstallation_image_2','gateinstallation_image_3',)


class RazorElectricFenceImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = RazorElectricFenceImage
        fields = ('razorelectricfance_image_1','razorelectricfance_image_2','razorelectricfance_image_3')


#TOWER & ANTENNA_COAXs

class TowerErectionImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = TowerErectionImage
        fields = ('tower_erection_image_1','tower_erection_image_2','tower_erection_image_3',)


class TowerPaintImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = TowerPaintImage
        fields = ('tower_painting_image_1','tower_painting_image_2','tower_painting_image_3',)

class TowerDeliveryImageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TowerDeliveryImage
        fields = ('tower_delivery_image_1','tower_delivery_image_2','tower_delivery_image_3',)


class CableInstallationImageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CableInstallationImage
        fields = ('cable_installation_image_1','cable_installation_image_2','cable_installation_image_3',)

class EarthInstallationImageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = EarthInstallationImage
        fields = ('earth_Installation_image_1','earth_Installation_image_2','earth_Installation_image_3',)

class AviationLightsInstallationImageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = AviationLightsInstallationImage
        fields = ('aviation_lights_installation_image_1','aviation_lights_installation_image_2','aviation_lights_installation_image_3',)





class CableWaysImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = CableWaysImage
        fields = ('cable_ways_image_1','cable_ways_image_2','cable_ways_image_3',)


class AntennaCoaxInstallImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = AntennaCoaxInstallImage
        fields = ('antenna_coax_installation_image_1','antenna_coax_installation_image_2','antenna_coax_installation_image_3',)

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


class HealthDocumentsFilesInstallationTeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = HealthDocumentsInstallationTeam
        fields = ('job_hazard_form', 'incident_notification_form', 'toolbox_meeting_form', 'communication_plan_form', 'safety_picture')
        read_only_fields = ('created_at', 'updated_at', 'is_active')


class AccessApprovalFileInstallationSerializer(serializers.ModelSerializer):

    class Meta:
        model = AccessApprovalInstallation
        fields = ('access_approval',)
        read_only_fields = ('created_at', 'updated_at', 'is_active')


class UndergroundTasksFilesSerializer(serializers.ModelSerializer):

    class Meta:
        model = UndergroundTasks
        fields = ('Underground_ducting_and_manholes_image_1','Underground_ducting_and_manholes_image_2','Underground_ducting_and_manholes_image_3',)


class ReticulationAPSinstallationFilesSerializer(serializers.ModelSerializer):

    class Meta:
        model = ReticulationAPSinstallation
        fields = ('Electricalreticulation_APSInstallation_image_1','Electricalreticulation_APSInstallation_image_2','Electricalreticulation_APSInstallation_image_3')


class ElectricalEarthingImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = ElectricalEarthing
        fields = ('Earthing_connections_and_testing_image_1','Earthing_connections_and_testing_image_2','Earthing_connections_and_testing_image_3',)


class GeneratorInstallationImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = GeneratorInstallation
        fields = ('Generator_and_Fuel_Tank_Installation_image_1','Generator_and_Fuel_Tank_Installation_image_2','Generator_and_Fuel_Tank_Installation_image_3','before_fuel_image_1','before_fuel_image_2','after_fuel_image_1','after_fuel_image_2')


class KPLCSolarImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = KPLCSolarImage
        fields = ('kplc_solar_installation_image_1','kplc_solar_installation_image_2','kplc_solar_installation_image_3',)


class BTSinstallationTaskImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = BTSinstallationTask
        fields = ('BTSinstallation_image_1','BTSinstallation_image_2','BTSinstallation_image_3',)


class MWInstallationTaskImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = MWInstallationTask
        fields = ('MWinstallation_image_1','MWinstallation_image_2','MWinstallation_image_3',)


class InstallationTeamFilesSerializer(serializers.ModelSerializer):

    class Meta:
        model = InstallationTeam
        fields = ('as_built', 'signoff', 'rfi_document', 'snag_document', 'conditional_acceptance_cert',)


class IssueImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Issues
        fields = ('issue_image', 'issue_sorted_image',)

class IRROF7FreeFilesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = IRROF7Free
        fields = ('tower_complete', 'free_issue_material', 'link_material',)


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

    setsiteclearingimage = SiteClearingFilesSerializer ( read_only =True)
    towerbaseimage = TowerBaseImagesSerializer(read_only=True)
    bindingimage = BindingImagesSerializer(read_only=True)
    steelfixformworkimage = SteelFixFormworkImagesSerializer(read_only=True)
    concretepourimage = ConcretePourImagesSerializer(read_only=True)
    concretecuringimage = ConcreteCuringImagesSerializer(read_only=True)

    excavationimage = ExcavationImagesSerializer(read_only=True)
    concretepourcuringieriodimage = ConcreteCuringPeriodImagesSerializer(read_only=True)

    foundfootpourimage = FoundFootPourImagesSerializer(read_only=True)

    bwcableconduitsimage=BWCableConduitsImageSerializer(read_only=True)
    bwblindingimage     =BWBlindingImageSerializer(read_only=True)
    excavationstripfoundationsimage=  ExcavationstripFoundationsImageSerializer(read_only=True)
    bwconcretepourcuringperiodimage = BWConcretePourCuringPeriodImageSerializer(read_only=True)
      

    blockworkpanelconstimage = BlockworkPanelConstImagesSerializer(read_only=True)
    gateinstallationimage = GateInstallationImagesSerializer(read_only=True)
    razorelectricfenceimage = RazorElectricFenceImagesSerializer(read_only=True)

    towererectionimage = TowerErectionImagesSerializer(read_only=True)
    towerpaintimage = TowerPaintImagesSerializer(read_only=True)


    cablewaysimage = CableWaysImagesSerializer(read_only=True)

    towerdeliveryimage = TowerDeliveryImageSerializer(read_only=True)
    cableinstallationimage = CableInstallationImageSerializer(read_only=True)
    earthinstallationimage = EarthInstallationImageSerializer(read_only=True)
    aviationlightsinstallationimage = AviationLightsInstallationImageSerializer(read_only=True)

 
    antennacoaxinstallimage = AntennaCoaxInstallImagesSerializer(read_only=True)

    projectpurchaseorders = ProjectPurchaseOrdersFileSerializer(read_only=True)
    projectcosting = ProjectCostingFileSerializer(read_only=True)
    commercialteam = CommercialTeamFilesSerializer(read_only=True)
    procurementteam = ProcurementTeamFilesSerializer(read_only=True)

    healthdocumentscivilteam = HealthDocumentsFilesCivilTeamSerializer(many = True,read_only =True)
    accessapprovalcivil = AccessApprovalFileCivilSerializer(many = True,read_only=True)
    healthdocumentsInstallationteam = HealthDocumentsFilesInstallationTeamSerializer(many = True,read_only =True)
    accessapprovalinstallation = AccessApprovalFileInstallationSerializer(many = True,read_only=True)

    undergroundtasks = UndergroundTasksFilesSerializer(read_only=True)
    reticulationapsinstallation = ReticulationAPSinstallationFilesSerializer(read_only=True)
    electricalearthing = ElectricalEarthingImagesSerializer(read_only =True)
    generatorinstallation = GeneratorInstallationImagesSerializer(read_only=True)
    kplcsolarimage = KPLCSolarImagesSerializer(read_only=True)

    btsinstallationtask = BTSinstallationTaskImagesSerializer(read_only=True)
    mwinstallationtask = MWInstallationTaskImagesSerializer(read_only=True)
    installationteam = InstallationTeamFilesSerializer(read_only =True)
    issueimages = IssueImageSerializer(read_only=True)
    irrof7Free = IRROF7FreeFilesSerializer(read_only=True)


    class Meta:
        model = BtsSite
       # fields = ('__all__')
        exclude = ("id","site_name","site_number","BTS_type","site_owner","final_acceptance_cert_comment",
           "icon", "location", "created_by")

        #fields = ('geotech_file','access_letter','approved_drawing','final_acceptance_cert','setsiteclearingimage',
        #'towerbaseimage','bindingimage','steelfixformworkimage','concretepourcuringimage')
        #read_only_fields = ('created_at', 'updated_at', 'is_active')

"""Extract files and images per project.
"""
#---------
# Imports
#---------
from rest_framework import serializers  #, exceptions
from erp_construction.models import *


############################ PROJECT FILES SERIALIZERS ###############################################

# Site Clearing  Files Serializers///////////////
class SiteClearingImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = SiteClearingImage
        fields = ('setting_site_clearing_image','setting_site_clearing_comment')


class SiteClearingDateFilesSerializer(serializers.ModelSerializer):
    siteclearingimage = SiteClearingImagesSerializer(read_only=True)

    class Meta:
        model = SiteClearingDate
        fields = ('work_day','casuals_list','siteclearingimage',)

class SiteClearingSubTaskFilesSerializer(serializers.ModelSerializer):
    siteclearingdates =SiteClearingDateFilesSerializer(many = True,read_only =True)

    class Meta:
        model = SiteClearingSubtask
        fields = ('id','project_name_id','setting_site_clearing_image_1','setting_site_clearing_image_2','setting_site_clearing_image_3','setting_site_clearing_comment','siteclearingdates',)

class SiteClearingSubTaskAFilesSerializer(serializers.ModelSerializer):
    siteclearingsubtask = SiteClearingSubTaskFilesSerializer(read_only =True)

    class Meta:
        model = BtsSite
        exclude = ("project_name","site_name","site_number","BTS_type","site_owner","final_acceptance_cert_comment","created_at",
           "updated_at", "is_active", "location", "created_by",'geotech_file','access_letter','approved_drawing','final_acceptance_cert')
# TowerBaseSubTask  Files Serializers///////////////

class TowerBaseImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = TowerBaseImage
        fields = ('towerbase_image','tower_base_comment')


class TowerBaseDateFilesSerializer(serializers.ModelSerializer):
    towerbaseimages = TowerBaseImagesSerializer(read_only=True)

    class Meta:
        model = TowerBaseDate
        fields = ('work_day','casuals_list','towerbaseimages',)

class TowerBaseSubTaskFilesSerializer(serializers.ModelSerializer):
    towerbasedates =TowerBaseDateFilesSerializer(many = True,read_only =True)

    class Meta:
        model = TowerBaseSubtask
        fields = ('towerbase_image_1', 'towerbase_image_2', 'towerbase_image_3', 'tower_base_comment','towerbasedates',)

class TowerBaseSubTaskAFilesSerializer(serializers.ModelSerializer):
    towerbasesubtask = TowerBaseSubTaskFilesSerializer(read_only =True)

    class Meta:
        model = BtsSite
        exclude = ("id","project_name","site_name","site_number","BTS_type","site_owner","final_acceptance_cert_comment","created_at",
           "updated_at", "is_active", "location", "created_by",'geotech_file','access_letter','approved_drawing','final_acceptance_cert')

# BlindingSubTask  Files Serializers///////////////

class BlindingImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = BlindingImage
        fields = ('blinding_image','blinding_image_comment',)


class BlindingDateFilesSerializer(serializers.ModelSerializer):
    blindingimages = BlindingImagesSerializer(read_only=True)

    class Meta:
        model = BlindingDate
        fields = ('work_day','casuals_list','blindingimages',)

class BlindingSubTaskFilesSerializer(serializers.ModelSerializer):
    blindingdates =BlindingDateFilesSerializer(many = True,read_only =True)

    class Meta:
        model = BlindingSubtask
        fields = ('blinding_image_1', 'blinding_image_2', 'blinding_image_3', 'blinding_comment','blindingdates',)

class BlindingSubTaskAFilesSerializer(serializers.ModelSerializer):
    blindingsubtask = BlindingSubTaskFilesSerializer(read_only =True)

    class Meta:
        model = BtsSite
        exclude = ("id","project_name","site_name","site_number","BTS_type","site_owner","final_acceptance_cert_comment","created_at",
           "updated_at", "is_active", "location", "created_by",'geotech_file','access_letter','approved_drawing','final_acceptance_cert')
           
 #CON          
# SteelFixFormwork  Files Serializers///////////////
class SteelFixFormworkImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = SteelFixFormworkImage
        fields = ('steel_fixformwork_image','steel_fixformwork_comment')


class SteelFixFormworkDateFilesSerializer(serializers.ModelSerializer):
    steelfixformworkimages = SteelFixFormworkImagesSerializer(read_only=True)

    class Meta:
        model = SteelFixFormworkDate
        fields = ('work_day','casuals_list','steelfixformworkimages',)

class SteelFixFormworkSubTaskFilesSerializer(serializers.ModelSerializer):
    steelfixformworkdates =SteelFixFormworkDateFilesSerializer(many = True,read_only =True)

    class Meta:
        model = SteelFixFormworkSubtask
        fields = ('steel_fix_formwork_image_1', 'steel_fix_formwork_image_2', 'steel_fix_formwork_image_3', 'steel_fix_formwork_comment','steelfixformworkdates',)

class SteelFixFormworkSubTaskAFilesSerializer(serializers.ModelSerializer):
    steelfixformworksubtask = SteelFixFormworkSubTaskFilesSerializer(read_only =True)

    class Meta:
        model = BtsSite
        exclude = ("id","project_name","site_name","site_number","BTS_type","site_owner","final_acceptance_cert_comment","created_at",
           "updated_at", "is_active", "location", "created_by",'geotech_file','access_letter','approved_drawing','final_acceptance_cert')
           
        
# ConcretePour Files Serializers///////////////

class ConcretePourImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = ConcretePourImage
        fields = ('concrete_pour_curing_image','concrete_pour_curing_comment',)


class ConcretePourDateFilesSerializer(serializers.ModelSerializer):
    concretepourimages = ConcretePourImagesSerializer(read_only=True)

    class Meta:
        model = ConcretePourDate
        fields = ('work_day','casuals_list','concretepourimages',)

class ConcretePourSubTaskFilesSerializer(serializers.ModelSerializer):
    concretepourdates = ConcretePourDateFilesSerializer(many = True,read_only =True)

    class Meta:
        model = ConcretePourSubtask
        fields = ('concrete_pour_curing_image_1', 'concrete_pour_curing_image_2', 'concrete_pour_curing_image_3', 'concrete_pour_curing_comment','concretepourdates',)

class ConcretePourSubTaskAFilesSerializer(serializers.ModelSerializer):
    concretepoursubtask = ConcretePourSubTaskFilesSerializer(read_only =True)

    class Meta:
        model = BtsSite
        exclude = ("id","project_name","site_name","site_number","BTS_type","site_owner","final_acceptance_cert_comment","created_at",
           "updated_at", "is_active", "location", "created_by",'geotech_file','access_letter','approved_drawing','final_acceptance_cert')
           
           
# SteelFixFormwork  Files Serializers///////////////

class ConcreteCuringImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = ConcreteCuringPeriodImage
        fields = ('concrete_curing_period_image','concrete_curing_period_comment',)



class ConcreteCuringPeriodDateFilesSerializer(serializers.ModelSerializer):
    concretecuringperiodimages = ConcreteCuringImagesSerializer(read_only=True)

    class Meta:
        model = ConcreteCuringPeriodDate
        fields = ('work_day','casuals_list','concretecuringperiodimages',)

class ConcreteCuringPeriodSubTaskFilesSerializer(serializers.ModelSerializer):
    concretecuringperioddates = ConcreteCuringPeriodDateFilesSerializer(many = True,read_only =True)

    class Meta:
        model = ConcreteCuringPeriodSubtask
        fields = ('concrete_pour_curing_period_image_1', 'concrete_pour_curing_period_image_2', 'concrete_pour_curing_period_image_3', 'concrete_pour_curing_period_comment','concretecuringperioddates',)

class ConcreteCuringPeriodSubTaskAFilesSerializer(serializers.ModelSerializer):
    concretecuringperiodsubtask = ConcreteCuringPeriodSubTaskFilesSerializer(read_only =True)

    class Meta:
        model = BtsSite
        exclude = ("id","project_name","site_name","site_number","BTS_type","site_owner","final_acceptance_cert_comment","created_at",
           "updated_at", "is_active", "location", "created_by",'geotech_file','access_letter','approved_drawing','final_acceptance_cert')

# #GENERATOR FOUNDATION

#SteelFixFormwork  Files Serializers///////////////

class ExcavationImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = ExcavationImage
        fields = ('excavation_image','excavation_image_comment',)



class ExcavationDateFilesSerializer(serializers.ModelSerializer):
    excavationimages = ExcavationImagesSerializer(read_only=True)

    class Meta:
        model = ExcavationDate
        fields = ('work_day','casuals_list','excavationimages',)

class ExcavationSubTaskFilesSerializer(serializers.ModelSerializer):
    excavationdates = ExcavationDateFilesSerializer(many = True,read_only =True)

    class Meta:
        model = ExcavationSubtask
        fields = ('excavation_image_1', 'excavation_image_2', 'excavation_image_3','excavationdates',)

class ExcavationSubTaskAFilesSerializer(serializers.ModelSerializer):
    excavationsubtask = ExcavationSubTaskFilesSerializer(read_only =True)

    class Meta:
        model = BtsSite
        exclude = ("id","project_name","site_name","site_number","BTS_type","site_owner","final_acceptance_cert_comment","created_at",
           "updated_at", "is_active", "location", "created_by",'geotech_file','access_letter','approved_drawing','final_acceptance_cert')

#BS21ConcreteCuringPeriodI  Files Serializers///////////////


class BS241ConcretePourCuringPeriodImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = BS241ConcretePourCuringPeriodImage
        fields = ('bs241_concrete_pour_curing_period_image','bs241_concrete_pour_curing_period_comment',)



class BS241ConcretePourCuringPeriodDateFilesSerializer(serializers.ModelSerializer):
    bs241Concretepourcuringperiodimages = BS241ConcretePourCuringPeriodImagesSerializer(read_only=True)

    class Meta:
        model = BS241ConcretePourCuringPeriodDate
        fields = ('work_day','casuals_list','bs241Concretepourcuringperiodimages',)

class BS241ConcretePourCuringPeriodSubTaskFilesSerializer(serializers.ModelSerializer):
    bs241Concretepourcuringperioddates = BS241ConcretePourCuringPeriodDateFilesSerializer(many = True,read_only =True)

    class Meta:
        model = BS241ConcretePourCuringPeriodSubtask
        fields = ('bs241_concrete_pour_curing_period_image_1', 'bs241_concrete_pour_curing_period_image_2','bs241_concrete_pour_curing_period_image_3', 'bs241_concrete_pour_curing_period_comment','bs241Concretepourcuringperioddates',)

class BS241ConcretePourCuringPeriodSubTaskAFilesSerializer(serializers.ModelSerializer):
    bs241concretepourcuringperiodsubtask = BS241ConcretePourCuringPeriodSubTaskFilesSerializer(read_only =True)

    class Meta:
        model = BtsSite
        exclude = ("id","project_name","site_name","site_number","BTS_type","site_owner","final_acceptance_cert_comment","created_at",
           "updated_at", "is_active", "location", "created_by",'geotech_file','access_letter','approved_drawing','final_acceptance_cert')
# #  BOUNDARY WALL

#FoundFootPour  Files Serializers///////////////
class FoundFootPourImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = FoundFootPourImage
        fields = ('foundfootpour_image','foundfootpour_comment',)



class FoundFootPourDateFilesSerializer(serializers.ModelSerializer):
    foundfootpourimages = FoundFootPourImagesSerializer(read_only=True)

    class Meta:
        model = FoundFootPourDate
        fields = ('work_day','casuals_list','foundfootpourimages',)

class FoundFootPourSubTaskFilesSerializer(serializers.ModelSerializer):
    foundfootpourdates = FoundFootPourDateFilesSerializer(many = True,read_only =True)

    class Meta:
        model = FoundFootPourSubtask
        fields = ('foundfootpour_image_1', 'foundfootpour_image_2','foundfootpour_image_3', 'foundfootpour_comment','foundfootpourdates',)

class FoundFootPourSubTaskAFilesSerializer(serializers.ModelSerializer):
    foundfootpoursubtask = FoundFootPourSubTaskFilesSerializer(read_only =True)

    class Meta:
        model = BtsSite
        exclude = ("id","project_name","site_name","site_number","BTS_type","site_owner","final_acceptance_cert_comment","created_at",
           "updated_at", "is_active", "location", "created_by",'geotech_file','access_letter','approved_drawing','final_acceptance_cert')

# class BlockworkPanelConst  Files Serializers///////////////

class BlockworkPanelConstImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = BlockworkPanelConstImage
        fields = ('blockwallpanelconst_image','blockwallpanelconst_comment',)


class BlockworkPanelConstDateFilesSerializer(serializers.ModelSerializer):
    blockworkpanelconstimages = BlockworkPanelConstImagesSerializer(read_only=True)

    class Meta:
        model = BlockworkPanelConstDate
        fields = ('work_day','casuals_list','blockworkpanelconstimages',)

class BlockworkPanelConstSubTaskFilesSerializer(serializers.ModelSerializer):
    blockworkpanelconstdates = BlockworkPanelConstDateFilesSerializer(many = True,read_only =True)

    class Meta:
        model = BlockworkPanelConstSubtask
        fields = ('blockwallpanelconst_image_1', 'blockwallpanelconst_image_2', 'blockwallpanelconst_image_3', 'blockwallpanelconst_comment','blockworkpanelconstdates',)

class BlockworkPanelConstSubTaskAFilesSerializer(serializers.ModelSerializer):
    blockworkpanelconstsubtask = BlockworkPanelConstSubTaskFilesSerializer(read_only =True)

    class Meta:
        model = BtsSite
        exclude = ("id","project_name","site_name","site_number","BTS_type","site_owner","final_acceptance_cert_comment","created_at",
           "updated_at", "is_active", "location", "created_by",'geotech_file','access_letter','approved_drawing','final_acceptance_cert')


# class GateInstallation  Files Serializers///////////////
class GateInstallationImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = GateInstallationImage
        fields = ('gateinstallation_image','gateinstallation_comment',)

class GateInstallationDateFilesSerializer(serializers.ModelSerializer):
    gateinstallationimages = GateInstallationImagesSerializer(read_only=True)

    class Meta:
        model = GateInstallationDate
        fields = ('work_day','casuals_list','gateinstallationimages',)

class GateInstallationSubTaskFilesSerializer(serializers.ModelSerializer):
    gateinstallationdates = GateInstallationDateFilesSerializer(many = True,read_only =True)

    class Meta:
        model = GateInstallationSubtask
        fields = ('gateinstallation_image_1', 'gateinstallation_image_2', 'gateinstallation_image_3','gateinstallation_comment','gateinstallationdates',)

class GateInstallationSubTaskAFilesSerializer(serializers.ModelSerializer):
    gateinstallationsubtask = GateInstallationSubTaskFilesSerializer(read_only =True)

    class Meta:
        model = BtsSite
        exclude = ("id","project_name","site_name","site_number","BTS_type","site_owner","final_acceptance_cert_comment","created_at",
           "updated_at", "is_active", "location", "created_by",'geotech_file','access_letter','approved_drawing','final_acceptance_cert')



# class RazorElectricFenceImagesSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = RazorElectricFenceImage
#         fields = ('razorelectricfance_image_1','razorelectricfance_image_2','razorelectricfance_image_3')

# class GateInstallation  Files Serializers///////////////
class GateInstallationImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = GateInstallationImage
        fields = ('gateinstallation_image','gateinstallation_comment',)

class GateInstallationDateFilesSerializer(serializers.ModelSerializer):
    gateinstallationimages = GateInstallationImagesSerializer(read_only=True)

    class Meta:
        model = GateInstallationDate
        fields = ('work_day','casuals_list','gateinstallationimages',)

class GateInstallationSubTaskFilesSerializer(serializers.ModelSerializer):
    gateinstallationdates = GateInstallationDateFilesSerializer(many = True,read_only =True)

    class Meta:
        model = GateInstallationSubtask
        fields = ('gateinstallation_image_1', 'gateinstallation_image_2', 'gateinstallation_image_3','gateinstallation_comment','gateinstallationdates',)

class GateInstallationSubTaskAFilesSerializer(serializers.ModelSerializer):
    gateinstallationsubtask = GateInstallationSubTaskFilesSerializer(read_only =True)

    class Meta:
        model = BtsSite
        exclude = ("id","project_name","site_name","site_number","BTS_type","site_owner","final_acceptance_cert_comment","created_at",
           "updated_at", "is_active", "location", "created_by",'geotech_file','access_letter','approved_drawing','final_acceptance_cert')


# #TOWER & ANTENNA_COAXs

# class TowerErectionImagesSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = TowerErectionImage
#         fields = ('tower_erection_image_1','tower_erection_image_2','tower_erection_image_3',)

# class GateInstallation  Files Serializers///////////////
class GateInstallationImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = GateInstallationImage
        fields = ('gateinstallation_image','gateinstallation_comment',)

class GateInstallationDateFilesSerializer(serializers.ModelSerializer):
    gateinstallationimages = GateInstallationImagesSerializer(read_only=True)

    class Meta:
        model = GateInstallationDate
        fields = ('work_day','casuals_list','gateinstallationimages',)

class GateInstallationSubTaskFilesSerializer(serializers.ModelSerializer):
    gateinstallationdates = GateInstallationDateFilesSerializer(many = True,read_only =True)

    class Meta:
        model = GateInstallationSubtask
        fields = ('gateinstallation_image_1', 'gateinstallation_image_2', 'gateinstallation_image_3','gateinstallation_comment','gateinstallationdates',)

class GateInstallationSubTaskAFilesSerializer(serializers.ModelSerializer):
    gateinstallationsubtask = GateInstallationSubTaskFilesSerializer(read_only =True)

    class Meta:
        model = BtsSite
        exclude = ("id","project_name","site_name","site_number","BTS_type","site_owner","final_acceptance_cert_comment","created_at",
           "updated_at", "is_active", "location", "created_by",'geotech_file','access_letter','approved_drawing','final_acceptance_cert')


# class TowerPaintImagesSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = TowerPaintImage
#         fields = ('tower_painting_image_1','tower_painting_image_2','tower_painting_image_3',)

# class GateInstallation  Files Serializers///////////////
class GateInstallationImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = GateInstallationImage
        fields = ('gateinstallation_image','gateinstallation_comment',)

class GateInstallationDateFilesSerializer(serializers.ModelSerializer):
    gateinstallationimages = GateInstallationImagesSerializer(read_only=True)

    class Meta:
        model = GateInstallationDate
        fields = ('work_day','casuals_list','gateinstallationimages',)

class GateInstallationSubTaskFilesSerializer(serializers.ModelSerializer):
    gateinstallationdates = GateInstallationDateFilesSerializer(many = True,read_only =True)

    class Meta:
        model = GateInstallationSubtask
        fields = ('gateinstallation_image_1', 'gateinstallation_image_2', 'gateinstallation_image_3','gateinstallation_comment','gateinstallationdates',)

class GateInstallationSubTaskAFilesSerializer(serializers.ModelSerializer):
    gateinstallationsubtask = GateInstallationSubTaskFilesSerializer(read_only =True)

    class Meta:
        model = BtsSite
        exclude = ("id","project_name","site_name","site_number","BTS_type","site_owner","final_acceptance_cert_comment","created_at",
           "updated_at", "is_active", "location", "created_by",'geotech_file','access_letter','approved_drawing','final_acceptance_cert')

# class CableWays  Files Serializers///////////////

class CableWaysImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = CableWaysImage
        fields = ('cable_ways_image_1','cable_ways_image_2','cable_ways_image_3',)


class CableWaysDateFilesSerializer(serializers.ModelSerializer):
    cablewaysimages = CableWaysImagesSerializer(read_only=True)

    class Meta:
        model = CableWaysDate
        fields = ('work_day','casuals_list','gateinstallationimages',)

class CableWaysSubTaskFilesSerializer(serializers.ModelSerializer):
    cablewaysdates = CableWaysDateFilesSerializer(many = True,read_only =True)

    class Meta:
        model = CableWaysSubtask
        fields = ('gateinstallation_image_1', 'gateinstallation_image_2', 'gateinstallation_image_3','gateinstallation_comment','gateinstallationdates',)

class CableWaysSubTaskAFilesSerializer(serializers.ModelSerializer):
    cablewayssubtask = CableWaysSubTaskFilesSerializer(read_only =True)

    class Meta:
        model = BtsSite
        exclude = ("id","project_name","site_name","site_number","BTS_type","site_owner","final_acceptance_cert_comment","created_at",
           "updated_at", "is_active", "location", "created_by",'geotech_file','access_letter','approved_drawing','final_acceptance_cert')

#  GateInstallation  Files Serializers///////////////
class AntennaCoaxInstallImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = AntennaCoaxInstallImage
        fields = ('antenna_coax_installation_image','antenna_coax_installation_comment',)


class AntennaCoaxInstallDateFilesSerializer(serializers.ModelSerializer):
    antennacoaxinstallimages = AntennaCoaxInstallImagesSerializer(read_only=True)

    class Meta:
        model = AntennaCoaxInstallDate
        fields = ('work_day','casuals_list','antennacoaxinstallimages',)

class AntennaCoaxInstallSubTaskFilesSerializer(serializers.ModelSerializer):
    antennacoaxinstalldates = AntennaCoaxInstallDateFilesSerializer(many = True,read_only =True)

    class Meta:
        model = AntennaCoaxInstallSubtask
        fields = ('antenna_coax_installation_image_1', 'antenna_coax_installation_image_2', 'antenna_coax_installation_image_3','antenna_coax_installation_comment','antennacoaxinstalldates',)

class AntennaCoaxInstallSubTaskAFilesSerializer(serializers.ModelSerializer):
    antennacoaxinstallsubtask = AntennaCoaxInstallSubTaskFilesSerializer(read_only =True)

    class Meta:
        model = BtsSite
        exclude = ("id","project_name","site_name","site_number","BTS_type","site_owner","final_acceptance_cert_comment","created_at",
           "updated_at", "is_active", "location", "created_by",'geotech_file','access_letter','approved_drawing','final_acceptance_cert')


# #END

# class ProjectPurchaseOrdersFileSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = ProjectPurchaseOrders
#         fields = ('po_file',)


# class ProjectCostingFileSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = ProjectCosting
#         fields = ('project_costing_file',)


# class CommercialTeamFilesSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = CommercialTeam
#         fields = ('approved_quote_file','initial_invoice',)


# class ProcurementTeamFilesSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = ProcurementTeam
#         fields = ('po_steel', 'po_subcontractors', 'po_electrical_materials')


# class HealthDocumentsFilesCivilTeamSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = HealthDocumentsCivilTeam
#         fields = ('job_hazard_form', 'incident_notification_form', 'toolbox_meeting_form', 'communication_plan_form', 'safety_picture')


# class AccessApprovalFileCivilSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = AccessApprovalCivil
#         fields = ('access_approval',)


# class HealthDocumentsFilesInstallationTeamSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = HealthDocumentsInstallationTeam
#         fields = ('job_hazard_form', 'incident_notification_form', 'toolbox_meeting_form', 'communication_plan_form', 'safety_picture')
#         read_only_fields = ('created_at', 'updated_at', 'is_active')


# class AccessApprovalFileInstallationSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = AccessApprovalInstallation
#         fields = ('access_approval',)
#         read_only_fields = ('created_at', 'updated_at', 'is_active')


# class UndergroundTasksFilesSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = UndergroundTasks
#         fields = ('Underground_ducting_and_manholes_image_1','Underground_ducting_and_manholes_image_2','Underground_ducting_and_manholes_image_3',)


# class ReticulationAPSinstallationFilesSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = ReticulationAPSinstallation
#         fields = ('Electricalreticulation_APSInstallation_image_1','Electricalreticulation_APSInstallation_image_2','Electricalreticulation_APSInstallation_image_3')


# class ElectricalEarthingImagesSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = ElectricalEarthing
#         fields = ('Earthing_connections_and_testing_image_1','Earthing_connections_and_testing_image_2','Earthing_connections_and_testing_image_3',)


# class GeneratorInstallationImagesSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = GeneratorInstallation
#         fields = ('Generator_and_Fuel_Tank_Installation_image_1','Generator_and_Fuel_Tank_Installation_image_2','Generator_and_Fuel_Tank_Installation_image_3','before_fuel_image_1','before_fuel_image_2','after_fuel_image_1','after_fuel_image_2')


# class KPLCSolarImagesSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = KPLCSolarImage
#         fields = ('kplc_solar_installation_image_1','kplc_solar_installation_image_2','kplc_solar_installation_image_3',)


# class BTSinstallationTaskImagesSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = BTSinstallationTask
#         fields = ('BTSinstallation_image_1','BTSinstallation_image_2','BTSinstallation_image_3',)


# class MWInstallationTaskImagesSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = MWInstallationTask
#         fields = ('MWinstallation_image_1','MWinstallation_image_2','MWinstallation_image_3',)


# class InstallationTeamFilesSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = InstallationTeam
#         fields = ('as_built', 'signoff', 'rfi_document', 'snag_document', 'conditional_acceptance_cert',)


# class IssuesImageSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Issues
#         fields = ('issue_image', 'issue_sorted_image',)


################### Main Project Serializer################################

class BtsSiteFilesSerializer(serializers.ModelSerializer):

    '''
    Main Serializer class : to access all serializers classes above
    :: facilitate serialization of all images and files per project
    :: Files that need not to be serialized can be commented out
     e.g
       # setsiteclearingimage = SiteClearingFilesSerializer ( read_only =True)
    :: More field can be added from the excluded one by removing from exlude variable

      '''

    siteclearingsubtask = SiteClearingSubTaskFilesSerializer ( read_only =True)
    towerbasesubtask = TowerBaseSubTaskFilesSerializer(read_only=True)
    blindingsubtask = BlindingSubTaskFilesSerializer(read_only =True)
    steelfixformworksubtask = SteelFixFormworkSubTaskFilesSerializer(read_only=True)
    concretepoursubtask = ConcretePourSubTaskFilesSerializer(read_only=True)
    concretecuringperiodsubtask = ConcreteCuringPeriodSubTaskFilesSerializer(read_only=True)
    #          #bs241 & generator fountation
    excavationsubtask = ExcavationSubTaskFilesSerializer(read_only=True)
    bs241concretepourcuringperiodsubtask = BS241ConcretePourCuringPeriodSubTaskFilesSerializer(read_only=True)
    #          # Bountary Wall
    foundfootpoursubtask = FoundFootPourSubTaskFilesSerializer(read_only=True)
    blockworkpanelconstsubtask = BlockworkPanelConstSubTaskFilesSerializer(read_only=True)
    gateinstallationsubtask = GateInstallationSubTaskFilesSerializer(read_only =True)
    # razorelectricfenceimage = RazorElectricFenceImagesSerializer(read_only=True)
    #          # Tower & Antenna
    # towererectionimage = TowerErectionImagesSerializer(read_only=True)
    # towerpaintimage = TowerPaintImagesSerializer(read_only=True)
    cablewayssubtask = CableWaysSubTaskFilesSerializer(read_only =True)
    antennacoaxinstallsubtask = AntennaCoaxInstallSubTaskFilesSerializer(read_only =True)

    #          # pos ,commercial team ,procurement 
    # projectpurchaseorders = ProjectPurchaseOrdersFileSerializer(read_only=True)
    # projectcosting = ProjectCostingFileSerializer(read_only=True)
    # commercialteam = CommercialTeamFilesSerializer(read_only=True)
    # procurementteam = ProcurementTeamFilesSerializer(read_only=True)
    #          # health docs & access approvals
    # healthdocumentscivilteam = HealthDocumentsFilesCivilTeamSerializer(many = True,read_only =True)
    # accessapprovalcivil = AccessApprovalFileCivilSerializer(many = True,read_only=True)
    # healthdocumentsInstallationteam = HealthDocumentsFilesInstallationTeamSerializer(many = True,read_only =True)
    # accessapprovalinstallation = AccessApprovalFileInstallationSerializer(many = True,read_only=True)
    #          # Installation
    # undergroundtasks = UndergroundTasksFilesSerializer(read_only=True)
    # reticulationapsinstallation = ReticulationAPSinstallationFilesSerializer(read_only=True)
    # electricalearthing = ElectricalEarthingImagesSerializer(read_only =True)
    # generatorinstallation = GeneratorInstallationImagesSerializer(read_only=True)
    # kplcsolarimage = KPLCSolarImagesSerializer(read_only=True)

    # btsinstallationtask = BTSinstallationTaskImagesSerializer(read_only=True)
    # mwinstallationtask = MWInstallationTaskImagesSerializer(read_only=True)
    # installationteam = InstallationTeamFilesSerializer(read_only =True)
    # issuess = IssuesImageSerializer(many = True,read_only=True)


    class Meta:
        model = BtsSite
       # fields = ('__all__')
        exclude = ("id","project_name","site_name","site_number","BTS_type","site_owner","final_acceptance_cert_comment","created_at",
           "updated_at", "is_active", "location", "created_by")

        #fields = ('geotech_file','access_letter','approved_drawing','final_acceptance_cert','setsiteclearingimage',
        #'towerbaseimage','bindingimage','steelfixformworkimage','concretepourcuringimage')
        #read_only_fields = ('created_at', 'updated_at', 'is_active')

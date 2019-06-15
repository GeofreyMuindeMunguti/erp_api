from rest_framework import serializers, exceptions
from rest_framework.validators import UniqueValidator
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from users.models import CustomUser
from .models import *
from rest_framework.authtoken.models import Token


class ProjectIconsSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProjectIcons
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class ProcurementTeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProcurementTeam
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')


class ProjectCostingSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProjectCosting
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')


class ProjectPurchaseOrdersSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProjectPurchaseOrders
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')


class CommercialTeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = CommercialTeam
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')


class HealthDocumentsCivilTeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = HealthDocumentsCivilTeam
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')


class AccessApprovalCivilSerializer(serializers.ModelSerializer):

    class Meta:
        model = AccessApprovalCivil
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

####################################### KPI ###############################################################################################################################

class KpiSerializer(serializers.ModelSerializer):

    class Meta:
        model = Kpi
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

######################################## END #######################################################################################################################################

####################################### TASKS ###############################################################################################################################

class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

######################################## END #######################################################################################################################################

####################################### SUBTASKS ###############################################################################################################################

class SubTaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = SubTask
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

######################################## END #######################################################################################################################################

####################################### START FOUNDATION IMAGES ###########################################################################################################################
class FoundationImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = FoundationImage
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')


class SiteClearingSerializer(serializers.ModelSerializer):

    class Meta:
        model = SetSiteClearingImage
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')


class TowerBaseImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = TowerBaseImage
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')


class BindingImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = BindingImage
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')


class SteelFixFormworkImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = SteelFixFormworkImage
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')


class ConcretePourCuringImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ConcretePourCuringImage
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

######################################## END #######################################################################################################################################

#######################################BS241 & GENERATOR FOUNDATION ###########################################################################################################################
class ExcavationImageerializer(serializers.ModelSerializer):

    class Meta:
        model = ExcavationImage
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class ConcretePourCuringPeriodImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ConcretePourCuringPeriodImage
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class BTSAndGeneatorSlabsImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = BTSAndGeneatorSlabsImage
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')
######################################## END #######################################################################################################################################

######################################  BOUNDARY WALL ###########################################################################################################################
class FoundFootPourImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = FoundFootPourImage
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class BlockworkPanelConstImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = BlockworkPanelConstImage
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class GateInstallationImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = GateInstallationImage
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class RazorElectricFenceImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = RazorElectricFenceImage
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class BoundaryWallImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = BoundaryWallImage
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

######################################## END #######################################################################################################################################

####################################### TOWER & ANTENNA_COAXs ###########################################################################################################################
class TowerErectionImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = TowerErectionImage
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class TowerPaintImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = TowerPaintImage
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class CableWaysImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = CableWaysImage
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class AntennaCoaxInstallImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = AntennaCoaxInstallImage
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class TowerAntennaCoaxImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = TowerAntennaCoaxImage
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')
######################################## END #######################################################################################################################################

class BTSAndGeneatorSlabsImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = BTSAndGeneatorSlabsImage
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class CivilWorksTeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = CivilWorksTeam
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')


class BTSinstallationTaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = BTSinstallationTask
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')


class MWInstallationTaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = MWInstallationTask
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')


class TelecomTasksSerializer(serializers.ModelSerializer):

    class Meta:
        model = TelecomTasks
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')


class UndergroundTasksSerializer(serializers.ModelSerializer):

    class Meta:
        model = UndergroundTasks
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')


class ReticulationAPSinstallationSerializer(serializers.ModelSerializer):

    class Meta:
        model = ReticulationAPSinstallation
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')


class ElectricalEarthingSerializer(serializers.ModelSerializer):

    class Meta:
        model = ElectricalEarthing
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')


class GeneratorInstallationSerializer(serializers.ModelSerializer):

    class Meta:
        model = GeneratorInstallation
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')


class ElectricalTasksSerializer(serializers.ModelSerializer):

    class Meta:
        model = ElectricalTasks
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')


class InstallationTeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = InstallationTeam
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')


class HealthDocumentsInstallationTeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = HealthDocumentsInstallationTeam
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')


class AccessApprovalInstallationSerializer(serializers.ModelSerializer):

    class Meta:
        model = AccessApprovalInstallation
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')


class KPLCSolarImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = KPLCSolarImage
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')


# PROJECT FILES:



class ProjectFilesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ('geotech_file','access_letter','approved_drawing','final_acceptance_cert',)
        #read_only_fields = ('created_at', 'updated_at', 'is_active')


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
        read_only_fields = ('created_at', 'updated_at', 'is_active')


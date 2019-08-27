from rest_framework import serializers, exceptions
from rest_framework.validators import UniqueValidator
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from users.models import CustomUser
from .models import *
from rest_framework.authtoken.models import Token


class ProjectIconSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProjectIcon
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class BtsProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = BtsProject
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class BtsSiteSerializer(serializers.ModelSerializer):

    turn_around_time = serializers.IntegerField(read_only=True)
    progress = serializers.IntegerField(read_only=True)

    class Meta:
        model = BtsSite
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')


class ProcurementTeamSerializer(serializers.ModelSerializer):
    total_material_cost = serializers.IntegerField(read_only=True)

    class Meta:
        model = ProcurementTeam
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')


class ProjectCostingSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProjectCosting
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')


class ProjectPurchaseOrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProjectPurchaseOrder
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
    track_docs = serializers.IntegerField(read_only=True)

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


class FoundationCreationTaskSerializer(serializers.ModelSerializer):
    raise_flag = serializers.CharField(read_only=True)
    team_task_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = FoundationCreationTask
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

    # SubTask (1)://///////////Site-Clearing Subtask //////////////////
class SiteClearingImageSerializer(serializers.ModelSerializer):
    bts_site_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = SiteClearingImage
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class SiteClearingDateSerializer(serializers.ModelSerializer):
    image_list = serializers.ListField(read_only=True)
    class Meta:
        model = SiteClearingDate
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class SiteClearingSubTaskSerializer(serializers.ModelSerializer):
    raise_flag = serializers.CharField(read_only=True)
    task_id = serializers.IntegerField(read_only=True)
    days_list = serializers.ListField(read_only=True)
    class Meta:
        model = SiteClearingSubtask
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

    # SubTask (2):Tower-Base Subtask ////////////////////

class TowerBaseImageSerializer(serializers.ModelSerializer):
    bts_site_id = serializers.IntegerField(read_only=True)
    class Meta:
        model = TowerBaseImage
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class TowerBaseDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TowerBaseDate
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active') 
  
class TowerBaseSubTaskSerializer(serializers.ModelSerializer):
    raise_flag = serializers.CharField(read_only=True)
    task_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = TowerBaseSubtask
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

    # SubTask (3)://///////////SiteBlindingSubTask Subtask //////////////////

class BlindingSubTaskSerializer(serializers.ModelSerializer):
    raise_flag = serializers.CharField(read_only=True)
    task_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = BlindingSubtask
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class BlindingDateSerializer(serializers.ModelSerializer):

    class Meta:
        model = BlindingDate
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class BlindingImageSerializer(serializers.ModelSerializer):
    bts_site_id = serializers.IntegerField(read_only=True)
    class Meta:
        model = BlindingImage
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

    # SubTask (4)://///////////SteelFixFormwork Subtask //////////////////
    #        
class SteelFixFormworkSubTaskSerializer(serializers.ModelSerializer):
    raise_flag = serializers.CharField(read_only=True)
    task_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = SteelFixFormworkSubtask
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')
   # SubTask (5)://///////////SteelFixFormwork Subtask //////////////////


class SteelFixFormworkDateSerializer(serializers.ModelSerializer):

    class Meta:
        model = SteelFixFormworkDate
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')


class SteelFixFormworkImageSerializer(serializers.ModelSerializer):
    bts_site_id = serializers.IntegerField(read_only=True)
    class Meta:
        model = SteelFixFormworkImage
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

   # SubTask (5)://///////////ConcretePour Subtask //////////////////


class ConcretePourSubTaskSerializer(serializers.ModelSerializer):
    raise_flag = serializers.CharField(read_only=True)
    task_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = ConcretePourSubtask
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class ConcretePourDateSerializer(serializers.ModelSerializer):

    class Meta:
        model = ConcretePourDate
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class ConcretePourImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ConcretePourImage
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')


   # SubTask (5)://///////////ConcreteCuringPeriod Subtask //////////////////

class ConcreteCuringPeriodSubTaskSerializer(serializers.ModelSerializer):
    raise_flag = serializers.CharField(read_only=True)
    task_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = ConcreteCuringPeriodSubtask
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')


class ConcreteCuringPeriodDateSerializer(serializers.ModelSerializer):

    class Meta:
        model = ConcreteCuringPeriodDate
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class ConcreteCuringPeriodImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ConcreteCuringPeriodImage
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')
        
######################################## END #######################################################################################################################################

#######################################BS241 & GENERATOR FOUNDATION ###########################################################################################################################

  # SubTask (5):///////////ExcavationSubTask Subtask //////////////////

class ExcavationSubTaskSerializer(serializers.ModelSerializer):
    raise_flag = serializers.CharField(read_only=True)
    task_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = ExcavationSubtask
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class ExcavationDateSerializer(serializers.ModelSerializer):

    class Meta:
        model = ExcavationDate
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class ExcavationImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ExcavationImage
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')


  # SubTask (5)://///////////BS241ConcretePourCuringPeriodSubTask Subtask //////////////////

class ConcretePourCuringPeriodSubTaskSerializer(serializers.ModelSerializer):
    raise_flag = serializers.CharField(read_only=True)
    task_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = BS241ConcretePourCuringPeriodSubtask
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class BS241ConcretePourCuringPeriodDateSerializer(serializers.ModelSerializer):

    class Meta:
        model = BS241ConcretePourCuringPeriodDate
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class BS241ConcretePourCuringPeriodImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = BS241ConcretePourCuringPeriodImage
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')


  # SubTask (5):////////////BS241AndGeneatorSlabs Subtask //////////////////

class BS241AndGeneratorSlabTaskSerializer(serializers.ModelSerializer):
    raise_flag = serializers.CharField(read_only=True)
    team_task_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = BS241AndGeneratorSlabTask
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

######################################## END #######################################################################################################################################

######################################  BOUNDARY WALL ###########################################################################################################################

  # SubTask (1)://///////////FoundFootPourubTask Subtask //////////////////

class FoundFootPourSubtaskSerializer(serializers.ModelSerializer):
    raise_flag = serializers.CharField(read_only=True)
    task_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = FoundFootPourSubtask
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class FoundFootPourDateSerializer(serializers.ModelSerializer):

    class Meta:
        model = FoundFootPourDate
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class FoundFootPourImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = FoundFootPourImage
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')


  # SubTask (2):///////////BlockworkPanelConst Subtask //////////////////

class BlockworkPanelConstSubtaskSerializer(serializers.ModelSerializer):
    raise_flag = serializers.CharField(read_only=True)
    task_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = BlockworkPanelConstImage
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class BlockworkPanelConstDateSerializer(serializers.ModelSerializer):

    class Meta:
        model = BlockworkPanelConstDate
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class BlockworkPanelConstImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = BlockworkPanelConstImage
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')


  # SubTask (1)://///////////GateInstallation  Subtask //////////////////
class GateInstallationSubtaskSerializer(serializers.ModelSerializer):
    raise_flag = serializers.CharField(read_only=True)
    task_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = GateInstallationSubtask
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class GateInstallationDateSerializer(serializers.ModelSerializer):

    class Meta:
        model = GateInstallationDate
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class GateInstallationImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = GateInstallationImage
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')


  # SubTask (4)://///////////RazorElectricFenceSubtask //////////////////

class RazorElectricFenceSubtaskSerializer(serializers.ModelSerializer):
    raise_flag = serializers.CharField(read_only=True)
    task_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = RazorElectricFenceSubtask
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')


class RazorElectricFenceDateSerializer(serializers.ModelSerializer):

    class Meta:
        model = RazorElectricFenceDate
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class RazorElectricFenceImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = RazorElectricFenceImage
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')


  # Task (4): BoundaryWall //////////////////

class BoundaryWallTaskSerializer(serializers.ModelSerializer):
    raise_flag = serializers.CharField(read_only=True)
    team_task_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = BoundaryWallTask
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

######################################## END #######################################################################################################################################

####################################### TOWER & ANTENNA_COAXs ###########################################################################################################################

  # SubTask (4)://///////////RazorElectricFenceSubtask //////////////////
class TowerErectionSubtaskSerializer(serializers.ModelSerializer):
    raise_flag = serializers.CharField(read_only=True)
    task_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = TowerErectionSubtask
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class TowerErectionDateSerializer(serializers.ModelSerializer):

    class Meta:
        model = TowerErectionDate
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class TowerErectionImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = TowerErectionImage
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

  # SubTask (4)://///////////RazorElectricFenceSubtask //////////////////
class TowerPaintSubtaskSerializer(serializers.ModelSerializer):
    raise_flag = serializers.CharField(read_only=True)
    task_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = TowerPaintSubtask
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class TowerPaintDateSerializer(serializers.ModelSerializer):

    class Meta:
        model = TowerPaintDate
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class TowerPaintImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = TowerPaintImage
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')


  # SubTask (4)://///////////CableWays Subtask //////////////////
class CableWaysSubtaskSerializer(serializers.ModelSerializer):
    raise_flag = serializers.CharField(read_only=True)
    task_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = CableWaysSubtask
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class CableWaysDateSerializer(serializers.ModelSerializer):

    class Meta:
        model = CableWaysDate
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class CableWaysImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = CableWaysImage
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

  # SubTask (4)://///////////AntennaCoaxInstall Subtask //////////////////
class AntennaCoaxInstallSubtaskSerializer(serializers.ModelSerializer):
    raise_flag = serializers.CharField(read_only=True)
    task_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = AntennaCoaxInstallSubtask
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')


class AntennaCoaxInstallDateSerializer(serializers.ModelSerializer):

    class Meta:
        model = AntennaCoaxInstallDate
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class AntennaCoaxInstallImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = AntennaCoaxInstallImage
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

  # SubTask (4)://////////TowerAntennaCoax Subtask //////////////////

class TowerAntennaCoaxTaskSerializer(serializers.ModelSerializer):
    raise_flag = serializers.CharField(read_only=True)
    team_task_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = TowerAntennaCoaxTask
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')


######################################## END #######################################################################################################################################


class CivilWorksTeamSerializer(serializers.ModelSerializer):
    raise_flag = serializers.CharField(read_only=True)

    class Meta:
        model = CivilWorksTeam
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')


class BTSinstallationTaskSerializer(serializers.ModelSerializer):
    raise_flag = serializers.CharField(read_only=True)
    task_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = BTSinstallationTask
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')


class BTSinstallationTaskDateSerializer(serializers.ModelSerializer):

    class Meta:
        model = BTSinstallationTaskDate
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class BTSinstallationTaskImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = BTSinstallationTaskImage
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')


class MWInstallationTaskSerializer(serializers.ModelSerializer):
    raise_flag = serializers.CharField(read_only=True)
    task_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = MWInstallationTask
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class MWInstallationTaskDateSerializer(serializers.ModelSerializer):

    class Meta:
        model = MWInstallationTaskDate
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class MWInstallationTaskImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = MWInstallationTaskImage
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class BTSinstallationTaskDateSerializer(serializers.ModelSerializer):

    class Meta:
        model = BTSinstallationTaskDate
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class BTSinstallationTaskImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = BTSinstallationTaskImage
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')


class TelecomTaskSerializer(serializers.ModelSerializer):
    raise_flag = serializers.CharField(read_only=True)
    team_task_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = TelecomTask
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')


class UndergroundTaskSerializer(serializers.ModelSerializer):
    raise_flag = serializers.CharField(read_only=True)
    task_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = UndergroundTask
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class UndergroundTaskDateSerializer(serializers.ModelSerializer):

    class Meta:
        model = UndergroundTaskDate
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class UndergroundTaskImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = UndergroundTaskImage
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')


class ReticulationAPSSerializer(serializers.ModelSerializer):
    raise_flag = serializers.CharField(read_only=True)
    task_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = ReticulationAPSinstallation
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class ReticulationAPSDateSerializer(serializers.ModelSerializer):

    class Meta:
        model = ReticulationAPSinstallationDate
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class ReticulationAPSImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ReticulationAPSinstallationImage
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class ElectricalEarthingSerializer(serializers.ModelSerializer):
    raise_flag = serializers.CharField(read_only=True)
    task_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = ElectricalEarthing
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class ElectricalEarthingDateSerializer(serializers.ModelSerializer):

    class Meta:
        model = ElectricalEarthingDate
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class ElectricalEarthingImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ElectricalEarthingImage
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class GeneratorInstallationSerializer(serializers.ModelSerializer):
    raise_flag = serializers.CharField(read_only=True)
    task_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = GeneratorInstallation
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')


class GeneratorInstallationDateSerializer(serializers.ModelSerializer):

    class Meta:
        model = GeneratorInstallationDate
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class GeneratorInstallationImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = GeneratorInstallationImage
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

  # SubTask (4)://////////ElectricalTask Subtask //////////////////

class ElectricalTaskSerializer(serializers.ModelSerializer):
    raise_flag = serializers.CharField(read_only=True)
    team_task_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = ElectricalTask
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


class KPLCSolarSubtaskSerializer(serializers.ModelSerializer):
    raise_flag = serializers.CharField(read_only=True)

    class Meta:
        model = KPLCSolarSubtask
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class KPLCSolarDateSerializer(serializers.ModelSerializer):

    class Meta:
        model = KPLCSolarDate
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class KPLCSolarImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = KPLCSolarImage
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

  # SubTask (4)://////////ElectricalTask Subtask //////////////////


class WarrantyCertificateSerializer(serializers.ModelSerializer):

    class Meta:
        model = WarrantyCertificate
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')


class TestCetificateSerializer(serializers.ModelSerializer):

    class Meta:
        model = TestCetificate
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')


class IssueSerializer(serializers.ModelSerializer):

    class Meta:
        model = Issue
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

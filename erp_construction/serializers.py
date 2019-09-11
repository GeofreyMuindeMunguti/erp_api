from rest_framework import serializers, exceptions
from rest_framework.validators import UniqueValidator
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from users.models import *
from .models import *
from rest_framework.authtoken.models import Token


class ProjectIconsSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProjectIcons
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


class FoundationImageSerializer(serializers.ModelSerializer):
    raise_flag = serializers.CharField(read_only=True)
    team_task_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = FoundationImage
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')


class SiteClearingSerializer(serializers.ModelSerializer):
    raise_flag = serializers.CharField(read_only=True)
    task_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = SetSiteClearingImage
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')


class TowerBaseImageSerializer(serializers.ModelSerializer):
    raise_flag = serializers.CharField(read_only=True)
    task_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = TowerBaseImage
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')


class BindingImageSerializer(serializers.ModelSerializer):
    raise_flag = serializers.CharField(read_only=True)
    task_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = BindingImage
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')


class SteelFixFormworkImageSerializer(serializers.ModelSerializer):
    raise_flag = serializers.CharField(read_only=True)
    task_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = SteelFixFormworkImage
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')


class ConcretePourImageSerializer(serializers.ModelSerializer):
    raise_flag = serializers.CharField(read_only=True)
    task_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = ConcretePourImage
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')


class ConcreteCuringPeriodImageSerializer(serializers.ModelSerializer):
    raise_flag = serializers.CharField(read_only=True)
    task_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = ConcreteCuringPeriodImage
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

######################################## END #######################################################################################################################################

#######################################BS241 & GENERATOR FOUNDATION ###########################################################################################################################


class ExcavationImageerializer(serializers.ModelSerializer):
    raise_flag = serializers.CharField(read_only=True)
    task_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = ExcavationImage
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')


class ConcretePourCuringPeriodImageSerializer(serializers.ModelSerializer):
    raise_flag = serializers.CharField(read_only=True)
    task_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = BS241ConcretePourCuringPeriodImage
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')


class BS241AndGeneatorSlabsImageSerializer(serializers.ModelSerializer):
    raise_flag = serializers.CharField(read_only=True)
    team_task_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = BS241AndGeneatorSlabsImage
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')
######################################## END #######################################################################################################################################

######################################  BOUNDARY WALL ###########################################################################################################################


class FoundFootPourImageSerializer(serializers.ModelSerializer):
    raise_flag = serializers.CharField(read_only=True)
    task_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = FoundFootPourImage
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')


class BlockworkPanelConstImageSerializer(serializers.ModelSerializer):
    raise_flag = serializers.CharField(read_only=True)
    task_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = BlockworkPanelConstImage
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')


class GateInstallationImageSerializer(serializers.ModelSerializer):
    raise_flag = serializers.CharField(read_only=True)
    task_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = GateInstallationImage
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')


class RazorElectricFenceImageSerializer(serializers.ModelSerializer):
    raise_flag = serializers.CharField(read_only=True)
    task_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = RazorElectricFenceImage
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')


class BoundaryWallImageSerializer(serializers.ModelSerializer):
    raise_flag = serializers.CharField(read_only=True)
    team_task_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = BoundaryWallImage
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

######################################## END #######################################################################################################################################

####################################### TOWER & ANTENNA_COAXs ###########################################################################################################################


class TowerErectionImageSerializer(serializers.ModelSerializer):
    raise_flag = serializers.CharField(read_only=True)
    task_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = TowerErectionImage
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')


class TowerPaintImageSerializer(serializers.ModelSerializer):
    raise_flag = serializers.CharField(read_only=True)
    task_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = TowerPaintImage
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')


class CableWaysImageSerializer(serializers.ModelSerializer):
    raise_flag = serializers.CharField(read_only=True)
    task_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = CableWaysImage
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')


class AntennaCoaxInstallImageSerializer(serializers.ModelSerializer):
    raise_flag = serializers.CharField(read_only=True)
    task_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = AntennaCoaxInstallImage
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')


class TowerAntennaCoaxImageSerializer(serializers.ModelSerializer):
    raise_flag = serializers.CharField(read_only=True)
    team_task_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = TowerAntennaCoaxImage
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


class MWInstallationTaskSerializer(serializers.ModelSerializer):
    raise_flag = serializers.CharField(read_only=True)
    task_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = MWInstallationTask
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')


class TelecomTasksSerializer(serializers.ModelSerializer):
    raise_flag = serializers.CharField(read_only=True)
    team_task_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = TelecomTasks
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')


class UndergroundTasksSerializer(serializers.ModelSerializer):
    raise_flag = serializers.CharField(read_only=True)
    task_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = UndergroundTasks
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')


class ReticulationAPSinstallationSerializer(serializers.ModelSerializer):
    raise_flag = serializers.CharField(read_only=True)
    task_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = ReticulationAPSinstallation
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')


class ElectricalEarthingSerializer(serializers.ModelSerializer):
    raise_flag = serializers.CharField(read_only=True)
    task_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = ElectricalEarthing
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')


class GeneratorInstallationSerializer(serializers.ModelSerializer):
    raise_flag = serializers.CharField(read_only=True)
    task_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = GeneratorInstallation
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')


class ElectricalTasksSerializer(serializers.ModelSerializer):
    raise_flag = serializers.CharField(read_only=True)
    team_task_id = serializers.IntegerField(read_only=True)

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
    raise_flag = serializers.CharField(read_only=True)

    class Meta:
        model = KPLCSolarImage
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')


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


class IssuesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Issues
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

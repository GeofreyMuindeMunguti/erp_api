from rest_framework.views import APIView
from .models import *
from rest_framework.response import Response


"""VIEWS TO CALCULATE PROGRESS OF TEAMS/CATEGORIES"""


class CommercialTeamProgressView(APIView):

    def get(self, request, pk):
        total_tasks = 4
        completed_tasks = 0
        approved_quote_status = ''
        po_status = ''
        project_costing_status = ''
        initial_invoice_status = ''
        project_id = pk
        try:
            progress_object = CommercialTeam.objects.get(project_name=project_id)
        except Exception as e:
            return Response({'error': 'Task not started'})
        approved_quote = progress_object.approved_quote_file
        po = progress_object.po_data
        project_costing = progress_object.project_costing_data
        initialinvoice = progress_object.initial_invoice
        if bool(po) is False:
            po_status = "Not uploaded"
        else:
            completed_tasks += 1
            po_status = "Uploaded"
        if bool(initialinvoice) is False:
            initial_invoice_status = "Not Uploaded"
        else:
            completed_tasks += 1
            initial_invoice_status = "Uploaded"
        if bool(approved_quote) is False:
            approved_quote_status = "Not Uploaded"
        else:
            completed_tasks += 1
            approved_quote_status = "Uploaded"
        if bool(project_costing) is False:
            project_costing_status = "Not Uploaded"
        else:
            completed_tasks += 1
            project_costing_status = "Uploaded"
        commercial_percentage = percentage_function(completed_tasks, total_tasks)
        return Response({'no_of_tasks': total_tasks, 'po_status': po_status, 'initial_invoice_status': initial_invoice_status, 'approved_quote_status': approved_quote_status, 'project_costing_status': project_costing_status, 'progress': commercial_percentage})


class ProcurementProgressTeamView(APIView):

    def get(self, request, pk):
        total_tasks = 3
        completed_tasks = 0
        po_steel_status = ''
        po_electrical_materials_status = ''
        po_subcontractors_status = ''
        project_id = pk
        try:
            progress_object = ProcurementTeam.objects.get(project_name=project_id)
        except Exception as e:
            return Response({'error': 'Task not started'})
        po_steel = progress_object.po_steel
        po_electrical_materials = progress_object.po_electrical_materials
        po_subcontractors = progress_object.po_subcontractors
        if bool(po_steel) is False:
            po_steel_status = "Not uploaded"
        else:
            completed_tasks += 1
            po_steel_status = "Uploaded"
        if bool(po_electrical_materials) is False:
            po_electrical_materials_status = "Not Uploaded"
        else:
            completed_tasks += 1
            po_electrical_materials_status = "Uploaded"
        if bool(po_subcontractors) is False:
            po_subcontractors_status = "Not Uploaded"
        else:
            completed_tasks += 1
            po_subcontractors_status = "Uploaded"
        procurement_percentage = percentage_function(completed_tasks, total_tasks)
        return Response({'no_of_tasks': total_tasks, 'po_steel_status': po_steel_status, 'po_electrical_materials_status': po_electrical_materials_status, 'po_subcontractors_status': po_subcontractors_status, 'progress': procurement_percentage})


class CivilProgressView(APIView):

    def get(self, request, pk):
        total_tasks = 4
        completed_tasks = 0
        foundation_status = ''
        slabs_status = ''
        site_walling_status = ''
        tower_status = ''
        project_id = pk
        try:
            progress_object = CivilWorksTeam.objects.get(project_name=project_id)
        except Exception as e:
            return Response({'error': 'Task not started'})
        foundation_and_curing_images = progress_object.foundation_and_curing_images
        bts_and_generator_slabs_images = progress_object.bts_and_generator_slabs_images
        site_walling_images_field = progress_object.site_walling_images_field
        tower_field = progress_object.tower_data
        if bool(foundation_and_curing_images) is False:
            foundation_status = "Not uploaded"
        else:
            completed_tasks += 1
            foundation_status = "Uploaded"
        if bool(bts_and_generator_slabs_images) is False:
            slabs_status = "Not Uploaded"
        else:
            completed_tasks += 1
            slabs_status = "Uploaded"
        if bool(site_walling_images_field) is False:
            site_walling_status = "Not Uploaded"
        else:
            completed_tasks += 1
            site_walling_status = "Uploaded"
        if bool(tower_field) is False:
            tower_status = "Not Uploaded"
        else:
            completed_tasks += 1
            tower_status = "Uploaded"
        civil_percentage = percentage_function(completed_tasks, total_tasks)
        return Response({'no_of_tasks': total_tasks, 'foundation_status': foundation_status, 'slabs_status': slabs_status, 'site_walling_status': site_walling_status, 'tower_status': tower_status, 'progress': civil_percentage})


class InstallationProgressView(APIView):

    def get(self, request, pk):
        total_tasks = 6
        completed_tasks = 0
        electrical_tasks_status = ''
        telecom_tasks_status = ''
        sign_off_status = ''
        rfi_status = ''
        integration_parameter_status = ''
        conditional_acceptance_status = ''
        project_id = pk
        try:
            progress_object = InstallationTeam.objects.get(project_name=project_id)
        except Exception as e:
            return Response({'error': 'Task not started'})
        electrical_tasks_data = progress_object.electrical_tasks_data
        telecom_tasks_data = progress_object.telecom_tasks_data
        signoff = progress_object.signoff
        rfi_document = progress_object.rfi_document
        integration_parameter = progress_object.integration_parameter
        conditional_acceptance_cert = progress_object.conditional_acceptance_cert
        if bool(electrical_tasks_data) is False:
            electrical_tasks_status = "Not uploaded"
        else:
            completed_tasks += 1
            electrical_tasks_status = "Uploaded"
        if bool(telecom_tasks_data) is False:
            telecom_tasks_status = "Not Uploaded"
        else:
            completed_tasks += 1
            telecom_tasks_status = "Uploaded"
        if bool(signoff) is False:
            sign_off_status = "Not Uploaded"
        else:
            completed_tasks += 1
            sign_off_status = "Uploaded"
        if bool(rfi_document) is False:
            rfi_status = "Not Uploaded"
        else:
            completed_tasks += 1
            rfi_status = "Uploaded"
        if bool(integration_parameter) is False:
            integration_parameter_status = "Not Uploaded"
        else:
            completed_tasks += 1
            integration_parameter_status = "Uploaded"
        if bool(conditional_acceptance_cert) is False:
            conditional_acceptance_status = "Not Uploaded"
        else:
            completed_tasks += 1
            conditional_acceptance_status = "Uploaded"
        civil_percentage = percentage_function(completed_tasks, total_tasks)
        return Response({'no_of_tasks': total_tasks, 'electrical_tasks_status': electrical_tasks_status, 'telecom_tasks_status': telecom_tasks_status, 'sign_off_status': sign_off_status, 'rfi_status': rfi_status, 'integration_parameter_status': integration_parameter_status, 'conditional_acceptance_status': conditional_acceptance_status, 'progress': civil_percentage})


"""VIEWS TO CALCULATE PROGRESS OF TASKS"""


"""CIVIL TEAM TASKS"""


class FoundationTaskProgressView(APIView):

    def get(self, request, pk):
        total_tasks = 5
        completed_tasks = 0
        setting_site_status = ''
        excavation_status = ''
        binding_status = ''
        steel_fix_status = ''
        concrete_pour_status = ''
        project_id = pk
        try:
            progress_object = FoundationImage.objects.get(project_name=project_id)
        except Exception as e:
            return Response({'error': 'Task not started'})
        setting_site = progress_object.setting_site_clearing
        excavation = progress_object.excavation_tower_base
        binding = progress_object.binding
        steel_fix = progress_object.steel_fix_formwork
        concrete_pour_curing = progress_object.concrete_pour_curing
        if bool(setting_site) is False:
            setting_site_status = "Not uploaded"
        else:
            completed_tasks += 1
            setting_site_status = "Uploaded"
        if bool(excavation) is False:
            excavation_status = "Not Uploaded"
        else:
            completed_tasks += 1
            excavation_status = "Uploaded"
        if bool(binding) is False:
            binding_status = "Not Uploaded"
        else:
            completed_tasks += 1
            binding_status = "Uploaded"
        if bool(steel_fix) is False:
            steel_fix_status = "Not Uploaded"
        else:
            completed_tasks += 1
            steel_fix_status = "Uploaded"
        if bool(concrete_pour_curing) is False:
            concrete_pour_status = "Not Uploaded"
        else:
            completed_tasks += 1
            concrete_pour_status = "Uploaded"
        commercial_percentage = percentage_function(completed_tasks, total_tasks)
        return Response({'no_of_tasks': total_tasks, 'setting_site_status': setting_site_status, 'excavation_status': excavation_status, 'binding_status': binding_status, 'steel_fix_status': steel_fix_status, 'concrete_pour_status': concrete_pour_status, 'progress': commercial_percentage})


def percentage_function(no_of_complete, total_task):
    """Function to return perecentage of progress  """
    percentage = ((no_of_complete/total_task) * 100)
    return percentage

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
        installation_percentage = percentage_function(completed_tasks, total_tasks)
        return Response({'no_of_tasks': total_tasks, 'electrical_tasks_status': electrical_tasks_status, 'telecom_tasks_status': telecom_tasks_status, 'sign_off_status': sign_off_status, 'rfi_status': rfi_status, 'integration_parameter_status': integration_parameter_status, 'conditional_acceptance_status': conditional_acceptance_status, 'progress': installation_percentage})


"""END OF TEAM PROGRESS"""


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
        foundation_percentage = percentage_function(completed_tasks, total_tasks)
        return Response({'no_of_tasks': total_tasks, 'setting_site_status': setting_site_status, 'excavation_status': excavation_status, 'binding_status': binding_status, 'steel_fix_status': steel_fix_status, 'concrete_pour_status': concrete_pour_status, 'progress': foundation_percentage})


class BTSandGenTaskProgressView(APIView):

    def get(self, request, pk):
        total_tasks = 2
        completed_tasks = 0
        foundation_foot_status = ''
        concrete_pour_status = ''
        project_id = pk
        try:
            progress_object = BTSAndGeneatorSlabsImage.objects.get(project_name=project_id)
        except Exception as e:
            return Response({'error': 'Task not started'})
        foundation_foot = progress_object.foundation_foot_pouring
        concrete_pour = progress_object.concrete_pour_period
        if bool(foundation_foot) is False:
            foundation_foot_status = "Not uploaded"
        else:
            completed_tasks += 1
            foundation_foot_status = "Uploaded"
        if bool(concrete_pour) is False:
            concrete_pour_status = "Not Uploaded"
        else:
            completed_tasks += 1
            concrete_pour_status = "Uploaded"
        bts_gen_percentage = percentage_function(completed_tasks, total_tasks)
        return Response({'no_of_tasks': total_tasks, 'foundation_foot_status': foundation_foot_status, 'concrete_pour_status': concrete_pour_status, 'progress': bts_gen_percentage})


class BoundaryTaskProgressView(APIView):

    def get(self, request, pk):
        total_tasks = 4
        completed_tasks = 0
        foundation_foot_status = ''
        block_status = ''
        gate_status = ''
        razor_electric_status = ''
        project_id = pk
        try:
            progress_object = BoundaryWallImage.objects.get(project_name=project_id)
        except Exception as e:
            return Response({'error': 'Task not started'})
        foundation_foot = progress_object.foundation_foot_pouring
        block = progress_object.block_construction
        gate = progress_object.gate_installation
        razor_electric = progress_object.razor_electric_fence
        if bool(foundation_foot) is False:
            foundation_foot_status = "Not uploaded"
        else:
            completed_tasks += 1
            foundation_foot_status = "Uploaded"
        if bool(block) is False:
            block_status = "Not Uploaded"
        else:
            completed_tasks += 1
            block_status = "Uploaded"
        if bool(gate) is False:
            gate_status = "Not Uploaded"
        else:
            completed_tasks += 1
            gate_status = "Uploaded"
        if bool(razor_electric) is False:
            razor_electric_status = "Not Uploaded"
        else:
            completed_tasks += 1
            razor_electric_status = "Uploaded"
        boundary_percentage = percentage_function(completed_tasks, total_tasks)
        return Response({'no_of_tasks': total_tasks, 'foundation_foot_status': foundation_foot_status, 'block_status': block_status, 'gate_status': gate_status, 'razor_electric_status': razor_electric_status, 'progress': boundary_percentage})


class TowerTaskProgressView(APIView):

    def get(self, request, pk):
        total_tasks = 4
        completed_tasks = 0
        tower_erection_status = ''
        tower_painting_status = ''
        cable_ways_status = ''
        antenna_status = ''
        project_id = pk
        try:
            progress_object = TowerAntennaCoaxImage.objects.get(project_name=project_id)
        except Exception as e:
            return Response({'error': 'Task not started'})
        erection = progress_object.tower_erection
        painting = progress_object.tower_painting
        cable = progress_object.cable_ways
        antenna = progress_object.antenna_coax_installation
        if bool(erection) is False:
            tower_erection_status = "Not uploaded"
        else:
            completed_tasks += 1
            tower_erection_status = "Uploaded"
        if bool(painting) is False:
            tower_painting_status = "Not Uploaded"
        else:
            completed_tasks += 1
            tower_painting_status = "Uploaded"
        if bool(cable) is False:
            cable_ways_status = "Not Uploaded"
        else:
            completed_tasks += 1
            cable_ways_status = "Uploaded"
        if bool(antenna) is False:
            antenna_status = "Not Uploaded"
        else:
            completed_tasks += 1
            antenna_status = "Uploaded"
        tower_percentage = percentage_function(completed_tasks, total_tasks)
        return Response({'no_of_tasks': total_tasks, 'tower_erection_status': tower_erection_status, 'tower_painting_status': tower_painting_status, 'cable_ways_status': cable_ways_status, 'antenna_status': antenna_status, 'progress': tower_percentage})


"""END OF CIVIL TASKS"""


"""INSTALLATION TEAM TASKS"""


class ElectricalTaskProgressView(APIView):

    def get(self, request, pk):
        total_tasks = 5
        completed_tasks = 0
        Underground_status = ''
        reticulation_status = ''
        earthing_status = ''
        fuel_installation_status = ''
        kplc_status = ''
        project_id = pk
        try:
            progress_object = ElectricalTasks.objects.get(project_name=project_id)
        except Exception as e:
            return Response({'error': 'Task not started'})
        underground = progress_object.Underground_ducting_and_manholes
        reticulation = progress_object.Electricalreticulation_APSInstallation
        earthing = progress_object.Earthing_connections_and_testing
        fuel_tasks = progress_object.Generator_and_Fuel_Tank_Installation
        kplc_solar = progress_object.KPLC_solar_installation
        if bool(underground) is False:
            Underground_status = "Not uploaded"
        else:
            completed_tasks += 1
            Underground_status = "Uploaded"
        if bool(reticulation) is False:
            reticulation_status = "Not Uploaded"
        else:
            completed_tasks += 1
            reticulation_status = "Uploaded"
        if bool(earthing) is False:
            earthing_status = "Not Uploaded"
        else:
            completed_tasks += 1
            earthing_status = "Uploaded"
        if bool(fuel_tasks) is False:
            fuel_installation_status = "Not Uploaded"
        else:
            completed_tasks += 1
            fuel_installation_status = "Uploaded"
        if bool(kplc_solar) is False:
            kplc_status = "Not Uploaded"
        else:
            completed_tasks += 1
            kplc_status = "Uploaded"
        electrical_percentage = percentage_function(completed_tasks, total_tasks)
        return Response({'no_of_tasks': total_tasks, 'Underground_status': Underground_status, 'reticulation_status': reticulation_status, 'earthing_status': earthing_status, 'fuel_installation_status': fuel_installation_status, 'kplc_status': kplc_status, 'progress': electrical_percentage})


class TelecomTaskProgressView(APIView):

    def get(self, request, pk):
        total_tasks = 3
        completed_tasks = 0
        bts_installation_status = ''
        mw_installation_status = ''
        link_commissioning_status = ''
        project_id = pk
        try:
            progress_object = TelecomTasks.objects.get(project_name=project_id)
        except Exception as e:
            return Response({'error': 'Task not started'})
        bts = progress_object.Installation_of_BTS
        microwave = progress_object.Installation_of_MW_links
        commissioning = progress_object.link_commissioning
        if bool(bts) is False:
            bts_installation_status = "Not uploaded"
        else:
            completed_tasks += 1
            bts_installation_status = "Uploaded"
        if bool(microwave) is False:
            mw_installation_status = "Not Uploaded"
        else:
            completed_tasks += 1
            mw_installation_status = "Uploaded"
        if commissioning is False:
            link_commissioning_status = "Link not commissioned"
        else:
            completed_tasks += 1
            link_commissioning_status = "Link is commissioned"
        telecom_percentage = percentage_function(completed_tasks, total_tasks)
        return Response({'no_of_tasks': total_tasks, 'bts_installation_status': bts_installation_status, 'mw_installation_status': mw_installation_status, 'link_commissioning_status': link_commissioning_status, 'progress': telecom_percentage})


"""END OF INSTALLATION TASKS"""


def percentage_function(no_of_complete, total_task):
    """Function to return perecentage of progress  """
    percentage = ((no_of_complete/total_task) * 100)
    return percentage
from rest_framework.views import APIView
from erp_ftts.models import *
from rest_framework.response import Response

"""GET PROJECT PROGRESS"""


class FttsProjectProgressView(APIView):

    def get(self, request, pk):
        #PROGRESS FOR COMMERCIAL TEAM
        try:
            category = Category.objects.get(category_name='FTTS Commercial Team')
            category_id = category.id
            automatic_total_comtasks = FttsTask.objects.filter(category_name=category_id).count()
            completed_ctasks = 0
            site_id = self.id
            progress_object = FttsCommercialTeam.objects.get(site_name=site_id)
            ftts_approved_quote = progress_object.ftts_quote
            ftts_po = progress_object.ftts_po_data
            fttsinitialinvoice = progress_object.ftts_initial_invoice
            if bool(ftts_po) is False:
                completed_ctasks += 0
            else:
                completed_ctasks += 1
            if bool(fttsinitialinvoice) is False:
                completed_ctasks += 0
            else:
                completed_ctasks += 1
            if bool(ftts_approved_quote) is False:
                completed_ctasks += 0
            else:
                completed_ctasks += 1
            commercial_percentage = ftts_percentage_function(completed_ctasks, automatic_total_comtasks)
        except Exception as e:
            commercial_percentage = 0

            #return Response({'error': 'Commercial Team does not exist'})

        #PROGRESS FOR PROCUREMENTEAM
        try:
            category = Category.objects.get(category_name='FTTS Procurement Team')
            category_id = category.id
            automatic_total_protasks = FttsTask.objects.filter(category_name=category_id).count()
            completed_ptasks = 0
            site_id = self.id
            progress_object = FttsProcurementTeam.objects.get(site_name=site_id)
            site_material_requisition = progress_object.ftts_material_requisition
            site_po_subcontractors = progress_object.ftts_po_subcontractors
            if bool(site_material_requisition) is False:
                completed_ptasks += 0
            else:
                completed_ptasks += 1
            if bool(site_po_subcontractors) is False:
                completed_ptasks += 0
            else:
                completed_ptasks += 1
            procurement_percentage = percentage_function(completed_ptasks, automatic_total_protasks)
        except Exception as e:
            procurement_percentage = 0

        #PROGRESS FOR CIVIL TEAM
        try:
            category = Category.objects.get(category_name='FTTS Civil Team')
            category_id = category.id
            automatic_total_civtasks = FttsTask.objects.filter(category_name=category_id).count()
            completed_cltasks = 0
            site_id = self.id
            progress_object = FttsCivilTeam.objects.get(site_name=site_id)
            ftts_trenching = progress_object.ftts_trenching
            ftts_duct_installation = progress_object.ftts_duct_installation
            ftts_cable_installation = progress_object.ftts_cable_installation
            ftts_manhole_installation = progress_object.ftts_manhole_installation
            if bool(ftts_trenching) is False:
                completed_cltasks += 0
            else:
                completed_cltasks += 1
            if bool(ftts_duct_installation) is False:
                completed_cltasks += 0
            else:
                completed_cltasks += 1
            if bool(ftts_cable_installation) is False:
                completed_cltasks += 0
            else:
                completed_cltasks += 1
            if bool(ftts_manhole_installation) is False:
                completed_cltasks += 0
            else:
                completed_cltasks += 1
            civil_percentage = percentage_function(completed_cltasks, automatic_total_civtasks)
        except Exception as e:
            civil_percentage = 0

        #PROGRESS FOR INSTALLATION TEAM
        try:
            category = Category.objects.get(category_name='FTTS Installation Team')
            category_id = category.id
            automatic_total_instasks = FttsTask.objects.filter(category_name=category_id).count()
            completed_intasks = 0
            site_id = self.id
            progress_object = FttsInstallationTeam.objects.get(site_name=site_id)
            ftts_terminal_in_hse = progress_object.ftts_terminal_in_hse
            ftts_interception = progress_object.ftts_interception
            ftts_integration = progress_object.ftts_integration
            if bool(ftts_terminal_in_hse) is False:
                completed_intasks += 0
            else:
                completed_intasks += 1
            if bool(ftts_interception) is False:
                completed_intasks += 0
            else:
                completed_intasks += 1
            if bool(ftts_integration) is False:
                completed_intasks += 0
            else:
                completed_intasks += 1
            installation_percentage = percentage_function(completed_intasks, automatic_total_instasks)
        except Exception as e:
            installation_percentage = 0

        project_percentage = ((commercial_percentage + civil_percentage + procurement_percentage + installation_percentage )/4)

        return Response({'progress': project_percentage, 'site_id': pk})


"""END OF PROJECT PROGRESS"""

"""VIEWS TO CALCULATE PROGRESS OF TEAMS/CATEGORIES"""

class FttsCommercialTeamProgressView(APIView):

    def get(self, request, pk):
        total_tasks = 7 #HARDCODED WILL LEAVE HERE FOR CONFIMATION WHEN TESTING.
        try:
            category = Category.objects.get(category_name='FTTS Commercial Team')
            category_id = category.id
        except Exception as e:
            return Response({'error': 'FTTS Commercial Team does not exist'})
        automatic_total_tasks = FttsTask.objects.filter(category_name=category_id).count()
        completed_tasks = 0
        ftts_quote_status = ''
        ftts_po_data_status = ''
        ftts_initial_invoice_status = ''
        site_id = pk
        try:
            progress_object = FttsCommercialTeam.objects.get(site_name=site_id)
        except Exception as e:
            return Response({'error': 'Task not started', 'no_of_tasks': automatic_total_tasks,})
        ftts_quote = progress_object.ftts_quote
        ftts_po_data = progress_object.ftts_po_data
        ftts_initial_invoice = progress_object.ftts_initial_invoice
        if bool(ftts_quote) is False:
            ftts_quote_status = "Not uploaded"
        else:
            completed_tasks += 1
            ftts_quote_status = "Uploaded"
        if bool(ftts_po_data) is False:
            ftts_po_data_status = "Not Uploaded"
        else:
            completed_tasks += 1
            ftts_po_data_status = "Uploaded"
        if bool(ftts_initial_invoice) is False:
            ftts_initial_invoice_status = "Not Uploaded"
        else:
            completed_tasks += 1
            ftts_initial_invoice_status = "Uploaded"
        commercial_percentage = percentage_function(completed_tasks, automatic_total_tasks)
        return Response({'no_of_tasks': automatic_total_tasks,'ftts_quote_status': ftts_quote_status,
         'ftts_po_data_status': ftts_po_data_status, 'ftts_initial_invoice_status': ftts_initial_invoice_status, 'progress': commercial_percentage})


class FttsProcurementProgressTeamView(APIView):

    def get(self, request, pk):
        total_tasks = 3 #HARDCODED WILL LEAVE HERE FOR CONFIMATION WHEN TESTING.
        try:
            category = Category.objects.get(category_name='FTTS Procurement Team')
            category_id = category.id
        except Exception as e:
            return Response({'error': 'FTTS Procurement Team does not exist'})
        automatic_total_tasks = FttsTask.objects.filter(category_name=category_id).count()
        completed_tasks = 0
        site_material_requisition_status = ''
        site_po_subcontractors_status = ''
        po_subcontractors_status = ''
        site_id = pk
        try:
            progress_object = FttsProcurementTeam.objects.get(site_name=site_id)
        except Exception as e:
            return Response({'error': 'Task not started', 'no_of_tasks': automatic_total_tasks,})
        site_material_requisition = progress_object.ftts_material_requisition
        site_po_subcontractors = progress_object.ftts_po_subcontractors
        ftts_po_quote_serviceno = progress_object.ftts_po_quote_serviceno
        if bool(site_material_requisition) is False:
            site_material_requisition_status = "Not uploaded"
        else:
            completed_tasks += 1
            site_material_requisition_status = "Uploaded"
        if bool(site_po_subcontractors) is False:
            site_po_subcontractors_status = "Not Uploaded"
        else:
            completed_tasks += 1
            site_po_subcontractors_status = "Uploaded"
        if bool(ftts_po_quote_serviceno) is False:
            ftts_po_quote_serviceno_status = "Not Uploaded"
        else:
            completed_tasks += 1
            ftts_po_quote_serviceno_status = "Uploaded"
        procurement_percentage = percentage_function(completed_tasks, automatic_total_tasks)
        return Response({'no_of_tasks': automatic_total_tasks, 'site_material_requisition_status': site_material_requisition_status, 'site_po_subcontractors_status': site_po_subcontractors_status,
        'ftts_po_quote_serviceno_status': ftts_po_quote_serviceno_status, 'progress': procurement_percentage})


class FttsCivilProgressView(APIView):

    def get(self, request, pk):
        total_tasks = 4 #HARDCODED WILL LEAVE HERE FOR CONFIMATION WHEN TESTING.
        try:
            category = Category.objects.get(category_name='Civil Team Tasks')
            category_id = category.id
        except Exception as e:
            return Response({'error': 'Civil Team does not exist'})
        automatic_total_tasks = FiberTask.objects.filter(category_name=category_id).count()
        completed_tasks = 0
        ftts_trenching_status = ''
        ftts_duct_installation_status = ''
        ftts_cable_installation_status = ''
        ftts_manhole_installation_status = ''
        site_id = pk
        try:
            progress_object = CivilWorksTeam.objects.get(project_name=project_id)
        except Exception as e:
            return Response({'error': 'Task not started', 'no_of_tasks': automatic_total_tasks,})
        ftts_trenching = progress_object.ftts_trenching
        ftts_duct_installation = progress_object.ftts_duct_installation
        ftts_cable_installation = progress_object.ftts_cable_installation
        ftts_manhole_installation = progress_object.ftts_manhole_installation
        tower_field = progress_object.tower_data
        if bool(ftts_trenching) is False:
            ftts_trenching_status = "Not uploaded"
        else:
            completed_tasks += 1
            ftts_trenching_status = "Uploaded"
        if bool(ftts_duct_installation) is False:
            ftts_duct_installation_status = "Not Uploaded"
        else:
            completed_tasks += 1
            ftts_duct_installation_status = "Uploaded"
        if bool(ftts_cable_installation) is False:
            ftts_cable_installation_status = "Not Uploaded"
        else:
            completed_tasks += 1
            ftts_cable_installation_status = "Uploaded"
        if bool(ftts_manhole_installation) is False:
            ftts_manhole_installation_status = "Not Uploaded"
        else:
            completed_tasks += 1
            ftts_manhole_installation_status = "Uploaded"
        civil_percentage = percentage_function(completed_tasks, automatic_total_tasks)
        return Response({'no_of_tasks': automatic_total_tasks, 'ftts_trenching_status': ftts_trenching_status, 'ftts_duct_installation_status': ftts_duct_installation_status,
         'ftts_cable_installation_status': ftts_cable_installation_status, 'ftts_manhole_installation_status': ftts_manhole_installation_status, 'progress': civil_percentage})


class FttsInstallationProgressView(APIView):

    def get(self, request, pk):
        total_tasks = 3 #HARDCODED WILL LEAVE HERE FOR CONFIMATION WHEN TESTING.
        try:
            category = Category.objects.get(category_name='Installation Team Tasks')
            category_id = category.id
        except Exception as e:
            return Response({'error': 'Installation Team does not exist'})
        automatic_total_tasks = FttsTask.objects.filter(category_name=category_id).count()
        completed_tasks = 0
        ftts_terminal_in_hse_status = ''
        ftts_interception_status = ''
        ftts_integration_status = ''
        site_id = pk
        try:
            progress_object = FttsInstallationTeam.objects.get(site_name=site_id)
        except Exception as e:
            return Response({'error': 'Task not started', 'no_of_tasks': automatic_total_tasks,})
        ftts_terminal_in_hse = progress_object.ftts_terminal_in_hse
        ftts_interception = progress_object.ftts_interception
        ftts_integration = progress_object.ftts_integration
        if bool(ftts_terminal_in_hse) is False:
            ftts_terminal_in_hse_status = "Not uploaded"
        else:
            completed_tasks += 1
            ftts_terminal_in_hse_status = "Uploaded"
        if bool(ftts_interception) is False:
            ftts_interception_status = "Not Uploaded"
        else:
            completed_tasks += 1
            ftts_interception_status = "Uploaded"
        if bool(ftts_integration) is False:
            ftts_integration_status = "Not Uploaded"
        else:
            completed_tasks += 1
            ftts_integration_status = "Uploaded"
        installation_percentage = percentage_function(completed_tasks, automatic_total_tasks)
        return Response({'no_of_tasks': automatic_total_tasks, 'ftts_terminal_in_hse_status': ftts_terminal_in_hse_status, 'ftts_interception_status': ftts_interception_status, 'ftts_integration_status': ftts_integration_status,'progress': installation_percentage})


"""END OF TEAM PROGRESS"""


"""VIEWS TO CALCULATE PROGRESS OF TASKS"""


"""CIVIL TEAM TASKS"""


class FttsCivilTeamProgressView(APIView):

    def get(self, request, pk):
        total_tasks = 4
        try:
            task = FiberTask.objects.get(task_name='Civil Team')
            task_id = task.id
        except Exception as e:
            return Response({'error': 'Civil Team Task does not exist'})
        automatic_total_tasks = FttsSubTask.objects.filter(task_name=task_id).count()
        completed_tasks = 0
        ftts_trenching_status = ''
        ftts_duct_installation_status = ''
        ftts_manhole_installation_status = ''
        ftts_cable_installation_status = ''
        site_id = pk
        try:
            progress_object = FttsCivilTeam.objects.get(site_name=site_id)
        except Exception as e:
            return Response({'error': 'Task not started', 'no_of_tasks': automatic_total_tasks,})
        ftts_trenching = progress_object.ftts_trenching
        ftts_duct_installation = progress_object.ftts_duct_installation
        ftts_manhole_installation = progress_object.ftts_manhole_installation
        ftts_cable_installation = progress_object.ftts_cable_installation
        if bool(ftts_trenching) is False:
            ftts_trenching_status = "Not uploaded"
        else:
            completed_tasks += 1
            ftts_trenching_status = "Uploaded"
        if bool(ftts_duct_installation) is False:
            ftts_duct_installation_status = "Not Uploaded"
        else:
            completed_tasks += 1
            ftts_duct_installation_status = "Uploaded"
        if bool(ftts_manhole_installation) is False:
            ftts_manhole_installation_status = "Not Uploaded"
        else:
            completed_tasks += 1
            ftts_manhole_installation_status = "Uploaded"
        if bool(ftts_cable_installation) is False:
            ftts_cable_installation_status = "Not Uploaded"
        else:
            completed_tasks += 1
            ftts_cable_installation_status = "Uploaded"
        civilteam_percentage = percentage_function(completed_tasks, automatic_total_tasks)
        return Response({'no_of_tasks': automatic_total_tasks, 'ftts_trenching_status': ftts_trenching_status, 'ftts_duct_installation_status': ftts_duct_installation_status, 'ftts_manhole_installation_status': ftts_manhole_installation_status, 'ftts_cable_installation_status': ftts_cable_installation_status,'progress': civilteam_percentage})

"""END OF CIVIL TASKS"""


"""INSTALLATION TEAM TASKS"""


class FttsInstallationTeamProgressView(APIView):

    def get(self, request, pk):
        total_tasks = 3
        try:
            task = FiberTask.objects.get(task_name='Installation Team')
            task_id = task.id
        except Exception as e:
            return Response({'error': 'Electrical Tasks does not exist'})
        automatic_total_tasks = FttsSubTask.objects.filter(task_name=task_id).count()
        completed_tasks = 0
        ftts_terminal_in_hse_status = ''
        ftts_interception_status = ''
        ftts_integration_status = ''
        site_id = pk
        try:
            progress_object = ElectricalTask.objects.get(site_name=site_id)
        except Exception as e:
            return Response({'error': 'Task not started', 'no_of_tasks': automatic_total_tasks,})
        ftts_terminal_in_hse = progress_object.ftts_terminal_in_hse
        ftts_interception = progress_object.ftts_interception
        ftts_integration = progress_object.ftts_integration
        if bool(ftts_terminal_in_hse) is False:
            ftts_terminal_in_hse_status = "Not uploaded"
        else:
            completed_tasks += 1
            ftts_terminal_in_hse_status = "Uploaded"
        if bool(ftts_interception) is False:
            ftts_interception_status = "Not Uploaded"
        else:
            completed_tasks += 1
            ftts_interception_status = "Uploaded"
        if bool(ftts_integration) is False:
            ftts_integration_status = "Not Uploaded"
        else:
            completed_tasks += 1
            ftts_integration_status = "Uploaded"
        installationteam_percentage = percentage_function(completed_tasks, automatic_total_tasks)
        return Response({'no_of_tasks': automatic_total_tasks, 'ftts_terminal_in_hse_status': ftts_terminal_in_hse_status, 'ftts_interception_status': ftts_interception_status, 'ftts_integration_status': ftts_integration_status, 'progress': installationteam_percentage})


"""END OF INSTALLATION TASKS"""


def percentage_function(no_of_complete, total_task):
    """Function to return perecentage of progress  """
    percentage = round(((no_of_complete/total_task) * 100))
    return percentage

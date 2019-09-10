from rest_framework.views import APIView
from erp_ftth.models import *
from rest_framework.response import Response

"""GET PROJECT PROGRESS"""


class FtthProjectProgressView(APIView):

    def get(self, request, pk):

                # PROGRESS FOR SURVEYTEAM
        try:
            category = Category.objects.get(category_name='FTTH Survey Team')
            category_id = category.id
            automatic_total_comtasks = FtthTask.objects.filter(category_name=category_id).count()
            completed_ctasks = 0
            project_id = self.id
            progress_object = ftthSurvey.objects.get(project_name=project_id)
            ftth_interception_point = progress_object.ftth_interception_point
            site_latitude = progress_object.site_latitude
            site_longitude = progress_object.site_longitude
            distance_from_ip = progress_object.distance_from_ip
            no_of_fdts = progress_object.no_of_fdts
            survey_photos = progress_object.survey_photos
            high_level_design = progress_object.high_level_design
            county = progress_object.county
            if bool(ftth_interception_point) is False:
                completed_ctasks += 0
            else:
                completed_ctasks += 1
            if bool(site_latitude) is False:
                completed_ctasks += 0
            else:
                completed_ctasks += 1
            if bool(site_longitude) is False:
                completed_ctasks += 0
            else:
                completed_ctasks += 1
            if bool(distance_from_ip) is False:
                completed_ctasks += 0
            else:
                completed_ctasks += 1
            if bool(no_of_fdts) is False:
                completed_ctasks += 0
            else:
                completed_ctasks += 1
            if bool(survey_photos) is False:
                completed_ctasks += 0
            else:
                completed_ctasks += 1
            if bool(high_level_design) is False:
                completed_ctasks += 0
            else:
                completed_ctasks += 1
            if bool(county) is False:
                completed_ctasks += 0
            else:
                completed_ctasks += 1

            survey_percentage = ftth_percentage_function(completed_ctasks, automatic_total_comtasks)
        except Exception as e:
            survey_percentage = 0

        # PROGRESS FOR COMMERCIALTEAM
        try:
            category = Category.objects.get(category_name='FTTH Commercial Team')
            category_id = category.id
            automatic_total_comtasks = FtthTask.objects.filter(category_name=category_id).count()
            completed_ctasks = 0
            project_id = self.id
            progress_object = FtthCommercialTeam.objects.get(project_name=project_id)
            ftth_po = progress_object.ftth_po
            ftth_boq = progress_object.ftth_boq
            ftth_quote = progress_object.ftth_quote
            ftth_wayleave_application = progress_object.ftth_wayleave_application
            if bool(ftth_po) is False:
                completed_ctasks += 0
            else:
                completed_ctasks += 1
            if bool(ftth_boq) is False:
                completed_ctasks += 0
            else:
                completed_ctasks += 1
            if bool(ftth_quote) is False:
                completed_ctasks += 0
            else:
                completed_ctasks += 1
            if bool(ftth_wayleave_application) is False:
                completed_ctasks += 0
            else:
                completed_ctasks += 1
            commercial_percentage = ftts_percentage_function(completed_ctasks, automatic_total_comtasks)
        except Exception as e:
            commercial_percentage = 0

        # PROGRESS FOR PROCUREMENTTEAM
        try:
            category = Category.objects.get(category_name='FTTH Procurement Team')
            category_id = category.id
            automatic_total_protasks = FttsTask.objects.filter(category_name=category_id).count()
            completed_ptasks = 0
            project_id = self.id
            progress_object = FtthProcurementTeam.objects.get(project_name=project_id)
            ftth_bom = progress_object.ftth_bom
            po_to_supplier = progress_object.po_to_supplier
            ftth_initial_invoice = progress_object.ftth_initial_invoice
            if bool(ftth_bom) is False:
                completed_ptasks += 0
            else:
                completed_ptasks += 1
            if bool(po_to_supplier) is False:
                completed_ptasks += 0
            else:
                completed_ptasks += 1
            if bool(ftth_initial_invoice) is False:
                completed_ptasks += 0
            else:
                completed_ptasks += 1
            procurement_percentage = percentage_function(completed_ptasks, automatic_total_protasks)
        except Exception as e:
            procurement_percentage = 0

        #PROGRESS FOR CIVIL TEAM
        try:
            category = Category.objects.get(category_name='FTTH Civil Team')
            category_id = category.id
            automatic_total_civtasks = FtthTask.objects.filter(category_name=category_id).count()
            completed_cltasks = 0
            project_id = self.id
            progress_object = FtthCivilTeam.objects.get(project_name=project_id)
            ftth_pole_installation = progress_object.ftth_pole_installation
            ftth_trenching = progress_object.ftth_trenching
            ftth_backfiling = progress_object.ftth_backfiling
            ftth_cable_installation = progress_object.ftth_cable_installation
            if bool(ftth_pole_installation) is False:
                completed_cltasks += 0
            else:
                completed_cltasks += 1
            if bool(ftth_trenching) is False:
                completed_cltasks += 0
            else:
                completed_cltasks += 1
            if bool(ftth_backfiling) is False:
                completed_cltasks += 0
            else:
                completed_cltasks += 1
            if bool(ftth_cable_installation) is False:
                completed_cltasks += 0
            else:
                completed_cltasks += 1
            civil_percentage = percentage_function(completed_cltasks, automatic_total_civtasks)
        except Exception as e:
            civil_percentage = 0

        #PROGRESS FOR INSTALLATION TEAM
        try:
            category = Category.objects.get(category_name='FTTH Installation Team')
            category_id = category.id
            automatic_total_instasks = FtthTask.objects.filter(category_name=category_id).count()
            completed_intasks = 0
            project_id = self.id
            progress_object = FtthInstallationTeam.objects.get(project_name=project_id)
            ftth_splicing = progress_object.ftth_splicing
            ftth_signal_testing = progress_object.ftth_signal_testing
            ftts_integration = progress_object.ftts_integration
            ftth_asbuit_received = progress_object.ftth_asbuit_received
            ftth_network_activation = progress_object.ftth_network_activation
            if bool(ftth_splicing) is False:
                completed_intasks += 0
            else:
                completed_intasks += 1
            if bool(ftth_signal_testing) is False:
                completed_intasks += 0
            else:
                completed_intasks += 1
            if bool(ftts_integration) is False:
                completed_intasks += 0
            else:
                completed_intasks += 1
            if bool(ftth_asbuit_received) is False:
                completed_intasks += 0
            else:
                completed_intasks += 1
            if bool(ftth_network_activation) is False:
                completed_intasks += 0
            else:
                completed_intasks += 1
            installation_percentage = percentage_function(completed_intasks, automatic_total_instasks)
        except Exception as e:
            installation_percentage = 0

        project_percentage = ((survey_percentage + commercial_percentage + civil_percentage + procurement_percentage + installation_percentage )/4)

        return Response({'progress': project_percentage, 'project_id': pk})


"""END OF PROJECT PROGRESS"""

"""VIEWS TO CALCULATE PROGRESS OF TEAMS/CATEGORIES"""

class FtthSurveyTeamProgressView(APIView):

    def get(self, request, pk):
        total_tasks = 8 #HARDCODED WILL LEAVE HERE FOR CONFIMATION WHEN TESTING.
        try:
            category = Category.objects.get(category_name='FTTH Survey Team')
            category_id = category.id
        except Exception as e:
            return Response({'error': 'FTTH Survey Team does not exist'})
        automatic_total_tasks = FtthTask.objects.filter(category_name=category_id).count()
        completed_tasks = 0
        Ip_status = ''
        latitude_status = ''
        logitude_status = ''
        distance_from_ip_status = ''
        survey_photos_status = ''
        high_level_design_status = ''
        county_status = ''
        project_id = pk
        try:
            progress_object = ftthSurvey.objects.get(project_name=project_id)
        except Exception as e:
            return Response({'error': 'Task not started', 'no_of_tasks': automatic_total_tasks,})
        ftth_interception_point = progress_object.ftth_interception_point
        site_latitude = progress_object.site_latitude
        site_longitude = progress_object.site_longitude
        distance_from_ip = progress_object.distance_from_ip
        no_of_fdts = progress_object.no_of_fdts
        survey_photos = progress_object.survey_photos
        high_level_design = progress_object.high_level_design
        county = progress_object.county
        if bool(ftth_interception_point) is False:
            Ip_status = "Not uploaded"
        else:
            completed_tasks += 1
            Ip_status = "Uploaded"
        if bool(site_latitude) is False:
            latitude_status = "Not Uploaded"
        else:
            completed_tasks += 1
            latitude_status = "Uploaded"
        if bool(site_longitude) is False:
            logitude_status = "Not Uploaded"
        else:
            completed_tasks += 1
            logitude_status = "Uploaded"
        if bool(distance_from_ip) is False:
            distance_from_ip_status = "Not uploaded"
        else:
            completed_tasks += 1
            distance_from_ip_status = "Uploaded"
        if bool(survey_photos) is False:
            survey_photos_status = "Not Uploaded"
        else:
            completed_tasks += 1
            survey_photos_status = "Uploaded"
        if bool(high_level_design) is False:
            high_level_design_status = "Not Uploaded"
        else:
            completed_tasks += 1
            high_level_design_status = "Uploaded"
        if bool(county) is False:
            county_status = "Not Uploaded"
        else:
            completed_tasks += 1
            county_status = "Uploaded"
        survey_percentage = percentage_function(completed_tasks, automatic_total_tasks)
        return Response({'no_of_tasks': automatic_total_tasks,'Ip_status': Ip_status, 'latitude_status':latitude_status, 'logitude_status': logitude_status, 'distance_from_ip_status': distance_from_ip_status, 'no_of_fdts':no_of_fdts,
         'survey_photos_status': survey_photos_status, 'high_level_design_status': high_level_design_status, 'county_status': county_status,'progress': survey_percentage})


class FtthCommercialTeamProgressView(APIView):

    def get(self, request, pk):
        total_tasks = 6 #HARDCODED WILL LEAVE HERE FOR CONFIMATION WHEN TESTING.
        try:
            category = Category.objects.get(category_name='FTTH Commercial Team')
            category_id = category.id
        except Exception as e:
            return Response({'error': 'FTTH Commercial Team does not exist'})
        automatic_total_tasks = FtthTask.objects.filter(category_name=category_id).count()
        completed_tasks = 0
        ftth_po_status = ''
        ftth_po_no_status = ''
        ftth_po_amount_status = ''
        ftth_boq_status = ''
        ftth_quote_status = ''
        ftth_wayleave_application_status = ''
        project_id = pk
        try:
            progress_object = FtthCommercialTeam.objects.get(project_name=project_id)
        except Exception as e:
            return Response({'error': 'Task not started', 'no_of_tasks': automatic_total_tasks,})
        ftth_po = progress_object.ftth_po
        ftth_po_no = progress_object.ftth_po_no
        ftth_po_amount = progress_object.ftth_po_amount
        ftth_boq = progress_object.ftth_boq
        ftth_quote = progress_object.ftth_quote
        ftth_wayleave_application = progress_object.ftth_wayleave_application
        if bool(ftth_po) is False:
            ftth_po_status = "Not uploaded"
        else:
            completed_tasks += 1
            ftth_po_status = "Uploaded"
        if bool(ftth_po_no) is False:
            ftth_po_no_status = "Not Uploaded"
        else:
            completed_tasks += 1
            ftth_po_no_status = "Uploaded"
        if bool(ftth_po_amount) is False:
            ftth_po_amount_status = "Not Uploaded"
        else:
            completed_tasks += 1
            ftth_po_amount_status = "Uploaded"
        if bool(ftth_boq) is False:
            ftth_boq_status = "Not uploaded"
        else:
            completed_tasks += 1
            ftth_boq_status = "Uploaded"
        if bool(ftth_quote) is False:
            ftth_quote_status = "Not Uploaded"
        else:
            completed_tasks += 1
            ftth_quote_status = "Uploaded"
        if bool(ftth_wayleave_application) is False:
            ftth_wayleave_application_status = "Not Uploaded"
        else:
            completed_tasks += 1
            ftth_wayleave_application_status = "Uploaded"
        commercial_percentage = percentage_function(completed_tasks, automatic_total_tasks)
        return Response({'no_of_tasks': automatic_total_tasks,'ftth_po_status': ftth_po_status,'ftth_po_no_status': ftth_po_no_status, 'ftth_po_amount_status': ftth_po_amount_status, 'ftth_boq_status': ftth_boq_status,
         'ftth_wayleave_application_status': ftth_wayleave_application_status, 'progress': commercial_percentage})


class FtthProcurementTeamProgressView(APIView):

    def get(self, request, pk):
        total_tasks = 7 #HARDCODED WILL LEAVE HERE FOR CONFIMATION WHEN TESTING.
        try:
            category = Category.objects.get(category_name='FTTH Procurement Team')
            category_id = category.id
        except Exception as e:
            return Response({'error': 'FTTH Procurement Team does not exist'})
        automatic_total_tasks = FtthTask.objects.filter(category_name=category_id).count()
        completed_tasks = 0
        ftth_bom_status = ''
        po_to_supplier_status = ''
        ftth_initial_invoice_status = ''
        project_id = pk
        try:
            progress_object = FtthProcurementTeam.objects.get(project_name=project_id)
        except Exception as e:
            return Response({'error': 'Task not started', 'no_of_tasks': automatic_total_tasks,})
        ftth_bom = progress_object.ftth_bom
        po_to_supplier = progress_object.po_to_supplier
        ftth_initial_invoice = progress_object.ftth_initial_invoice
        if bool(ftth_bom) is False:
            ftth_bom_status = "Not uploaded"
        else:
            completed_tasks += 1
            ftth_bom_status = "Uploaded"
        if bool(po_to_supplier) is False:
            po_to_supplier_status = "Not Uploaded"
        else:
            completed_tasks += 1
            po_to_supplier_status = "Uploaded"
        if bool(ftth_initial_invoice) is False:
            ftth_initial_invoice_status = "Not Uploaded"
        else:
            completed_tasks += 1
            ftth_initial_invoice_status = "Uploaded"
        procurement_percentage = percentage_function(completed_tasks, automatic_total_tasks)
        return Response({'no_of_tasks': automatic_total_tasks, 'ftth_bom_status': ftth_bom_status, 'po_to_supplier_status': po_to_supplier_status,
        'ftth_initial_invoice_status': ftth_initial_invoice_status, 'progress': procurement_percentage})


class FtthCivilTeamProgressView(APIView):

    def get(self, request, pk):
        total_tasks = 4 #HARDCODED WILL LEAVE HERE FOR CONFIMATION WHEN TESTING.
        try:
            category = Category.objects.get(category_name='FTTH Civil Team Tasks')
            category_id = category.id
        except Exception as e:
            return Response({'error': 'FTTH Civil Team does not exist'})
        automatic_total_tasks = FtthTask.objects.filter(category_name=category_id).count()
        completed_tasks = 0
        ftth_pole_installation_status = ''
        ftth_trenching_status = ''
        ftth_backfiling_status = ''
        ftth_cable_installation_status = ''
        project_id = pk
        try:
            progress_object = FtthCivilTeam.objects.get(project_name=project_id)
        except Exception as e:
            return Response({'error': 'Task not started', 'no_of_tasks': automatic_total_tasks,})
        ftth_pole_installation = progress_object.ftth_pole_installation
        ftth_trenching = progress_object.ftth_trenching
        ftth_backfiling = progress_object.ftth_backfiling
        ftth_cable_installation = progress_object.ftth_cable_installation
        if bool(ftth_pole_installation) is False:
            ftth_pole_installation_status = "Not uploaded"
        else:
            completed_tasks += 1
            ftth_pole_installation_status = "Uploaded"
        if bool(ftth_trenching) is False:
            ftth_trenching_status = "Not Uploaded"
        else:
            completed_tasks += 1
            ftth_trenching_status = "Uploaded"
        if bool(ftth_backfiling) is False:
            ftth_backfiling_status = "Not Uploaded"
        else:
            completed_tasks += 1
            ftth_backfiling_status = "Uploaded"
        if bool(ftth_cable_installation) is False:
            ftth_cable_installation_status = "Not Uploaded"
        else:
            completed_tasks += 1
            ftth_cable_installation_status = "Uploaded"
        civil_percentage = percentage_function(completed_tasks, automatic_total_tasks)
        return Response({'no_of_tasks': automatic_total_tasks, 'ftth_pole_installation_status': ftth_pole_installation_status, 'ftth_trenching_status': ftth_trenching_status,
         'ftth_backfiling_status': ftth_backfiling_status, 'ftth_cable_installation_status': ftth_cable_installation_status, 'progress': civil_percentage})


class FtthInstallationTeamProgressView(APIView):

    def get(self, request, pk):
        total_tasks = 5 #HARDCODED WILL LEAVE HERE FOR CONFIMATION WHEN TESTING.
        try:
            category = Category.objects.get(category_name='Installation Team Tasks')
            category_id = category.id
        except Exception as e:
            return Response({'error': 'Installation Team does not exist'})
        automatic_total_tasks = FtthTask.objects.filter(category_name=category_id).count()
        completed_tasks = 0
        ftth_splicing_status = ''
        ftth_signal_testing_status = ''
        ftth_issues_status = ''
        ftth_asbuit_received_status = ''
        ftth_network_activation_status = ''
        project_id = pk
        try:
            progress_object = FtthInstallationTeam.objects.get(project_name=project_id)
        except Exception as e:
            return Response({'error': 'Task not started', 'no_of_tasks': automatic_total_tasks,})
        ftth_splicing = progress_object.ftth_splicing
        ftth_signal_testing = progress_object.ftth_signal_testing
        ftth_issues = progress_object.ftth_issues
        ftth_asbuit_received = progress_object.ftth_asbuit_received
        ftth_network_activation = progress_object.ftth_network_activation
        if bool(ftth_splicing) is False:
            ftth_splicing_status = "Not uploaded"
        else:
            completed_tasks += 1
            ftth_splicing_status = "Uploaded"
        if bool(ftth_signal_testing) is False:
            ftth_signal_testing_status = "Not Uploaded"
        else:
            completed_tasks += 1
            ftth_signal_testing_status = "Uploaded"
        if bool(ftth_issues) is False:
            ftth_issues_status = "Not Uploaded"
        else:
            completed_tasks += 1
            ftth_issues_status = "Uploaded"
        if bool(ftth_asbuit_received) is False:
            ftth_asbuit_received_status = "Not Uploaded"
        else:
            completed_tasks += 1
            ftth_asbuit_received_status = "Uploaded"
        if bool(ftth_network_activation) is False:
            ftth_network_activation_status = "Not Uploaded"
        else:
            completed_tasks += 1
            ftth_network_activation_status = "Uploaded"
        installation_percentage = percentage_function(completed_tasks, automatic_total_tasks)
        return Response({'no_of_tasks': automatic_total_tasks, 'ftth_splicing_status': ftth_splicing_status, 'ftth_signal_testing_status': ftth_signal_testing_status, 'ftth_issues_status': ftth_issues_status,
         'ftth_asbuit_received_status': ftth_asbuit_received_status, 'ftth_network_activation_status': ftth_network_activation_status,'progress': installation_percentage})


"""END OF TEAM PROGRESS"""

"""VIEWS TO CALCULATE PROGRESS OF TASKS"""


"""INSTALLATION TEAM TASKS"""


class FtthSplicingProgressView(APIView):

    def get(self, request, pk):
        total_tasks = 3
        try:
            task = FtthTask.objects.get(task_name='FTTH Splicing Tasks')
            task_id = task.id
        except Exception as e:
            return Response({'error': 'FTTH Splicing Tasks does not exist'})
        automatic_total_tasks = FtthSubTask.objects.filter(task_name=task_id).count()
        completed_tasks = 0
        ftth_splicing_encore_status = ''
        ftth_splicing_fat_status = ''
        ftth_splicing_fdt_status = ''
        project_id = pk
        try:
            progress_object = FtthSplicing.objects.get(project_name=project_id)
        except Exception as e:
            return Response({'error': 'Task not started', 'no_of_tasks': automatic_total_tasks,})
        ftth_splicing_encore = progress_object.ftth_splicing_encore
        ftth_splicing_fat = progress_object.ftth_splicing_fat
        ftth_splicing_fdt = progress_object.ftth_splicing_fdt
        if bool(ftth_splicing_encore) is False:
            ftth_splicing_encore_status = "Not uploaded"
        else:
            completed_tasks += 1
            ftth_splicing_encore_status = "Uploaded"
        if bool(ftth_splicing_fat) is False:
            ftth_splicing_fat_status = "Not Uploaded"
        else:
            completed_tasks += 1
            ftth_splicing_fat_status = "Uploaded"
        if bool(ftth_splicing_fdt) is False:
            ftth_splicing_fdt_status = "Not Uploaded"
        else:
            completed_tasks += 1
            ftth_splicing_fdt_status = "Uploaded"
        splicing_percentage = percentage_function(completed_tasks, automatic_total_tasks)
        return Response({'no_of_tasks': automatic_total_tasks, 'ftth_splicing_encore_status': ftth_splicing_encore_status, 'ftth_splicing_fat_status': ftth_splicing_fat_status,
        'ftth_splicing_fdt_status': ftth_splicing_fdt_status,'progress': splicing_percentage})

class FtthSignalTestingProgressView(APIView):

    def get(self, request, pk):
        total_tasks = 3
        try:
            task = FtthTask.objects.get(task_name='FTTH Signal Testing Task')
            task_id = task.id
        except Exception as e:
            return Response({'error': 'FTTH Signal Testing Task does not exist'})
        automatic_total_tasks = FtthSubTask.objects.filter(task_name=task_id).count()
        completed_tasks = 0
        ftth_core_provision_status = ''
        ftth_power_levels_status = ''
        ftth_otdr_traces_status = ''
        project_id = pk
        try:
            progress_object = FoundationTask.objects.get(project_name=project_id)
        except Exception as e:
            return Response({'error': 'Task not started', 'no_of_tasks': automatic_total_tasks,})
        ftth_core_provision = progress_object.ftth_core_provision
        ftth_power_levels = progress_object.ftth_power_levels
        ftth_otdr_traces = progress_object.ftth_otdr_traces
        if bool(ftth_core_provision) is False:
            ftth_core_provision_status = "Not uploaded"
        else:
            completed_tasks += 1
            ftth_core_provision_status = "Uploaded"
        if bool(ftth_power_levels) is False:
            ftth_power_levels_status = "Not Uploaded"
        else:
            completed_tasks += 1
            ftth_power_levels_status = "Uploaded"
        if bool(ftth_otdr_traces) is False:
            ftth_otdr_traces_status = "Not Uploaded"
        else:
            completed_tasks += 1
            ftth_otdr_traces_status = "Uploaded"
        signal_testing_percentage = percentage_function(completed_tasks, automatic_total_tasks)
        return Response({'no_of_tasks': automatic_total_tasks, 'ftth_core_provision_status': ftth_core_provision_status, 'ftth_power_levels_status': ftth_power_levels_status,
        'ftth_otdr_traces_status': ftth_otdr_traces_status,'progress': signal_testing_percentage})

"""END OF INSTALLATION TASKS"""

def percentage_function(no_of_complete, total_task):
    """Function to return perecentage of progress  """
    percentage = round(((no_of_complete/total_task) * 100))
    return percentage

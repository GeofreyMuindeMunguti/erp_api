from rest_framework.views import APIView
from erp_ftth.models import *
from rest_framework.response import Response

"""GET PROJECT PROGRESS"""


class FttsProjectProgressView(APIView):

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

#
# """END OF PROJECT PROGRESS"""
#
# """VIEWS TO CALCULATE PROGRESS OF TEAMS/CATEGORIES"""
#
# class FttsSurveyTeamProgressView(APIView):
#
#     def get(self, request, pk):
#         total_tasks = 7 #HARDCODED WILL LEAVE HERE FOR CONFIMATION WHEN TESTING.
#         try:
#             category = Category.objects.get(category_name='FTTS Survey Team')
#             category_id = category.id
#         except Exception as e:
#             return Response({'error': 'FTTS Survey Team does not exist'})
#         automatic_total_tasks = FttsTask.objects.filter(category_name=category_id).count()
#         completed_tasks = 0
#         Ip_status = ''
#         latitude_status = ''
#         logitude_status = ''
#         distance_from_ip_status = ''
#         survey_photos_status = ''
#         high_level_design_status = ''
#         county_status = ''
#         site_id = pk
#         try:
#             progress_object = FttsCommercialTeam.objects.get(site_name=site_id)
#         except Exception as e:
#             return Response({'error': 'Task not started', 'no_of_tasks': automatic_total_tasks,})
#         ftts_interception_point = progress_object.ftts_interception_point
#         site_latitude = progress_object.site_latitude
#         site_longitude = progress_object.site_longitude
#         distance_from_ip = progress_object.distance_from_ip
#         survey_photos = progress_object.survey_photos
#         high_level_design = progress_object.high_level_design
#         county = progress_object.county
#         if bool(ftts_interception_point) is False:
#             Ip_status = "Not uploaded"
#         else:
#             completed_tasks += 1
#             Ip_status = "Uploaded"
#         if bool(site_latitude) is False:
#             latitude_status = "Not Uploaded"
#         else:
#             completed_tasks += 1
#             latitude_status = "Uploaded"
#         if bool(site_longitude) is False:
#             logitude_status = "Not Uploaded"
#         else:
#             completed_tasks += 1
#             logitude_status = "Uploaded"
#         if bool(distance_from_ip) is False:
#             distance_from_ip_status = "Not uploaded"
#         else:
#             completed_tasks += 1
#             distance_from_ip_status = "Uploaded"
#         if bool(survey_photos) is False:
#             survey_photos_status = "Not Uploaded"
#         else:
#             completed_tasks += 1
#             survey_photos_status = "Uploaded"
#         if bool(high_level_design) is False:
#             high_level_design_status = "Not Uploaded"
#         else:
#             completed_tasks += 1
#             high_level_design_status = "Uploaded"
#         if bool(county) is False:
#             county_status = "Not Uploaded"
#         else:
#             completed_tasks += 1
#             county_status = "Uploaded"
#         survey_percentage = percentage_function(completed_tasks, automatic_total_tasks)
#         return Response({'no_of_tasks': automatic_total_tasks,'Ip_status': Ip_status, 'latitude_status':latitude_status, 'logitude_status': logitude_status, 'distance_from_ip_status': distance_from_ip_status,
#          'survey_photos_status': survey_photos_status, 'high_level_design_status': high_level_design_status, 'county_status': county_status,'progress': survey_percentage})
#
#
# class FttsCommercialTeamProgressView(APIView):
#
#     def get(self, request, pk):
#         total_tasks = 7 #HARDCODED WILL LEAVE HERE FOR CONFIMATION WHEN TESTING.
#         try:
#             category = Category.objects.get(category_name='FTTS Commercial Team')
#             category_id = category.id
#         except Exception as e:
#             return Response({'error': 'FTTS Commercial Team does not exist'})
#         automatic_total_tasks = FttsTask.objects.filter(category_name=category_id).count()
#         completed_tasks = 0
#         ftts_quote_status = ''
#         ftts_po_data_status = ''
#         ftts_initial_invoice_status = ''
#         site_id = pk
#         try:
#             progress_object = FttsCommercialTeam.objects.get(site_name=site_id)
#         except Exception as e:
#             return Response({'error': 'Task not started', 'no_of_tasks': automatic_total_tasks,})
#         ftts_quote = progress_object.ftts_quote
#         ftts_po_data = progress_object.ftts_po_data
#         ftts_initial_invoice = progress_object.ftts_initial_invoice
#         if bool(ftts_quote) is False:
#             ftts_quote_status = "Not uploaded"
#         else:
#             completed_tasks += 1
#             ftts_quote_status = "Uploaded"
#         if bool(ftts_po_data) is False:
#             ftts_po_data_status = "Not Uploaded"
#         else:
#             completed_tasks += 1
#             ftts_po_data_status = "Uploaded"
#         if bool(ftts_initial_invoice) is False:
#             ftts_initial_invoice_status = "Not Uploaded"
#         else:
#             completed_tasks += 1
#             ftts_initial_invoice_status = "Uploaded"
#         commercial_percentage = percentage_function(completed_tasks, automatic_total_tasks)
#         return Response({'no_of_tasks': automatic_total_tasks,'ftts_quote_status': ftts_quote_status,
#          'ftts_po_data_status': ftts_po_data_status, 'ftts_initial_invoice_status': ftts_initial_invoice_status, 'progress': commercial_percentage})
#
#
# class FttsProcurementProgressTeamView(APIView):
#
#     def get(self, request, pk):
#         total_tasks = 3 #HARDCODED WILL LEAVE HERE FOR CONFIMATION WHEN TESTING.
#         try:
#             category = Category.objects.get(category_name='FTTS Procurement Team')
#             category_id = category.id
#         except Exception as e:
#             return Response({'error': 'FTTS Procurement Team does not exist'})
#         automatic_total_tasks = FttsTask.objects.filter(category_name=category_id).count()
#         completed_tasks = 0
#         site_material_requisition_status = ''
#         site_po_subcontractors_status = ''
#         po_subcontractors_status = ''
#         site_id = pk
#         try:
#             progress_object = FttsProcurementTeam.objects.get(site_name=site_id)
#         except Exception as e:
#             return Response({'error': 'Task not started', 'no_of_tasks': automatic_total_tasks,})
#         site_material_requisition = progress_object.ftts_material_requisition
#         site_po_subcontractors = progress_object.ftts_po_subcontractors
#         ftts_po_quote_serviceno = progress_object.ftts_po_quote_serviceno
#         if bool(site_material_requisition) is False:
#             site_material_requisition_status = "Not uploaded"
#         else:
#             completed_tasks += 1
#             site_material_requisition_status = "Uploaded"
#         if bool(site_po_subcontractors) is False:
#             site_po_subcontractors_status = "Not Uploaded"
#         else:
#             completed_tasks += 1
#             site_po_subcontractors_status = "Uploaded"
#         if bool(ftts_po_quote_serviceno) is False:
#             ftts_po_quote_serviceno_status = "Not Uploaded"
#         else:
#             completed_tasks += 1
#             ftts_po_quote_serviceno_status = "Uploaded"
#         procurement_percentage = percentage_function(completed_tasks, automatic_total_tasks)
#         return Response({'no_of_tasks': automatic_total_tasks, 'site_material_requisition_status': site_material_requisition_status, 'site_po_subcontractors_status': site_po_subcontractors_status,
#         'ftts_po_quote_serviceno_status': ftts_po_quote_serviceno_status, 'progress': procurement_percentage})
#
#
# class FttsCivilProgressView(APIView):
#
#     def get(self, request, pk):
#         total_tasks = 4 #HARDCODED WILL LEAVE HERE FOR CONFIMATION WHEN TESTING.
#         try:
#             category = Category.objects.get(category_name='Civil Team Tasks')
#             category_id = category.id
#         except Exception as e:
#             return Response({'error': 'Civil Team does not exist'})
#         automatic_total_tasks = FiberTask.objects.filter(category_name=category_id).count()
#         completed_tasks = 0
#         ftts_trenching_status = ''
#         ftts_duct_installation_status = ''
#         ftts_cable_installation_status = ''
#         ftts_manhole_installation_status = ''
#         site_id = pk
#         try:
#             progress_object = CivilWorksTeam.objects.get(project_name=project_id)
#         except Exception as e:
#             return Response({'error': 'Task not started', 'no_of_tasks': automatic_total_tasks,})
#         ftts_trenching = progress_object.ftts_trenching
#         ftts_duct_installation = progress_object.ftts_duct_installation
#         ftts_cable_installation = progress_object.ftts_cable_installation
#         ftts_manhole_installation = progress_object.ftts_manhole_installation
#         tower_field = progress_object.tower_data
#         if bool(ftts_trenching) is False:
#             ftts_trenching_status = "Not uploaded"
#         else:
#             completed_tasks += 1
#             ftts_trenching_status = "Uploaded"
#         if bool(ftts_duct_installation) is False:
#             ftts_duct_installation_status = "Not Uploaded"
#         else:
#             completed_tasks += 1
#             ftts_duct_installation_status = "Uploaded"
#         if bool(ftts_cable_installation) is False:
#             ftts_cable_installation_status = "Not Uploaded"
#         else:
#             completed_tasks += 1
#             ftts_cable_installation_status = "Uploaded"
#         if bool(ftts_manhole_installation) is False:
#             ftts_manhole_installation_status = "Not Uploaded"
#         else:
#             completed_tasks += 1
#             ftts_manhole_installation_status = "Uploaded"
#         civil_percentage = percentage_function(completed_tasks, automatic_total_tasks)
#         return Response({'no_of_tasks': automatic_total_tasks, 'ftts_trenching_status': ftts_trenching_status, 'ftts_duct_installation_status': ftts_duct_installation_status,
#          'ftts_cable_installation_status': ftts_cable_installation_status, 'ftts_manhole_installation_status': ftts_manhole_installation_status, 'progress': civil_percentage})
#
#
# class FttsInstallationProgressView(APIView):
#
#     def get(self, request, pk):
#         total_tasks = 3 #HARDCODED WILL LEAVE HERE FOR CONFIMATION WHEN TESTING.
#         try:
#             category = Category.objects.get(category_name='Installation Team Tasks')
#             category_id = category.id
#         except Exception as e:
#             return Response({'error': 'Installation Team does not exist'})
#         automatic_total_tasks = FttsTask.objects.filter(category_name=category_id).count()
#         completed_tasks = 0
#         ftts_terminal_in_hse_status = ''
#         ftts_interception_status = ''
#         ftts_integration_status = ''
#         site_id = pk
#         try:
#             progress_object = FttsInstallationTeam.objects.get(site_name=site_id)
#         except Exception as e:
#             return Response({'error': 'Task not started', 'no_of_tasks': automatic_total_tasks,})
#         ftts_terminal_in_hse = progress_object.ftts_terminal_in_hse
#         ftts_interception = progress_object.ftts_interception
#         ftts_integration = progress_object.ftts_integration
#         if bool(ftts_terminal_in_hse) is False:
#             ftts_terminal_in_hse_status = "Not uploaded"
#         else:
#             completed_tasks += 1
#             ftts_terminal_in_hse_status = "Uploaded"
#         if bool(ftts_interception) is False:
#             ftts_interception_status = "Not Uploaded"
#         else:
#             completed_tasks += 1
#             ftts_interception_status = "Uploaded"
#         if bool(ftts_integration) is False:
#             ftts_integration_status = "Not Uploaded"
#         else:
#             completed_tasks += 1
#             ftts_integration_status = "Uploaded"
#         installation_percentage = percentage_function(completed_tasks, automatic_total_tasks)
#         return Response({'no_of_tasks': automatic_total_tasks, 'ftts_terminal_in_hse_status': ftts_terminal_in_hse_status, 'ftts_interception_status': ftts_interception_status, 'ftts_integration_status': ftts_integration_status,'progress': installation_percentage})
#
#
# """END OF TEAM PROGRESS"""
#
#
# """VIEWS TO CALCULATE PROGRESS OF TASKS"""
#
#
# """CIVIL TEAM TASKS"""
#
#
# class FttsCivilTeamProgressView(APIView):
#
#     def get(self, request, pk):
#         total_tasks = 4
#         try:
#             task = FiberTask.objects.get(task_name='Civil Team')
#             task_id = task.id
#         except Exception as e:
#             return Response({'error': 'Civil Team Task does not exist'})
#         automatic_total_tasks = FttsSubTask.objects.filter(task_name=task_id).count()
#         completed_tasks = 0
#         ftts_trenching_status = ''
#         ftts_duct_installation_status = ''
#         ftts_manhole_installation_status = ''
#         ftts_cable_installation_status = ''
#         site_id = pk
#         try:
#             progress_object = FttsCivilTeam.objects.get(site_name=site_id)
#         except Exception as e:
#             return Response({'error': 'Task not started', 'no_of_tasks': automatic_total_tasks,})
#         ftts_trenching = progress_object.ftts_trenching
#         ftts_duct_installation = progress_object.ftts_duct_installation
#         ftts_manhole_installation = progress_object.ftts_manhole_installation
#         ftts_cable_installation = progress_object.ftts_cable_installation
#         if bool(ftts_trenching) is False:
#             ftts_trenching_status = "Not uploaded"
#         else:
#             completed_tasks += 1
#             ftts_trenching_status = "Uploaded"
#         if bool(ftts_duct_installation) is False:
#             ftts_duct_installation_status = "Not Uploaded"
#         else:
#             completed_tasks += 1
#             ftts_duct_installation_status = "Uploaded"
#         if bool(ftts_manhole_installation) is False:
#             ftts_manhole_installation_status = "Not Uploaded"
#         else:
#             completed_tasks += 1
#             ftts_manhole_installation_status = "Uploaded"
#         if bool(ftts_cable_installation) is False:
#             ftts_cable_installation_status = "Not Uploaded"
#         else:
#             completed_tasks += 1
#             ftts_cable_installation_status = "Uploaded"
#         civilteam_percentage = percentage_function(completed_tasks, automatic_total_tasks)
#         return Response({'no_of_tasks': automatic_total_tasks, 'ftts_trenching_status': ftts_trenching_status, 'ftts_duct_installation_status': ftts_duct_installation_status, 'ftts_manhole_installation_status': ftts_manhole_installation_status, 'ftts_cable_installation_status': ftts_cable_installation_status,'progress': civilteam_percentage})
#
# """END OF CIVIL TASKS"""
#
#
# """INSTALLATION TEAM TASKS"""
#
#
# class FttsInstallationTeamProgressView(APIView):
#
#     def get(self, request, pk):
#         total_tasks = 3
#         try:
#             task = FiberTask.objects.get(task_name='Installation Team')
#             task_id = task.id
#         except Exception as e:
#             return Response({'error': 'Electrical Tasks does not exist'})
#         automatic_total_tasks = FttsSubTask.objects.filter(task_name=task_id).count()
#         completed_tasks = 0
#         ftts_terminal_in_hse_status = ''
#         ftts_interception_status = ''
#         ftts_integration_status = ''
#         site_id = pk
#         try:
#             progress_object = ElectricalTask.objects.get(site_name=site_id)
#         except Exception as e:
#             return Response({'error': 'Task not started', 'no_of_tasks': automatic_total_tasks,})
#         ftts_terminal_in_hse = progress_object.ftts_terminal_in_hse
#         ftts_interception = progress_object.ftts_interception
#         ftts_integration = progress_object.ftts_integration
#         if bool(ftts_terminal_in_hse) is False:
#             ftts_terminal_in_hse_status = "Not uploaded"
#         else:
#             completed_tasks += 1
#             ftts_terminal_in_hse_status = "Uploaded"
#         if bool(ftts_interception) is False:
#             ftts_interception_status = "Not Uploaded"
#         else:
#             completed_tasks += 1
#             ftts_interception_status = "Uploaded"
#         if bool(ftts_integration) is False:
#             ftts_integration_status = "Not Uploaded"
#         else:
#             completed_tasks += 1
#             ftts_integration_status = "Uploaded"
#         installationteam_percentage = percentage_function(completed_tasks, automatic_total_tasks)
#         return Response({'no_of_tasks': automatic_total_tasks, 'ftts_terminal_in_hse_status': ftts_terminal_in_hse_status, 'ftts_interception_status': ftts_interception_status, 'ftts_integration_status': ftts_integration_status, 'progress': installationteam_percentage})
#
#
# """END OF INSTALLATION TASKS"""
#
#
# def percentage_function(no_of_complete, total_task):
#     """Function to return perecentage of progress  """
#     percentage = round(((no_of_complete/total_task) * 100))
#     return percentage

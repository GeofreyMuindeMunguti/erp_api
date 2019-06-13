from rest_framework.views import APIView
from .models import *
from rest_framework.response import Response

""" GET TASK STATUS FOR MONITORING"""

"""CURRENTLY CHECKING COMMENT BUT THAT SHOULD BE FILE CHECK"""


class TaskStatusView(APIView):

    def get(self, request):
        total_projects = Project.objects.all().count()
        projects_open = Project.objects.filter(final_acceptance_cert_comment__isnull=True).count()
        projects_closed = Project.objects.filter(final_acceptance_cert_comment__isnull=False).count()
        return Response({'total_projects': total_projects, 'open': projects_open, 'closed': projects_closed, })


class TimesheetSummaryView(APIView):

    def get(self, request):
        total_ca = InstallationTeam.objects.filter(conditional_acceptance_cert_comment__isnull=False).count()
        total_fa = Project.objects.filter(final_acceptance_cert_comment__isnull=False).count()
        total_certs = total_ca + total_fa
        return Response({'total_certs': total_certs, 'CA': total_ca, 'FA': total_fa, })

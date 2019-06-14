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


""" GET NO OF CA AND FA IN SYSTEM FOR MONITORING"""


class TimesheetSummaryView(APIView):

    def get(self, request):
        total_ca = InstallationTeam.objects.filter(conditional_acceptance_cert_comment__isnull=False).count()
        total_fa = Project.objects.filter(final_acceptance_cert_comment__isnull=False).count()
        total_certs = total_ca + total_fa
        return Response({'total_certs': total_certs, 'CA': total_ca, 'FA': total_fa, })


"""GET ISSUE STATUS FOR BOTH A SINGLE PROJECT AND ALL THE PROJECT"""


class IssueStatusView(APIView):

    def get(self, request):
        issues = Issues.objects.all().count()
        issues_closed = Issues.objects.filter(closed=True).count()
        issues_open = Issues.objects.filter(closed=True).count()
        return Response({'total_issues': issues, 'issues_closed': issues_closed, 'issues_open': issues_open, })

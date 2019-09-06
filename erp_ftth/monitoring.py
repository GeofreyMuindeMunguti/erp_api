from rest_framework.views import APIView
from erp_ftth.models import *
from rest_framework.response import Response

""" GET TASK STATUS FOR MONITORING"""

"""CURRENTLY CHECKING COMMENT BUT THAT SHOULD BE FILE CHECK"""


class FtthTaskStatusView(APIView):

    def get(self, request):
        total_projects = FtthCertificates.objects.all().count()
        projects_open = FtthCertificates.objects.filter(ftth_final_acceptance_cert_comment__isnull=True).count()
        projects_closed = total_projects - projects_open
        return Response({'total_projects': total_projects, 'open': projects_open, 'closed': projects_closed, })


""" GET NO OF CA AND FA IN SYSTEM FOR MONITORING"""


class FtthTimesheetSummaryView(APIView):

    def get(self, request):
        ftth_total_ca = FtthCertificates.objects.filter(ftth_conditional_acceptance_cert_comment__isnull=False).count()
        ftth_total_fa = FtthCertificates.objects.filter(ftth_final_acceptance_cert_comment__isnull=False).count()
        ftth_total_certs = ftth_total_ca + ftth_total_fa
        return Response({'ftth_total_certs': ftth_total_certs, 'ftth CA': ftth_total_ca, 'ftth FA': ftth_total_fa, })


"""GET ISSUE STATUS FOR BOTH A SINGLE PROJECT AND ALL THE PROJECT"""


class FtthIssueStatusView(APIView):

    def get(self, request):
        issues = FtthIssues.objects.all().count()
        issues_closed = FtthIssues.objects.filter(closed=True).count()
        issues_open = issues - issues_closed
        return Response({'total_issues': issues, 'issues_closed': issues_closed, 'issues_open': issues_open, })

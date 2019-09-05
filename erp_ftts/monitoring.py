from rest_framework.views import APIView
from .models import *
from rest_framework.response import Response

""" GET TASK STATUS FOR MONITORING"""

"""CURRENTLY CHECKING COMMENT BUT THAT SHOULD BE FILE CHECK"""


class FttsTaskStatusView(APIView):

    def get(self, request):
        total_sites = FttsCertificates.objects.all().count()
        sites_open = FttsCertificates.objects.filter(ftts_final_acceptance_cert_comment__isnull=True).count()
        sites_closed = total_sites - sites_open
        return Response({'total_sites': total_sites, 'open': sites_open, 'closed': sites_closed, })


""" GET NO OF CA AND FA IN SYSTEM FOR MONITORING"""


class FttsTimesheetSummaryView(APIView):

    def get(self, request):
        ftts_total_ca = FttsCertificates.objects.filter(ftts_conditional_acceptance_cert_comment__isnull=False).count()
        ftts_total_fa = FttsCertificates.objects.filter(ftts_final_acceptance_cert_comment__isnull=False).count()
        ftts_total_certs = ftts_total_ca + ftts_total_fa
        return Response({'ftts_total_certs': ftts_total_certs, 'FTTS CA': ftts_total_ca, 'FTTS FA': ftts_total_fa, })


"""GET ISSUE STATUS FOR BOTH A SINGLE PROJECT AND ALL THE PROJECT"""


class FttsIssueStatusView(APIView):

    def get(self, request):
        issues = FttsIssues.objects.all().count()
        issues_closed = FttsIssues.objects.filter(closed=True).count()
        issues_open = issues - issues_closed
        return Response({'total_issues': issues, 'issues_closed': issues_closed, 'issues_open': issues_open, })

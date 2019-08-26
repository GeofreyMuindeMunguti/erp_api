from rest_framework.views import APIView
from .models import *
from rest_framework.response import Response

""" GET TASK STATUS FOR MONITORING"""

"""GET ISSUE STATUS FOR BOTH A SINGLE PROJECT AND ALL THE PROJECT"""

class FttsIssueStatusView(APIView):

    def get(self, request):
        issues = FttsIssues.objects.all().count()
        issues_closed = FttsIssues.objects.filter(closed=True).count()
        issues_open = issues - issues_closed
        return Response({'total_issues': issues, 'issues_closed': issues_closed, 'issues_open': issues_open, })

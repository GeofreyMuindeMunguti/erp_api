from rest_framework.views import APIView
from .models import *
from rest_framework.response import Response

""" GET TASK STATUS FOR MONITORING"""


class TaskStatusView(APIView):

    def get(self, request):
        total_projects = Project.objects.all().count()
        projects_open = Project.objects.filter(final_acceptance_cert__isnull=False).count()
        projects_closed = Project.objects.filter(final_acceptance_cert__isnull=True).count()
        return Response({'total_projects': total_projects, 'open': projects_open, 'closed': projects_closed, })

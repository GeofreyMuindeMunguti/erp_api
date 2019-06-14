from rest_framework.views import APIView
from .models import *
from rest_framework.response import Response
import datetime

""" VIEWS TO CALCULATE OFFTRACK, ONTRACK AND COMPLETED TASKS """

# ############################### TRACK ###########################################################################################################################
def track_docs(model_class, request):
    tasks_done = Task.objects.all()

    if end_date == kpi:
        return Response('OnTrack')
    # else end_date == kpi:
    #     return Response('OffTrack')
# ############################## END #############################################################################################################################

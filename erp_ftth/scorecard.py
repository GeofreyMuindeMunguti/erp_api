from rest_framework.views import APIView
from erp_ftth.models import *
from rest_framework.response import Response
from django.db.models import Avg, Max, Min, Sum


"""GET AVERAGE TURN AROUND TIME"""


class FtthTurnAroundTimeView(APIView):

    def get(self, request):
        project_count = FTTHProject.objects.all().count()
        turn_around_time_data = FTTHProject.objects.all()
        turn_around_time = 0
        for time in turn_around_time_data:
            turn_around_time += time.turn_around_time()
        average_turn_around_time = (turn_around_time/project_count)
        return Response({'average_turn_around_time': average_turn_around_time, })

# 
# """GET REVENUE FOR AN INDIVIDUAL PROJECT USING TOTAL VALUE OF PURCHASE ORDER"""
#
#
# class FtthRevenueDetailView(APIView):
#
#     def get(self, request, pk):
#         try:
#             revenue_per_site_data = FttsProjectPurchaseOrder.objects.get(site_name=pk)
#             revenue_per_site = revenue_per_site_data.ftts_po_client_amount
#             return Response({'revenue_per_project': revenue_per_project, })
#         except Exception as e:
#             return Response({'Error': 'PO for site does not exist'})
#
#
# """GET REVENUE FOR ALL PROJECTS IN THE SYSTEM USING VALUE OF PURCHASE ORDER"""
#
#
# class FtthRevenueListView(APIView):
#
#     def get(self, request):
#         ftts_revenue_project_wide = FttsProjectPurchaseOrder.objects.all().aggregate(Sum('ftts_po_client_amount'))
#         return Response({'revenue_project_wide': ftts_revenue_project_wide, })

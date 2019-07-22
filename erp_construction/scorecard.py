from rest_framework.views import APIView
from .models import *
from rest_framework.response import Response
from django.db.models import Avg, Max, Min, Sum


"""GET AVERAGE TURN AROUND TIME"""


class TurnAroundTimeView(APIView):

    def get(self, request):
        project_count = Project.objects.all().count()
        turn_around_time_data = Project.objects.all()
        turn_around_time = 0
        for time in turn_around_time_data:
            turn_around_time += time.turn_around_time()
        average_turn_around_time = (turn_around_time/project_count)
        return Response({'average_turn_around_time': average_turn_around_time, })


"""GET NUMBER OF PURCHASE ORDERS IN THE SYSTEM"""


class TotalPurchaseOrdersView(APIView):

    def get(self, request):
        purchase_order_data = ProjectPurchaseOrders.objects.all().count()
        return Response({'total_purchase_orders': purchase_order_data, })


"""GET REVENUE FOR AN INDIVISUAL PROJECT USING TOTAL VALUE OF PURCHASE ORDER"""


class RevenueDetailView(APIView):

    def get(self, request, pk):
        try:
            revenue_per_project_data = ProjectPurchaseOrders.objects.get(Site_name=pk)
            revenue_per_project = revenue_per_project_data.total_cost_of_po
            return Response({'revenue_per_project': revenue_per_project, })
        except Exception as e:
            return Response({'Error': 'PO for project does not exist'})


"""GET REVENUE FOR ALL PROJECTS IN THE SYSTEM USING VALUE OF PURCHASE ORDER"""


class RevenueListView(APIView):

    def get(self, request):
        revenue_project_wide = ProjectPurchaseOrders.objects.all().aggregate(Sum('total_cost_of_po'))
        return Response({'revenue_project_wide': revenue_project_wide, })

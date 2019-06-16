from rest_framework.views import APIView
from .models import *
from rest_framework.response import Response
from django.db.models import Avg, Max, Min, Sum


"""GET AVERAGE TURN AROUND TIME"""


class TurnAroundTimeView(APIView):

    def get(self, request):
        turn_around_time_data = Project.objects.all().aggregate(Avg('turn_around_time'))
        return Response({'turn_around_time': turn_around_time_data, })


class TotalPurchaseOrdersView(APIView):

     def get(self, request):
         purchase_order_data = ProjectPurchaseOrders.objects.all().count()
         return Response({'total_purchase_orders': purchase_order_data, })


class RevenueDetailView(APIView):

    def get(self, request, pk):
        try:
            revenue_per_project_data = ProjectPurchaseOrders.objects.get(project_name=pk)
            revenue_per_project = revenue_per_project_data.total_cost_of_po
            return Response({'revenue_per_project': revenue_per_project, })
        except Exception as e:
            return Response({'Error': 'PO for project does not exist'})


class RevenueListView(APIView):

    def get(self, request):
        revenue_project_wide = ProjectPurchaseOrders.objects.all().aggregate(Sum('total_cost_of_po'))
        return Response({'revenue_project_wide': revenue_project_wide, })

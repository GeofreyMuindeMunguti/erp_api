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

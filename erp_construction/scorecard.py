from rest_framework.views import APIView
from .models import *
from rest_framework.response import Response


"""GET AVERAGE TURN AROUND TIME"""


class TurnAroundTimeView(APIView):

    def get(self, request):
        

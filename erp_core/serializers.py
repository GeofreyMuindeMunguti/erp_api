from .models import *

from rest_framework import serializers




class MainSiteSerializer(serializers.ModelSerializer):

    class Meta:
        model = MainSite
        fields = ('__all__')

from rest_framework import serializers
from fcm.models import Device
from fcm.utils import FCMMessage
from django.contrib.auth.models import User, Group


class DeviceSerializer(serializers.ModelSerializer):
     

    class Meta:
        model = Device
        fields = ('dev_id','reg_id','name','is_active')


    



 
from rest_framework import serializers
from fcm_devices.models import MyDevice
from fcm_messaging.models import *
from fcm.utils import FCMMessage
from fcm_devices.serializers import DeviceSerializer
from rest_framework.renderers import JSONRenderer
import requests
import json
import time

class MessageSerializer(serializers.ModelSerializer):

    receiver = serializers.SlugRelatedField(many=True,  slug_field='reg_id',queryset=MyDevice.objects.all())
    sender = serializers.SlugRelatedField(many=False, slug_field='reg_id', queryset=MyDevice.objects.all())

    class Meta:
        model = Message
        fields = ('sender','receiver','title', 'body')



    def save(self):
        message = Message.objects.last()
        data = MessageSerializer(message)
        url = 'https://fcm.googleapis.com/fcm/send'
        data= {
         "registration_ids":data.data['receiver'],
         "notification" : {
         "title": message.title,
         "text" : message.body,
            }
        }
        headers = {'Content-Type': 'application/json', 'Authorization':'key=AAAA__sAwZc:APA91bHlmvgUZObsuUAzCmIjKAxmuDZmZUxxF4VC0mNXBd5poBN6Pefj7lUDpiM8X-z6hPItuO_gIRe3cRkC6kZw6bKNvfCk6BcIuf2UPfAuwrAI7pC6EinU0OjyYN9NnFxr9mXhPion'}

        r = requests.post(url, data=json.dumps(data), headers=headers)

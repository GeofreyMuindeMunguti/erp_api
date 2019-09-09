
from rest_framework import serializers
from fcm_devices.models import MyDevice
from fcm_messaging.models import Message
from fcm.utils import FCMMessage
from users.models import CustomUser

class MessageSerializer(serializers.ModelSerializer):

    sender = serializers.SlugRelatedField(many=False,  slug_field='user_id', queryset=CustomUser.objects.all())
    receiver = serializers.SlugRelatedField(many=False, slug_field='user_id', queryset=CustomUser.objects.all())
    
    class Meta:
        model = Message
        fields = ('sender','receiver','title', 'body')

    def create(self, validated_data):
        message = Message(**validated_data)
        message.save()

        title = message.title #this is the topic to which devices can be subscribed to
        body = message.body # this is the message that can be sent

        FCMMessage().send({'message':body}, to=title)#create a sample topic to test
        
         
        return message


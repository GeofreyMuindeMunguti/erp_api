from django.contrib.auth import authenticate, user_logged_in,login
from django.contrib.auth.models import User, Group
from erp_construction.models import *
from .models import *

from django.http.response import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from rest_framework import serializers, exceptions
from rest_framework.validators import UniqueValidator
from rest_framework.authtoken.models import Token
from rest_framework_jwt.serializers import JSONWebTokenSerializer, jwt_payload_handler, jwt_encode_handler
from django.contrib.contenttypes.models import ContentType

from django.db.models.signals import post_save
from django.dispatch import receiver
import traceback
import sys, os
from django.core.mail import get_connection

"""MESSAGING"""

"""CHAT"""
class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.SlugRelatedField(many=False, slug_field='email', queryset=User.objects.all())
    receiver = serializers.SlugRelatedField(many=False, slug_field='email', queryset=User.objects.all())



    class Meta:
        model = Message
        fields = ['url','sender', 'receiver', 'message', 'timestamp']

    def create(self, validated_data):
         message = Message(**validated_data)
         sender = validated_data.pop('sender')
         message.save()
         newlog = Log(user=sender, action="chatmessage/create")
         newlog.save()

         return message

class SentEmailSerializer(serializers.ModelSerializer):

    class Meta:
        model = SentEmail
        fields = ('url','sender','receiver', 'subject', 'message','attachment')

        @receiver(post_save,sender=SentEmail)
        def send_email(instance,**kwargs):
         server = EmailConfig.objects.order_by('email_host').first()
         my_host = server.email_host
         my_port = server.sender_port
         my_username = server.email_host_user
         my_password = server.email_host_password
         my_use_tls = server.email_use_tls

         connection = get_connection(host=my_host,
                            port=my_port,
                            username=my_username,
                            password=my_password,
                            use_tls=my_use_tls)
         try:
          email = EmailMessage(instance.subject,instance.message,my_username,[instance.receiver.email], connection=connection)
          if instance.attachment != None:
           email.attach_file(str(instance.attachment))
          email.send()
          newlog = Log(user=instance.sender.email, action="emailmessage/create")
          newlog.save()

         except Exception:
             traceback.print_exc()

         def create(self, validated_data):
          message = EmailMessage(**validated_data)
          sender = validated_data.pop('sender')
          message.save()
          return message

class EmailConfigSerializer(serializers.ModelSerializer):

    class Meta:
        model = EmailConfig
        fields = ['url','email_host', 'sender_port', 'email_host_user','email_host_password', 'email_use_ssl','email_use_tls']
        extra_kwargs = {'email_host_password': {'write_only': True}}

        @receiver(post_save,sender=EmailConfig)
        def create_audit(instance,**kwargs):
         newlog = Log(user="Admin", action="emailConfig/create")
         newlog.save()
"""END"""

class JWTSerializer(JSONWebTokenSerializer):
    def validate(self, attrs):
        credentials = {
            self.username_field: attrs.get(self.username_field),
            'password': attrs.get('password')
        }

        if all(credentials.values()):
            user = authenticate(request=self.context['request'], **credentials)

            if user:
                if not user.is_active:
                    msg = 'User account is disabled.'
                    raise serializers.ValidationError(msg)

                payload = jwt_payload_handler(user)
                user_logged_in.send(sender=user.__class__, request=self.context['request'], user=user)

                return {
                    'token': jwt_encode_handler(payload),
                    'user': user
                }
            else:
                msg = 'Unable to log in with provided credentials.'
                raise serializers.ValidationError(msg)
        else:
            msg = 'Must include "{username_field}" and "password".'
            msg = msg.format(username_field=self.username_field)
            raise serializers.ValidationError(msg)

class TokenSerializer(serializers.ModelSerializer):

    class Meta:
        model = Token
        fields = ('key', 'user_id')

class LogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Log
        fields = ('__all__')

class UserProfileSerializer(serializers.ModelSerializer):

    last_seen = serializers.CharField(read_only=True)
    online = serializers.CharField(read_only=True)

    class Meta:
        model = CustomUser
        fields = ('user_id', 'customuser_phone_no','customuser_profile_pic','team', 'position','last_seen','online')
        read_only_fields = ('is_active', 'is_staff')



class UserSerializer(serializers.ModelSerializer):
    """
    A UserProfile serializer to return the UserProfile details
    """
    profile = UserProfileSerializer(required=True)


    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'password','profile')

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        password = validated_data.pop('password')
        user = UserSerializer.create(UserSerializer(), validated_data=profile_data)
        user.set_password(password)
        user.save()
        userprofile = User.objects.create(user=user, **validated_data)

        newlog = Log(user="Admin", action="user/create")
        newlog.save()

        return userprofile

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile')
        password = validated_data.pop('password')
        profile = instance.profile

        instance.email = validated_data.get('email', instance.email)
        instance.save()

        profile.team = profile_data.get('team', profile.team)
        profile.position = profile_data.get('position', profile.position)
        profile.customuser_phone_no = profile_data.get('customuser_phone_no', profile.customuser_phone_no)
        profile.customuser_profile_pic = profile_data.get('customuser_profile_pic', profile.customuser_profile_pic)

        newlog = Log(user="Admin", action="user/update")
        newlog.save()

        return instance

# Permission
class PermissionMapSerializer(serializers.ModelSerializer):
    class Meta:
        model = PermissionMap
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')


# Engineer
class EngineerProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Engineer
        fields = ('id','user_id','engineer_name','country_code', 'engineer_phone_no','department','location_name', 'eng_profile_pic','is_active','engineer_name')
        read_only_fields = ('created_at','updated_at','is_active')


# location
class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('__all__')
        read_only_fields = ('created_at','updated_at','is_active')


# casual
class CasualSerializer(serializers.ModelSerializer):
    class Meta:
        model = Casual
        fields = ('__all__')
        read_only_fields = ('created_at','updated_at','is_active')


class RatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rates
        fields = ('__all__')
        read_only_fields = ('created_at','updated_at','is_active')


class ContentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentType
        fields = ('__all__')

class TeamMemberTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = TeamMemberType
        fields = ('__all__')

class ProjectTeamFTTHSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProjectTeamFTTH
        fields = ('__all__')

class ProjectTeamFTTSSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProjectTeamFTTS
        fields = ('__all__')

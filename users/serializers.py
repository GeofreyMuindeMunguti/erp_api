from django.contrib.auth import authenticate, user_logged_in
from django.contrib.auth.models import User
from erp_construction.models import *
from .models import *

from rest_framework import serializers, exceptions
from rest_framework.validators import UniqueValidator
from rest_framework.authtoken.models import Token
from rest_framework_jwt.serializers import JSONWebTokenSerializer, jwt_payload_handler, jwt_encode_handler

class JWTSerializer(JSONWebTokenSerializer):
    def validate(self, attrs):
        credentials = {
            self.username_field:attrs.get(self.username_field),
            'password': attrs.get('password')
        }

        if all(credentials,values()):
            user = authenticate(request=self.context['request'], **credentials)

            if user:
                if not user.is_active:
                    msg = 'User account is disabled,'
                    raise serializers.ValidationError(msg)

                payload = jwt_payload_handler(user)
                user_logged_in.send(sender=iser.__class__, request=self.context['request'], user=user)

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


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('user_id', 'customuser_phone_no','customuser_profile_pic','team', 'position')
        read_only_fields = ('is_active', 'is_staff')



class UserSerializer(serializers.ModelSerializer):
    """
    A UserProfile serializer to return the UserProfile details
    """
    profile = UserProfileSerializer(required=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'password', 'profile')

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        password = validated_data.pop('password')
        user = UserSerializer.create(UserSerializer(), validated_data=profile_data)
        user.set_password(password)
        user.save()
        userprofile = User.objects.create(user=user, **validated_data)
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
        profile.save()

        return instance

        profile_data = validated_data.pop('profile')
        password = validated_data.pop('password')
        profile = instance.profile

        instance.email = validated_data.get('email', instance.email)
        instance.save()

        profile.team = profile_data.get('team', profile.team)
        profile.position = profile_data.get('position', profile.position)
        profile.customuser_phone_no = profile_data.get('customuser_phone_no', profile.customuser_phone_no)
        profile.customuser_profile_pic = profile_data.get('customuser_profile_pic', profile.customuser_profile_pic)
        profile.save()

        return instance

# Engineer
class EngineerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Engineer
        fields = ('user_id','engineer_phone_no','department','location_name', 'eng_profile_pic')
        read_only_fields = ('created_at','updated_at','is_active')



# class EngineerSerializer(serializers.ModelSerializer):
#     engineerprofile = EngineerProfileSerializer(required=True,many=True)
#
#     class Meta:
#         model = User
#         fields = ('id', 'username', 'email', 'first_name', 'last_name', 'password', 'engineerprofile')
#
#     def create(self, validated_data):
#         engineer_data = validated_data.pop('engineerprofile')
#         password = validated_data.pop('password')
#         user = UserSerializer.create(UserSerializer(), validated_data=engineer_data)
#         user.set_password(password)
#         user.save()
#         engineerprofile = User.objects.create(user=user, **validated_data)
#         return engineerprofile
#
#     def update(self, instance, validated_data):
#         engineer_data = validated_data.pop('engineerprofile')
#         password = validated_data.pop('password')
#         engineerprofile = instance.engineerprofile
#
#         instance.email = validated_data.get('email', instance.email)
#         instance.save()
#
#         engineerprofile.engineer_phone_no = engineer_data.get('engineer_phone_no', engineerprofile.engineer_phone_no)
#         engineerprofile.department = engineer_data.get('department', engineerprofile.department)
#         engineerprofile.location_name = engineer_data.get('location_name', engineerprofile.location_name)
#         engineerprofile.eng_profile_pic = engineer_data.get('eng_profile_pic', engineerprofile.eng_profile_pic)
#         engineerprofile.save()
#
#         return instance


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

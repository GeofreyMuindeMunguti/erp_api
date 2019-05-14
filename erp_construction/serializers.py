
from rest_framework import serializers, exceptions
from rest_framework.validators import UniqueValidator

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from . models import *

# UserList
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('user_id','team','position')
        read_only_fields = ('is_active', 'is_staff')

class UserSerializer(serializers.ModelSerializer):
    """
    A UserProfile serializer to return the UserProfile details
    """
    profile = UserProfileSerializer(required=True)

    class Meta:
        model = User
        fields = ('id','username', 'email', 'first_name', 'last_name', 'password','profile')
    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        password = validated_data.pop('password')
        user = UserSerializer.create(UserSerializer(), validated_data=profile_data)
        user.set_password(password_data)
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
        profile.save()

        return instance

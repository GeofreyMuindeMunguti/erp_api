from django.db import models
from django.contrib.auth.models import User
from phone_field import PhoneField
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    # customuser_phone_no = PhoneNumberField(blank=True, help_text='Phone Number')
    customuser_phone_no = models.CharField(max_length=100, blank=True, null=True)
    profile_pic = models.ImageField(upload_to='files/ProfilePictures', blank=True)
    team = models.CharField(max_length=150, unique=True)
    position = models.CharField(max_length=500, blank=False)

    def __str__(self):
        return self.user.username

    @classmethod
    def get_employees(cls):
        employees = CustomUser.objects.all()
        return employees

    @classmethod
    def get_single_emp(cls, username):
        single_emp = CustomUser.objects.get(employee=username)
        return single_emp

class UserLoginActivity(models.Model):
    # Login Status
    SUCCESS = 'S'
    FAILED = 'F'

    LOGIN_STATUS = ((SUCCESS, 'Success'),
                           (FAILED, 'Failed'))

    login_IP = models.GenericIPAddressField(null=True, blank=True)
    login_datetime = models.DateTimeField(auto_now=True)
    login_username = models.CharField(max_length=40, null=True, blank=True)
    status = models.CharField(max_length=1, default=SUCCESS, choices=LOGIN_STATUS, null=True, blank=True)
    user_agent_info = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'user_login_activity'
        verbose_name_plural = 'user_login_activities'


class Location(models.Model):
    location_name = models.CharField(max_length=20, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.location_name

    @classmethod
    def get_region(cls):
        locations = Location.objects.all()
        return locations

    @classmethod
    def get_single_location(cls, location_id):
        single_location = Location.objects.get(location=location_id)
        return single_location


class Casual(models.Model):
    casual_first_name = models.CharField(max_length=150, unique=True)
    casual_last_name = models.CharField(max_length=150, unique=True)
    casual_phone_no = models.CharField(max_length=100, blank=True, null=True)
    # casual_phone_no = PhoneNumberField(blank=True, help_text='Phone Number')
    location_name = models.ForeignKey(Location, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.casual_first_name  + self.casual_last_name

    @classmethod
    def get_casual(cls):
        casuals = CustomUser.objects.all()
        return casuals

    @classmethod
    def get_single_casual(cls, casual_id):
        single_casual = Casual.objects.get(casual=casual_id)
        return single_casual


class Engineer(models.Model):
    engineer_name = models. ForeignKey(User,on_delete=models.CASCADE, related_name='Engineers')
    engineer_phone_no = models.CharField(max_length=100, blank=True, null=True)
    # engineer_phone_no = PhoneNumberField(blank=True, help_text='Phone Number')
    department = models.CharField(max_length=100, blank=True)
    location_name = models.ForeignKey(Location, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.engineer_name.username


    @classmethod
    def get_engineer(cls):
        engineers = Engineer.objects.all()
        return engineers

    @classmethod
    def get_single_engineer(cls, engineer_id):
        single_engineer = Engineer.objects.get(engineer=engineer_id)
        return single_engineer

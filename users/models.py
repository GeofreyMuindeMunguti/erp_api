from django.db import models
from django.contrib.auth.models import User, Group
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
from django.contrib.auth.models import Permission


class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    # customuser_phone_no = PhoneNumberField(blank=True, help_text='Phone Number')
    customuser_phone_no = models.CharField(max_length=10, blank=True, null=True)
    customuser_profile_pic = models.ImageField(upload_to='ProfilePictures/Employee', blank=True, null=True)
    team = models.CharField(max_length=150)
    position = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='group')

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

    def get_permissions(self):
        perm_tuple = [(x.id, x.name) for x in Permission.objects.filter(group__user=self.user)]
        return perm_tuple

class PermissionMap(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, related_name='authpermission', unique=True)
    position = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='role')
    view = models.BooleanField(default=False)
    edit = models.BooleanField(default=False)
    create = models.BooleanField(default=False)
    approver = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return "%s" % self.position


class UserLoginActivity(models.Model):
    # Login Status
    SUCCESS = 'S'
    FAILED = 'F'

    LOGIN_STATUS = ((SUCCESS, 'Success'), (FAILED, 'Failed'))
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
    casual_name = models.CharField(max_length=150)
    country_code = models.CharField(max_length=100)
    casual_phone_no = models.CharField(max_length=100, unique=True)
    location_name = models.ForeignKey(Location, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.casual_name

    @classmethod
    def get_casual(cls):
        casuals = CustomUser.objects.all()
        return casuals

    @classmethod
    def get_single_casual(cls, casual_id):
        single_casual = Casual.objects.get(casual=casual_id)
        return single_casual


class Engineer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='engineerprofile', unique=True)
    country_code = models.CharField(max_length=100)
    engineer_phone_no = models.CharField(max_length=100)
    department = models.CharField(max_length=100, blank=True)
    location_name = models.ForeignKey(Location, on_delete=models.DO_NOTHING, related_name='location')
    eng_profile_pic = models.ImageField(upload_to='ProfilePictures/Engineer', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def engineer_name(self):
        eng_name = self.user.username
        return eng_name

    def __str__(self):
        return self.user.username

    @classmethod
    def get_engineer(cls):
        engineers = Engineer.objects.all()
        return engineers

    @classmethod
    def get_single_engineer(cls, engineer_id):
        single_engineer = Engineer.objects.get(engineer=engineer_id)
        return single_engineer


class Rates(models.Model):
    worker_type = models.CharField(max_length=100, unique=True)
    rate = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.worker_type)

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.conf import settings

from django.utils import timezone

from .managers import CustomUserManager

# Create your models here.

class Employee(models.Model):
    employee_id= models.CharField(max_length=150)
    first_name= models.CharField(max_length=150)
    last_name= models.CharField(max_length=150)
    team= models.CharField(max_length=150)
    position= models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.employee_id

    @classmethod
    def get_employees(cls):
        employees = Employee.objects.all()
        return employees

    @classmethod
    def get_single_emp(cls, county_id):
        single_emp = Employee.objects.get(employee=employee_id)
        return single_emp


# User.profile = property(lambda u: Employee.objects.get_or_create(user=u)[0])

class User(AbstractUser):
    username = models.CharField(blank=True, null=True,max_length=100)
    email = models.EmailField(_('email address'), unique=True,max_length=250)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return "{}".format(self.email)

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    employee_id= models.ForeignKey(Employee, null=True, on_delete=models.DO_NOTHING, related_name='employees')
    team= models.CharField(max_length=150)
    position= models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username

    @classmethod
    def get_profiles(cls):
        userProfiles = UserProfile.objects.all()
        return userProfiles

    @classmethod
    def get_single_profile(cls, user_id):
        single_profile = UserProfile.objects.get(User=user_id)
        return single_profile


User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])

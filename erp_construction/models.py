from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.conf import settings

from django.utils import timezone

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
    def get_single_emp(cls, employee_id):
        single_emp = Employee.objects.get(employee=employee_id)
        return single_emp



class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    employee_id = models.ForeignKey(Employee, null=True, on_delete=models.DO_NOTHING, related_name='employees')
    username = models.CharField(blank=True, null=True, max_length=150)
    REQUIRED_FIELDS = ['employee_id', 'username']
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.employee_id

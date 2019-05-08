from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import *

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Employee)

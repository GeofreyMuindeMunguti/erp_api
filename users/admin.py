from django.contrib import admin
from .models import *


# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'team', 'position')
    list_display_links = ('user', )
    search_fields = ('user', )

admin.site.register(CustomUser, CustomUserAdmin)

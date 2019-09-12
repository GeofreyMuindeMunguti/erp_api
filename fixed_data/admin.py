from django.contrib import admin
from django import forms
from .models import Client, Technology, Service, Building, Link



class ClientAdmin(admin.ModelAdmin):
    
    list_display = ['first_name','second_name','phone_no', 'created_at', 'updated_at', 'is_active']
    readonly_fields = ['phone_no', 'created_at', 'updated_at', 'is_active']

admin.site.register(Client, ClientAdmin)




class TechnologyAdmin(admin.ModelAdmin):
    pass
 


admin.site.register(Technology, TechnologyAdmin)


class ServiceAdmin(admin.ModelAdmin):
    pass
  


admin.site.register(Service, ServiceAdmin)



class BuildingAdmin(admin.ModelAdmin):
    list_display = [ 'name','created_at', 'updated_at', 'is_active']
    readonly_fields = [ 'created_at', 'updated_at', 'is_active']

admin.site.register(Building, BuildingAdmin)




class LinkAdmin(admin.ModelAdmin):
    list_display = ['circuit_id','created_at', 'updated_at', 'is_active']
    readonly_fields = ['created_at', 'updated_at', 'is_active']
    list_display = ['circuit_id']
    readonly_fields = ['circuit_id']

admin.site.register(Link, LinkAdmin)




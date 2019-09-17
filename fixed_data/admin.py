from django.contrib import admin
from django import forms
from .models import *



class ClientAdmin(admin.ModelAdmin):
    
    list_display = ['first_name','second_name','phone_no', 'created_at', 'updated_at', 'is_active']
    readonly_fields = [ 'created_at', 'updated_at', 'is_active']

admin.site.register(Client, ClientAdmin)


class TechnologyAdmin(admin.ModelAdmin):
    list_display = [ 'tech_name',]
 

admin.site.register(Technology, TechnologyAdmin)


class ServiceAdmin(admin.ModelAdmin):
    list_display = [ 'service_name','technology',]
    

admin.site.register(Service, ServiceAdmin)



class BuildingAdmin(admin.ModelAdmin):
    list_display = [ 'name','longitude','latitude','building_image_2','building_image_2','fiber_ready','created_at', 'updated_at', 'is_active']
    readonly_fields = [ 'created_at', 'updated_at', 'is_active']

admin.site.register(Building, BuildingAdmin)


class LinkAdmin(admin.ModelAdmin):
    list_display = ['circuit_id','client','service','building','survey_file','created_at','decomisioned', 'updated_at', 'is_active']
    readonly_fields = ['created_at', 'updated_at', 'is_active']
    link_display_link = ['circuit_id','client','building']
    search_fields = ('circuit_id', 'decomisioned')
    list_editable = ('is_active','decomisioned')
    #readonly_fields = ['circuit_id']

admin.site.register(Link, LinkAdmin)

class WiMaxtestCriteriaAdmin(admin.ModelAdmin):
    list_display = ['id','link','wan_ip','dbm','snir','connecting_bts','created_at', 'updated_at', 'is_active']
    readonly_fields = ['created_at', 'updated_at', 'is_active']
    link_display_link = ['id','wan_ip',]
    search_fields = ('link', )
    list_editable = ('is_active',)
    #readonly_fields = ['circuit_id']

admin.site.register(WiMaxtestCriteria, WiMaxtestCriteriaAdmin)


class ConsumableAdmin(admin.ModelAdmin):
    list_display = ['id','link','item','quantity','created_at', 'updated_at', 'is_active']
    readonly_fields = ['created_at', 'updated_at', 'is_active']
    link_display_link = ['id','link',]
    search_fields = ('link',)
    list_editable = ('is_active',)
    #readonly_fields = ['circuit_id']

admin.site.register(Consumable, ConsumableAdmin)

class WiMaxInstallationAdmin(admin.ModelAdmin):
    list_display = ['id','link','test_criteria','consumable','created_at', 'updated_at', 'is_active']
    readonly_fields = ['created_at', 'updated_at', 'is_active']
    link_display_link = ['id','link',]
    search_fields = ('id','link__id' )
    list_editable = ('is_active',)
    #readonly_fields = ['circuit_id']

admin.site.register(WiMaxInstallation, WiMaxInstallationAdmin)




class WiMaxPMaintenanceAdmin(admin.ModelAdmin):
    list_display = ['id','link','test_criteria','consumable','created_at', 'updated_at', 'is_active']
    readonly_fields = ['created_at', 'updated_at', 'is_active']
    link_display_link = ['id','link','test_criteria',]
    search_fields = ('link', )
    list_editable = ('is_active',)
    #readonly_fields = ['circuit_id']

admin.site.register(WiMaxPMaintenance, WiMaxPMaintenanceAdmin)


class SupportAdmin(admin.ModelAdmin):
    list_display = ['id','link','issue','resolution','created_at', 'updated_at', 'is_active']
    readonly_fields = ['created_at', 'updated_at', 'is_active']
    link_display_link = ['id','link',]
    search_fields = ('link', )
    list_editable = ('is_active',)
    #readonly_fields = ['circuit_id']

admin.site.register(Support, SupportAdmin)
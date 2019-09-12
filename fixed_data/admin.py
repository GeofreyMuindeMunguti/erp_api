from django.contrib import admin
from django import forms
from .models import Client, Technology, Service, Building, Link



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
    list_display = [ 'name','longitude','latitude','building_image_2','building_image_2','created_at', 'updated_at', 'is_active']
    readonly_fields = [ 'created_at', 'updated_at', 'is_active']

admin.site.register(Building, BuildingAdmin)




class LinkAdmin(admin.ModelAdmin):
    list_display = ['circuit_id','client','service','building','survey_file','created_at', 'updated_at', 'is_active']
    readonly_fields = ['created_at', 'updated_at', 'is_active']
    link_display_link = ['circuit_id','client','building']
    search_fields = ('circuit_id', )
    list_editable = ('is_active',)
    #readonly_fields = ['circuit_id']

admin.site.register(Link, LinkAdmin)




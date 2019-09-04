from django.contrib import admin
from .models import *
from erp_core.base import *
from erp_core.models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name', 'created_by', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('category_name', )
    search_fields = ('category_name', )
    list_editable = ('is_active',)

admin.site.register(Category, CategoryAdmin)

class FiberBudgetAdmin(admin.ModelAdmin):
    list_display = ('id', 'beneficiary_name','site_name','project_name','description', 'date','phoneNumber','quantity', 'rate','unit','amount','is_approved','created_at', 'updated_at', 'is_active')
    list_display_links = ('beneficiary_name', )
    search_fields = ('beneficiary_name', )
    list_editable = ('is_active',)

admin.site.register(FiberBudget, FiberBudgetAdmin)

####################################### KPI ###############################################################################################################################
class KpiAdmin(admin.ModelAdmin):
    list_display = ('id', 'kpi', 'posted_by', 'is_approved', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('kpi', )
    search_fields = ('kpi', )
    list_editable = ('is_active', 'is_approved')


admin.site.register(Kpi, KpiAdmin)

######################################## END #######################################################################################################################################

####################################### TASKS ################################################################################################################################
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name','task_name', 'kpi', 'posted_by', 'is_approved', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('task_name', )
    list_filter = ('category_name',)
    search_fields = ('task_name', )
    list_editable = ('is_active', 'is_approved')


admin.site.register(Task, TaskAdmin)
######################################## END #######################################################################################################################################

####################################### SUBTASKS ###############################################################################################################################
class SubTaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'task_name', 'subtask_name', 'kpi','posted_by', 'is_approved', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('subtask_name', )
    list_filter = ('task_name',)
    search_fields = ('subtask_name', )
    list_editable = ('is_active', 'is_approved')


admin.site.register(SubTask, SubTaskAdmin)

######################################## END #######################################################################################################################################
"""FIBER"""
####################################### KPI ###############################################################################################################################
class FttsKpiAdmin(admin.ModelAdmin):
    list_display = ('id', 'kpi', 'posted_by', 'is_approved', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('kpi', )
    search_fields = ('kpi', )
    list_editable = ('is_active', 'is_approved')


admin.site.register(FttsKpi, FttsKpiAdmin)

######################################## END #######################################################################################################################################

####################################### TASKS ################################################################################################################################
class FttsTaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name','task_name', 'kpi', 'posted_by', 'is_approved', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('task_name', )
    list_filter = ('category_name',)
    search_fields = ('task_name', )
    list_editable = ('is_active', 'is_approved')


admin.site.register(FttsTask, FttsTaskAdmin)
######################################## END #######################################################################################################################################

####################################### SUBTASKS ###############################################################################################################################
class FttsSubTaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'task_name', 'subtask_name', 'kpi','posted_by', 'is_approved', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('subtask_name', )
    list_filter = ('task_name',)
    search_fields = ('subtask_name', )
    list_editable = ('is_active', 'is_approved')


admin.site.register(FttsSubTask, FttsSubTaskAdmin)

######################################## END #######################################################################################################################################

from django.contrib import admin
from .models import *


# Register your models here.
class ProcurementCostTeamAdmin(admin.ModelAdmin):
    list_display = ('id','item','quantity','unit_price', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('item', )
    search_fields = ('item', )

admin.Site.register(ProcurementCostTeam, ProcurementCostTeamAdmin)

from .views import *

# def modify_input_for_multiple_files(project_name, setting_site_clearing,excavation_tower_base,binding,steel_fix_formwork,concrete_pour_curing):

def modify_input_for_multiple_files(project_name, setting_site_clearing):
dict = {}
dict['project_name'] = project_name
dict['setting_site_clearing'] = setting_site_clearing
# dict['setting_site_clearing','excavation_tower_base','binding','steel_fix_formwork','concrete_pour_curing'] = setting_site_clearing,excavation_tower_base,binding,steel_fix_formwork,concrete_pour_curing
return dict

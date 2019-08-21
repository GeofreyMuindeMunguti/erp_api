from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

class ErpFttsConfig(AppConfig):
    name = 'erp_ftts'
    # verbose_name = _('erp_ftts')

    # def ready(self):
    #     import erp_ftts.signals
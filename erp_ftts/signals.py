from .models import SiteTrenching ,CivilWorkProduction
from django.db.models.signals import pre_save
from django.dispatch import receiver

# @receiver(pre_save, sender=SiteTrenching, dispatch_uid="update_trenched_distance")
# def update_trenched_distance(sender, **kwargs):
#     sitetrenching = kwargs['instance']
#     if sitetrenching.pk:
#         CivilWorkProduction.objects.filter(pk=sitetrenching.civilworkproduction_id).update(backfilled_distance=20)




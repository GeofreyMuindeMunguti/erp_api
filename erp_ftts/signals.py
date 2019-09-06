from .models import SiteTrenching ,DailySiteTrenching
from django.db.models.signals import pre_save ,post_save
from django.dispatch import receiver


@receiver(pre_save, sender=DailySiteTrenching, dispatch_uid="update_distance_trenched")
def update_distance_trenched(sender, **kwargs):
    dailysitetrenching = kwargs['instance']
    if dailysitetrenching.pk:
        SiteTrenching.objects.filter(pk=dailysitetrenching.sub_task_id).update(site_trenched_distance = 7777)#dailysitetrenching_count=F('dailysitetrenching_count')+1)


# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from fcm_devices.models import MyDevice
from django.db import models
from users.models import *

# Create your models here.

class Message(models.Model):
    sender =models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='fcmsender')
    receiver =models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='fcmreceiver')
    title = models.CharField(max_length=30)
    body = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-timestamp',)


    def __str__(self):
        return str(self.title)

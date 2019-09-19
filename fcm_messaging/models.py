# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from fcm_devices.models import MyDevice
from django.db import models
from users.models import *

# Create your models here.

class Message(models.Model):
    receiver = models.ManyToManyField(MyDevice, blank = True, null=True)
    sender =models.ForeignKey(MyDevice, on_delete=models.CASCADE, related_name='receiver', null=True)
    title = models.CharField(max_length=30)
    body = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-timestamp',)


    def __str__(self):
        return str(self.title)

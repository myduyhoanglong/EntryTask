# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import timedelta

# Create your models here.

class Auth(models.Model):
    code = models.CharField(max_length=100)
    user_id = models.IntegerField()
    createdTime = models.DateTimeField(auto_now_add=True)
    expiredTime = models.DateTimeField() 

    def __unicode__(self):
        return '[' + self.code + '|' + self.user_id + ']'

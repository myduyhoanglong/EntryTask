# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Person(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=300)
    salt = models.CharField(max_length=300)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=10, choices=(('member', 'member'), ('admin', 'admin')), default='member')

    def __unicode__(self):
        return '[Username: ' + self.username + '|Email: ' + self.email + ']'

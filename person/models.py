# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Person(models.Model):
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=300)
    salt = models.CharField(max_length=300)
    email = models.EmailField()

    def __str__(self):
        return '[' + self.username + '|' + self.email + ']'

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.db import models
from django.contrib import admin
from person.models import Person

# Create your models here.

class Channel(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __unicode__(self):
        return self.name

class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    startDateTime = models.DateTimeField()
    endDateTime = models.DateTimeField()
    createdTime = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='images/%Y/%m/',max_length=300, blank=True)
    channels = models.ManyToManyField(Channel)

    class Meta:
        ordering = ['-createdTime']

    def __unicode__(self):
        return '[' + self.title + ']'

class Participation(models.Model):
    person = models.ForeignKey(Person)
    event = models.ForeignKey(Event)

class Like(models.Model):
    person = models.ForeignKey(Person)
    event = models.ForeignKey(Event)
    likedTime = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    person = models.ForeignKey(Person)
    event = models.ForeignKey(Event)
    content = models.TextField()
    commentedTime = models.DateTimeField(auto_now=True)

class EventAdminForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'
        widget = { 'channels': forms.CheckboxSelectMultiple }

class EventAdmin(admin.ModelAdmin):
    list_filter = ('title', 'location', 'startDateTime', 'endDateTime', 'channels')
    form = EventAdminForm

admin.site.register(Event, EventAdmin)
admin.site.register(Channel)

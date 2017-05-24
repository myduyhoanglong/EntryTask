# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from EntryTask import utils
from event.models import Event, Like, Comment, Participation
from event.views import getAllLikes, getAllComments, getAllParticipations

# Create your views here.

def like(request, event_id):
    data = request.POST

    if 'CURRENT_PERSON' not in request.META:
        utils.createError('Login first.')

    currentPerson = request.META['CURRENT_PERSON']

    event = None
    try:
        event = Event.objects.get(id=event_id)
    except:
        utils.createError('Event id is not correct.')

    if not Like.objects.filter(person=currentPerson, event=event):
        like = Like(person=currentPerson, event=event)
        like.save()

    return getAllLikes(request, event_id)

def comment(request, event_id):
    data = request.POST

    if 'CURRENT_PERSON' not in request.META:
        utils.createError('Login first.')

    currentPerson = request.META['CURRENT_PERSON']

    if 'content' not in data or data['content'] == '':
        utils.createError('No comment content.')

    event = None
    try:
        event = Event.objects.get(id=event_id)
    except:
        utils.createError('Event id is not correct.')

    cmt = Comment(person=currentPerson, event=event, content=data['content'])
    cmt.save()

    return getAllComments(request, event_id)

def participate(request, event_id):
    data = request.POST

    if 'CURRENT_PERSON' not in request.META:
        utils.createError('Login first.')

    currentPerson = request.META['CURRENT_PERSON']

    event = None
    try:
        event = Event.objects.get(id=event_id)
    except:
        utils.createError('Event id is not correct.')

    if not Participation.objects.filter(person=currentPerson, event=event):
        pct = Participation(person=currentPerson, event=event)
        pct.save()

    return getAllParticipations(request, event_id)

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from EntryTask import utils
from event.models import Event, Like, Comment, Participation
from event import views as views_event

# Create your views here.

def like(request, event_id):

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

    return views_event.getAllLikes(request, event_id)

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

    return views_event.getAllComments(request, event_id)

def participate(request, event_id):

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

    return views_event.getAllParticipations(request, event_id)

def getAllLikes(request):
    currentPerson = request.META['CURRENT_PERSON']
    likeList = []
    for like in Like.objects.all():
        if like.person.id == currentPerson.id:
            likeList.append(like)

    return render(request, 'like.html', {'person': True, 'likes': likeList})

def getAllComments(request):
    currentPerson = request.META['CURRENT_PERSON']
    commentList = []
    for cmt in Comment.objects.all():
        if cmt.person.id == currentPerson.id:
            commentList.append(cmt)

    return render(request, 'comment.html', {'person': True, 'comments': commentList})

def getAllParticipations(request):
    currentPerson = request.META['CURRENT_PERSON']
    pctList = []
    for pct in Participation.objects.all():
        if pct.person.id == currentPerson.id:
            pctList.append(pct)

    return render(request, 'participation.html', {'person': True, 'participations': pctList})

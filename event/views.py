# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.utils.dateparse import parse_datetime, parse_date
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from event.models import Event, Like, Comment, Participation, Channel
from EntryTask import utils

# Create your views here.

def getEvents(request):
    data = request.GET
    title = data.get('title', '')
    location = data.get('location', '')
    start = data.get('start', '')
    end = data.get('end', '')
    channels = data.getlist('channels', [])

    events = Event.objects.all()
    eventList = []

    test = ""
    if title != '':
        events = events.filter(title__icontains=title)
    if location != '':
        events = events.filter(location__icontains=location)

    if start != '':
        startDateTime = parse_date(start)
        if startDateTime == None:
            startDateTime = parse_datetime(start)
        if startDateTime != None:
            events = events.exclude(startDateTime__lt=startDateTime)
    if end != '':
        endDateTime = parse_date(end)
        if endDateTime == None:
            endDateTime = parse_datetime(end)
        if endDateTime != None:
            events = events.exclude(endDateTime__gt=endDateTime)

    if channels != []:
        for channel in channels:
            for event in events:
                for channelOfEvent in event.channels.all():
                    if channelOfEvent.id == int(channel):
                        eventList.append(event)
    else:
        eventList = list(events)

    eventPaginator = Paginator(eventList, 5)
    page = request.GET.get('page', '')
    events = []
    try:
        events = eventPaginator.page(page)
    except PageNotAnInteger:
        events = eventPaginator.page(1)
    except EmptyPage:
        events = eventPaginator.page(eventPaginator.num_pages)

    return render(request, 'events.html', {'events': events, 'test': test})

def getAllEvents(request):
    eventList = Event.objects.all()
    eventPaginator = Paginator(Event.objects.all(), 5)
    page = request.GET.get('page', '')
    events = []
    try:
        events = eventPaginator.page(page)
    except PageNotAnInteger:
        events = eventPaginator.page(1)
    except EmptyPage:
        events = eventPaginator.page(eventPaginator.num_pages)

    return render(request, 'events.html', {'events': events})

def getAllLikes(request, event_id):
    event = None
    try:
        event = Event.objects.get(id=event_id)
    except:
        utils.createError('Incorrect event id.')

    likeList = []
    for like in Like.objects.all():
        if like.event.id == int(event_id):
            likeList.append(like)

    return render(request, 'like.html', {'likes': likeList, 'event': event})   

def getAllComments(request, event_id):
    event = None
    try:
        event = Event.objects.get(id=event_id)
    except:
        utils.createError('Incorrect event id.')

    commentList = []
    for cmt in Comment.objects.all():
        if cmt.event.id == int(event_id):
            commentList.append(cmt)

    return render(request, 'comment.html', {'comments': commentList, 'event': event})   

def getAllParticipations(request, event_id):
    event = None
    try:
         event = Event.objects.get(id=event_id)
    except:
        utils.createError('Incorrect event id.')

    participationList = []
    for pct in Participation.objects.all():
        if pct.event.id == int(event_id):
            participationList.append(pct)

    return render(request, 'participation.html', {'participations': participationList, 'event': event})   


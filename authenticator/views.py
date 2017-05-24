# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.utils import timezone

from person.models import Person
from authenticator.models import Auth
from EntryTask import utils

# Create your views here.

#--require POST method
def signup(request):
    data = request.POST
    if 'username' not in data or 'password' not in data or 'email' not in data or data['username'] == '' or data['password'] == '' or data['email'] == '':
        return utils.createError('Invalid input form.')

    _username = data.get('username', '')
    _email = data.get('email', '')
    _password = data.get('password', '')

    #--validation--
    if Person.objects.filter(username=_username):
        return utils.createError('Username has been taken.')
    if Person.objects.filter(email=_email):
        return utils.createError('Email has been taken.')
    if len(_password) < 8:
        return utils.createError('Length of password must be at least 8.')

    #--create person--
    _salt = utils.getRandomString()
    _hashed_password = utils.hashPassword(_password, _salt)

    person = Person(username=_username, salt=_salt, password=_hashed_password, email=_email)	
    person.save()

    return utils.createResponse({'action': 'Sign up successfully', 'username': person.username, 'email': person.email}) 

#--require GET method
def login(request):
    data = request.GET
    if 'username' not in data or 'password' not in data or data['username'] == '' or data['password'] == '':
        utils.createError('Username or password is absent.')

    _username = data.get('username', '')
    _password = data.get('password', '')

    #--validation--
    try:
        person = Person.objects.get(username=_username)
    except:
        return utils.createError('Username does not exist.')

    if utils.hashPassword(_password, person.salt) != person.password:
        return utils.createError('Incorrect Password.')

    #--assign session--
    auth = Auth(code=utils.getRandomString(), user_id=person.id, expiredTime = timezone.now() + timezone.timedelta(days=1)) 
    auth.save()
    
    response = render(request, 'main.html')
    response.set_cookie(key='AUTHENTICATION', value=auth.code)

    return response

def logout(request):
    response = render(request, 'base.html')
    response.delete_cookie(key='AUTHENTICATION')
    return response

from django.http import HttpResponse
from django.shortcuts import render
from person.models import Person

def createPerson(request):
    if 'username' not in request or 'password' not in request or email not in request
        or request['username'] == '' or request['password'] == '' or request['email'] == '':
            raise Exception
    _username = request['username']
    _password = request['password']
    _email = request['email']
    return Person.objects.create(username=_username, password=_password, email=_email)	

def getPerson(request):
    _username = request['username']
    _password = request['password']
    personList = list(Person.objects.filter(username=_username, password=_password))
    if len(personList) > 0:
        return personList[0]
    else:
        raise Person.DoesNotExist

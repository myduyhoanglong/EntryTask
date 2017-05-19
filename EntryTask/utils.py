from django.http import HttpResponse
from django.shortcuts import render
from person.models import Person
import random, hashlib, binascii

def createPerson(request):
    if 'username' not in request or 'password' not in request or 'email' not in request or request['username'] == '' or request['password'] == '' or request['email'] == '':
        raise Exception('Invalid input form.')

    _username = request['username']
    _email = request['email']

    if Person.objects.filter(username=_username):
        raise Exception('Username has been taken.')
    if Person.objects.filter(email=_email):
        raise Exception('Email has been taken.')

    _salt = __getRandomString__()
    _password = __hashPassword__(request['password'], _salt)

    person = Person(username=_username, salt=_salt, password=_password, email=_email)	
    person.save()

    return person

def getPerson(request):
    if 'username' not in request or 'password' not in request or request['username'] == '' or request['password'] == '':
        raise Exception('Invalid input form.')
    
    _username = request['username']
    _password = request['password']

    personList = list(Person.objects.filter(username=_username))
    if len(personList) == 0:
        raise Exception('Username does not exist.')

    person = personList[0]
    if __hashPassword__(_password, person.salt) != person.password:
        raise Exception('Incorrect password.')

    return person

#----------------------------------

def __getRandomString__():
    ALPHABET = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' 
    return "".join(random.choice(ALPHABET) for i in range(16))

def __hashPassword__(plainPassword, salt):
    return binascii.hexlify(hashlib.pbkdf2_hmac('sha256', plainPassword, salt, 100000))

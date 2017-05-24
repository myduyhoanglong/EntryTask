from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse

from person.models import Person
from EntryTask import forms
import random, hashlib, binascii

def createError(text):
    return HttpResponse(text)

def createResponse(response):
    return JsonResponse(response)

def getRandomString():
    ALPHABET = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' 
    return "".join(random.choice(ALPHABET) for i in range(64))

def hashPassword(plainPassword, salt):
    return binascii.hexlify(hashlib.pbkdf2_hmac('sha256', plainPassword, salt, 100000))

def displayMeta(request):
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))

def index(request):
    return render(request, 'base.html')

def displayForm(request, formType, event_id=0):
    if formType == 'login':
        form = forms.LoginForm()
        return generateForm(request, 'form.html', '/auth/login/', form, 'Login', 'get')
    if formType == 'signup':
        form = forms.SignupForm()
        return generateForm(request, 'form.html', '/auth/signup/', form, 'SignUp', 'post')
    if formType == 'search':
        form = forms.SearchForm()
        return generateForm(request, 'form_logined.html', '/event/list/', form, 'Search', 'get')
    if formType == 'comment':
        form = forms.CommentForm()
        if event_id == 0:
           createError('Incorrect event id.') 
        action = '/event/' + str(event_id) + '/act/comment/'
        return generateForm(request, 'form_logined.html', action, form, 'Comment', 'post')

def generateForm(request, template, action, form, value, method):
    return render(request, template, {'action': action, 'form': form, 'value': value, 'method': method})

def displayAll(request):
    personList = list(Person.objects.all())
    html = 'first'
    for person in personList:
        html += str(person) + person.password + '\n'
    return HttpResponse(html)

from django.http import HttpResponse
from django.shortcuts import render
from person.models import Person
from utils import createPerson, getPerson

def signup(request):
    if request.method == 'POST':
        person = createPerson(request.POST)
        return render(request, 'signup_result.html', {'success': True})

def login(request):
    try:
        person = getPerson(request.GET)
    except Person.DoesNotExist:
        return render(request, 'login_form.html', {'error': True})
    return main(request, person)

def main(request, info):
    return render(request, 'main.html', {'person' : info})

def listPerson(request):
    personList = list(Person.objects.all())
    displayedString = ''
    idx = 1
    for person in personList:
        displayedString += str(idx) + '.'
        displayedString += str(person) + '\n'
        idx += 1
    return render(request, 'list.html', {'listPerson' : displayedString})

def login_form(request):
    return render(request, 'login_form.html', {'error': False})

def sign_up_form(request):
    return render(request, 'sign_up_form.html')

from django.http import HttpResponse
from django.shortcuts import render
from person.models import Person

def addPerson(request):
	if request.method == 'POST':
		_username = request.POST['username']
		_password = request.POST['password']
		_email = request.POST['email']
		if Person.objects.filter(username=_username):
			return HttpResponse('Username exists')
		else:
			p = Person.objects.create(username=_username, password=_password, email=_email)	
			return HttpResponse('User created')

def getPerson(request):
	name = request.GET['username']
	passw = request.GET['password']
	if Person.objects.filter(username=name):
		user = Person.objects.filter(username=name)
		if user.filter(password=passw):
			pw = user.filter(password=passw)
			return HttpResponse("Login successfully")	
		else:
			return HttpResponse("Wrong Password")
	else:
		return HttpResponse("No user")

def listPerson(request):
	personList = list(Person.objects.all())
	displayedString = ''
	idx = 1;
	for person in personList:
		displayedString += str(idx) + '.'
		displayedString += str(person) + '\n'
		idx += 1
	return render(request, 'list.html', {'listPerson' : displayedString})

def login_form(request):
	return render(request, 'login_form.html')

def sign_up_form(request):
	return render(request, 'sign_up_form.html')

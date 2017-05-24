from django import forms

from event.models import Channel

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=300, widget=forms.PasswordInput)

class SignupForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=300, widget=forms.PasswordInput)
    email = forms.EmailField()

class SearchForm(forms.Form):
    title = forms.CharField(max_length=100, required=False)
    location = forms.CharField(max_length=100, required=False)
    start = forms.DateTimeField(required=False, widget=forms.DateTimeInput)
    end = forms.DateTimeField(required=False)
    channels = forms.MultipleChoiceField(required=False,
            choices=[(c.id, unicode(c)) for c in Channel.objects.all()],
            widget=forms.CheckboxSelectMultiple)

class CommentForm(forms.Form):
    content = forms.CharField()

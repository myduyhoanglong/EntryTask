from django.conf.urls import url, include

from event import views

urlpatterns = [
    url(r'^all/$', views.getAllEvents),
    url(r'^list/$', views.getEvents),
    url(r'^([0-9]+)/like/$', views.getAllLikes),
    url(r'^([0-9]+)/comment/$', views.getAllComments),
    url(r'^([0-9]+)/participate/$', views.getAllParticipations),
    url(r'^([0-9]+)/', include('person.urls')),
]

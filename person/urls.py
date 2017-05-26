from django.conf.urls import url, include

from person import views
from EntryTask import utils

urlpatterns = [
    url(r'^$', utils.displayUser),
    url(r'^act/like/$', views.like),
    url(r'^act/comment/$', views.comment),
    url(r'^act/participate/$', views.participate),
    url(r'^like/$', views.getAllLikes),
    url(r'^comment/$', views.getAllComments),
    url(r'^participate/$', views.getAllParticipations),
]

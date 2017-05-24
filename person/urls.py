from django.conf.urls import url, include

from person import views
from EntryTask import utils

urlpatterns = [
    url(r'^like/$', views.like),
    url(r'^comment/$', views.comment),
    url(r'^participate/$', views.participate),
]

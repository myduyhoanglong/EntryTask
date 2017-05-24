from django.conf.urls import url, include

from authenticator import views

urlpatterns = [
    url(r'^login/$', views.login),
    url(r'^signup/$', views.signup),
    url(r'^logout/$', views.logout),
]

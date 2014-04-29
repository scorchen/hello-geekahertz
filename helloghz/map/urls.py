from django.conf.urls import patterns, url

from map import views

urlpatterns = patterns('',
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    url(r'sayhello/$', views.sayhello, name='sayhello'),
    url(r'videopopup/$', views.videopopup, name='videopopup'),
    url(r'clownpenis/$', views.clownpenis, name='clownpenis'),

)
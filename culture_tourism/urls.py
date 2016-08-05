from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^main/(?P<pk>\d+)/$', views.mainarticle, name='mainarticle'),
    url(r'^menus/(?P<mmenu>[-\w]+)', views.menu, name='menu'),
    url(r'small/(?P<title>[-\w]+)/(?P<s>[-\w]+)/$', views.small_to_big, name='small'),
    url(r'news/(?P<title>.{1,150})/$', views.news, name='news'),
    url(r'most-visited/(?P<name>.{1,150})/(?P<region>[-\w]+)/$', views.most_visited, name='most_visited'),
    url(r'feedback/$', views.feedback, name='feedback'),
    url(r'maqollar/$', views.maqollar, name='maqollar'),

]
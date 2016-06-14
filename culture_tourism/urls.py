from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^', views.home, name='home'),
    url(r'^information/(?P<category>[-\w]+)/$', views.big_texts, name='information'),

]
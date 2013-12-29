from django.conf.urls import patterns, url, include
from django.views.generic import DetailView, ListView

urlpatterns = patterns('',
   url(r'^$', 'ticket.views.index'),

)


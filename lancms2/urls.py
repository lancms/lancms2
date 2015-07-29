"""lancms2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

from event.views import EventListView, EventDetailView
from event.views import EventListView, EventDetailView, OrganizationDetailView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', EventListView.as_view(), name='event_list'),
    url(r'^o/(?P<slug>[\w-]+)/$', OrganizationDetailView.as_view(), name='org_detail'),
    url(r'^e/(?P<slug>[\w-]+)/$', EventDetailView.as_view(), name='event_detail'),
]

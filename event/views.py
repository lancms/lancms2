from django.shortcuts import render

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from event.models import Event, Organization

class EventListView(ListView):
    model = Event

class EventDetailView(DetailView):
    model = Event

class OrganizationDetailView(DetailView):
    model = Organization

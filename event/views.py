from django.shortcuts import render

from django.views.generic.list import ListView

from event.models import Event

class EventListView(ListView):
    model = Event

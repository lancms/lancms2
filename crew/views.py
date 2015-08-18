from django.shortcuts import render, get_object_or_404, redirect

from django.http import HttpResponse

from core.models import Event, Organization, User
from crew.models import Crew, CrewMembers


# Create your views here.

def crew_front(request, orgslug, eventslug):
    c = {}
    event = get_object_or_404(Event, urlslug=eventslug)
    org = event.organization

    crews = Crew.objects.filter(event=event.id)

    c['org'] = org
    c['event'] = event
    c['crews'] = crews

    return render(request, 'crew/front.html', c, )


def crew_view(request, orgslug, eventslug, crewslug):
    c = {}
    event = get_object_or_404(Event, urlslug=eventslug)
    org = event.organization

    crew = Crew.objects.get(name=crewslug)

    c['org'] = org
    c['event'] = event
    c['crew'] = crew
    c['ms'] = crew.members()
    c['numMs'] = crew.numMembers()

    return render(request, 'crew/view.html', c)


def apply_form(request, orgslug, eventslug):
    c = {}
    event = get_object_or_404(Event, urlslug=eventslug)
    org = event.organization

    c['org'] = org
    c['event'] = event

    return render(request, 'crew/apply.html', c)

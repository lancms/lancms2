from core.common import prtr

from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django.core.exceptions import PermissionDenied
from django.contrib import messages

from core.models import Organization, Event
from ticket.models import TicketType
from crew.models import Crew
from core.forms import EventForm, EventOwnerAddForm, EventSetting


def index (request):
	c = {}

	events = Event.objects.filter(is_active=True)
	if events.count () == 1:
		c['event_featured'] = events[0]
	else:
		c['events'] = events
	return prtr ('index.html', c, request) 


@login_required()
def selfprofile (request):
	c = {}
	return prtr ('account/profile.html', c, request)


def organization_front (request, slug):
	c = {}
	org = get_object_or_404(Organization, urlslug=slug)
	c['organization'] = org
	
	events = Event.objects.filter(is_active=True, organization=org)
	if events.count () == 1:
		c['event_featured'] = events[0]
	else:
		c['events'] = events
	
	return prtr ('organization/front.html', c, request) 


@login_required()
def organization_admin (request, slug):
	org = get_object_or_404(Organization, urlslug=slug)

	if not org.user_is_owner(request.user):
		raise PermissionDenied
    
	c = {'organization': org}
	return prtr ('organization/admin.html', c, request) 



@login_required()
def event_admin (request, orgslug, eventslug):
	c = {}
	event = get_object_or_404(Event, urlslug=eventslug)
	org = event.organization
	tickettypes = list(TicketType.objects.filter(event=event.pk))
	
	c['organization'] = org
	c['event'] = event
	c['tickettypes'] = tickettypes

	if not org.user_is_owner(request.user):
		raise PermissionDenied

	return prtr ('event/admin.html', c, request)


@login_required()
def organization_event_create (request, slug):
	c = {}
	org = get_object_or_404(Organization, urlslug=slug)
	c['organization'] = org

	if not org.user_is_owner(request.user):
		raise PermissionDenied
	
	if request.method == 'POST':
		form = EventForm (request.POST)
		if form.is_valid ():
			form.save (org=org)
			messages.add_message (request, messages.SUCCESS, _('Created event!'))
			return redirect(org)
		else:
			form = EventForm (request.POST)
	else:
		form = EventForm ()
	
	c['form'] = form
	return prtr ('organization/event_create.html', c, request) 


@login_required()
def event_owner_add (request, orgslug, eventslug):
	c = {}
	event = get_object_or_404(Event, urlslug=eventslug)
	org = event.organization
	c['organization'] = org
	c['event'] = event
	
	if not org.user_is_owner(request.user):
		raise PermissionDenied
	
	if request.method == 'POST':
		form = EventOwnerAddForm (request.POST)
		if form.is_valid ():
			if form.user_exists ():
				if form.user_is_new (event):
					form.save (event)
					messages.add_message (request, messages.SUCCESS, _('Added event owner!'))
					return redirect(org)
				else:
					form = EventOwnerAddForm (request.POST)
					messages.add_message (request, messages.ERROR, _('User is already event owner!'))
			else:
				form = EventOwnerAddForm (request.POST)
				messages.add_message (request, messages.ERROR, _("User doesn't exist"))	
		else:
			form = EventOwnerAddForm (request.POST)
	else:
		form = EventOwnerAddForm ()
	
	c['form'] = form
	return prtr ('event/owner_add.html', c, request) 


def event_front (request, orgslug, eventslug):
	c = {}
	event = get_object_or_404(Event, urlslug=eventslug)
	org = event.organization
	c['organization'] = org
	c['event'] = event
	
	return prtr ('event/front.html', c, request) 

@login_required
def event_settings (request, orgslug, eventslug):
	c = {}
	org = get_object_or_404(Organization, urlslug=orgslug)
	event = get_object_or_404(Event, urlslug=eventslug, organization=org)
#	org = event.organization
	c['organization'] = org
	c['event'] = event

	if request.method == 'POST':
		form = EventSetting (request.POST, instance=event)
		if form.is_valid ():
			form.save (event)
			messages.add_message (request, messages.SUCCESS, _('Changed event settings!'))
			return redirect(event)
		else:
			messages.add_message (request, messages.ERROR, form.errors)
			form = EventSetting (request.POST)
	else:
		form = EventSetting (event)
	form = EventSetting (None,instance=event)

	c['form'] = form

	return prtr ('event/settings.html', c, request)


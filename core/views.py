from core.common import prtr

from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django.core.exceptions import PermissionDenied


from core.models import Organization
from core.forms import EventForm

def index (request):
	c = {}
	return prtr ('index.html', c, request) 

@login_required()
def selfprofile (request):
	c = {}
	return prtr ('account/profile.html', c, request)


def organization_front (request, slug):
	c = {'organization': get_object_or_404(Organization, urlslug=slug)}
	return prtr ('organization/front.html', c, request) 


@login_required()
def organization_admin (request, slug):
	org = get_object_or_404(Organization, urlslug=slug)

	if not org.user_is_owner(request.user):
		raise PermissionDenied
    
	c = {'organization': org}
	return prtr ('organization/admin.html', c, request) 


@login_required()
def organization_event_create (request, slug):
	org = get_object_or_404(Organization, urlslug=slug)
	c = {'organization': org}

	if not org.user_is_owner(request.user):
		raise PermissionDenied
	
	if request.method == 'POST':
		form = EventForm (request.POST)
		if form.is_valid ():
			form.save (org=org)
			return redirect(org)
		else:
			form = EventForm (request.POST)
	else:
		form = EventForm ()
	
	c['form'] = form
	return prtr ('organization/event_create.html', c, request) 


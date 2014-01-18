from core.common import prtr


from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied


from core.models import Organization

def index (request):
	c = {}
	return prtr ('index.html', c, request) 

@login_required()
def selfprofile (request):
	c = {}
	return prtr ('account/profile.html', c, request)


def organization_front (request, slug):
	c = {'organization': get_object_or_404(Organization, urlslug=slug)}
	return prtr ('organization.html', c, request) 


@login_required()
def organization_admin (request, slug):
	org = get_object_or_404(Organization, urlslug=slug)

	if not org.user_is_owner(request.user):
		raise PermissionDenied
    
	c = {'organization': org}
	return prtr ('organization_admin.html', c, request) 

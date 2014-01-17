from django.shortcuts import render_to_response
from django.template import RequestContext

from django.conf import settings

from core.models import Organization

def prtr (template, c, request):

	try:
		if settings.DEBUG_WARN:
			c['DEBUG_WARN'] = True
	except:
		pass
	try:
		if settings.DEBUG_REV:
			c['DEBUG_REV'] = settings.DEBUG_REV
	except:
		pass


	# organizations is used in base template. I'm adding it here. -- mboehn
	c['organizations'] = Organization.objects.filter(is_active=True)

	return render_to_response (template, c, context_instance=RequestContext(request))



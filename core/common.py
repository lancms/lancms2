from django.shortcuts import render_to_response
from django.template import RequestContext

from django.conf import settings

def prtr (template, c, request):

	try:
		if settings.DEBUG_WARN:
			c['DEBUG_WARN'] = True
	except:
		pass

	return render_to_response (template, c, context_instance=RequestContext(request))



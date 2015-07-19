# -*- coding: utf-8 -*-

from core.models import Organization

from django.conf import settings

def lc_data(request):
	c = {}

	c['organizations'] = Organization.objects.filter(is_active=True)

	try:
		if settings.DEBUG_WAR:
			c['DEBUG_WARN'] = True
	except:
		pass
	
	try:
		if settings.DEBUG_REV:
			c['DEBUG_REV'] = settings.DEBUG_REV
	except:
		pass

	return c

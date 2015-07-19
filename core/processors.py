# -*- coding: utf-8 -*-

from core.models import Organization

def lc_data(request):
	organizations = Organization.objects.filter(is_active=True)

	return {'organizations': organizations}

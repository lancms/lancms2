# -*- coding: utf-8 -*-

from event.models import Organization

def lc_data(request):
    c = {}
    
    # FIXME: should filter on some active-flag
    c['all_organizations'] = Organization.objects.all()

    return c

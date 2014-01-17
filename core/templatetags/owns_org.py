# -*- coding: utf-8 -*-

from django import template
register = template.Library ()

from core.models import Organization
from django.contrib.auth.models import User

@register.filter
def owns_org (user, org):
	return org.user_is_owner (user)

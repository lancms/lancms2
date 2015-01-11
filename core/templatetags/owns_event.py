# -*- coding: utf-8 -*-

from django import template
register = template.Library ()

from core.models import Event
from django.contrib.auth.models import User

@register.filter
def owns_event (user, event):
        return event.user_is_owner (user)


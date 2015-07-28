from django.contrib import admin

from event.models import Event
from event.models import Organization

from simple_history.admin import SimpleHistoryAdmin

admin.site.register(Event, SimpleHistoryAdmin)
admin.site.register(Organization, SimpleHistoryAdmin)

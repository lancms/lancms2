from django.contrib import admin

from event.models import Event
from event.models import Organization

from simple_history.admin import SimpleHistoryAdmin

@admin.register(Event, Organization)
class ActiveAdmin(SimpleHistoryAdmin):
    def get_queryset(self, request):
        qs = self.model.objects_admin.all()
        return qs

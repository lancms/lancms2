from django.contrib import admin

# Register your models here.

from core.models import Organization, Event

class OrganizationAdmin (admin.ModelAdmin):
	pass
	
class EventAdmin (admin.ModelAdmin):
	pass

admin.site.register (Organization, OrganizationAdmin)
admin.site.register (Event, EventAdmin)

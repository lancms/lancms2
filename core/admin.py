from django.contrib import admin
from django.contrib.auth.models import User, Group

# Register your models here.

from core.models import Organization, Event

class OrganizationAdmin (admin.ModelAdmin):
	list_display = ('name', 'is_active')
	readonly_fields = ('owner', )
	
	def save_model(self, request, obj, form, change):
		gname = 'org_' + obj.urlslug + '_owners'
		try:
			if not Group.objects.filter(name=gname).exists():
				g = Group(name=gname)
				g.save()
				obj.owner = g		
		except:
			pass
		obj.save()
	
class EventAdmin (admin.ModelAdmin):
	list_display = ('name', 'is_active')
	readonly_fields = ('owner', )
	
	def save_model (self, request, obj, form, change):
		gname = 'event_' + obj.urlslug + '_owners'
		try:
			if not Group.objects.filter(name=gname).exists():
				g = Group(name=gname)
				g.save()
				obj.owner = g		
		except:
			pass
		obj.save()

admin.site.register (Organization, OrganizationAdmin)
admin.site.register (Event, EventAdmin)

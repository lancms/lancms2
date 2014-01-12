from django.contrib import admin
from django.contrib.auth.models import User, Group

# Register your models here.

from core.models import Organization, Event

class OrganizationAdmin (admin.ModelAdmin):
	list_display = ('name',)
	
	def save_model(self, request, obj, form, change):
		g = Group(name=obj.name + '_admin')
		g.save()
		
		obj.owner = g.pk		
		obj.save()
	
class EventAdmin (admin.ModelAdmin):
	pass

admin.site.register (Organization, OrganizationAdmin)
admin.site.register (Event, EventAdmin)

from django.contrib import admin
from django.contrib.auth.models import User, Group

# Register your models here.

from core.models import Organization, Event

class OrganizationAdmin (admin.ModelAdmin):
	list_display = ('name',)
	readonly_fields = ('owner', )
	
	def save_model(self, request, obj, form, change):
		g = Group(name=obj.name + '_admin')
		g.save()
		g.user_set.add(request.user)
		
		obj.owner = g		
		obj.save()
	
class EventAdmin (admin.ModelAdmin):
	list_display = ('name',)
	readonly_fields = ('owner', )
	
	def save_model(self, request, obj, form, change):
		g = Group(name=obj.name + '_admin')
		g.save()
		g.user_set.add(request.user)
		
		obj.owner = g		
		obj.save()

admin.site.register (Organization, OrganizationAdmin)
admin.site.register (Event, EventAdmin)

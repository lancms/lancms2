from django.contrib import admin

# Register your models here.

from core.models import Organization

class OrganizationAdmin (admin.ModelAdmin):
	pass

admin.site.register (Organization, OrganizationAdmin)

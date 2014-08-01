from django.contrib import admin

# Register your models here.

from ticket.models import TicketType

class TicketTypeAdmin (admin.ModelAdmin):
	list_display = ('event', 'name')
	#readonly_fields = ('owner', )


admin.site.register (TicketType, TicketTypeAdmin)
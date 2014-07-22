from django.contrib import admin

# Register your models here.

from ticket.models import TicketType


admin.site.register (TicketType)
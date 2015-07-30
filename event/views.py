from django.shortcuts import render
from django.utils.translation import ugettext as _
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

from event.models import Event, Organization

class EventListView(ListView):
    model = Event

class EventDetailView(DetailView):
    model = Event

class OrganizationDetailView(DetailView):
    model = Organization


class OrganizationCreateView(CreateView):
    model = Organization
    fields = ['name', 'slug' ]

    @method_decorator(permission_required('event.add_organization'))
    def dispatch(self, *args, **kwargs):
            return super(OrganizationCreateView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(OrganizationCreateView, self).get_context_data(**kwargs)
        context['page_header'] = _('Create organization')
        return context

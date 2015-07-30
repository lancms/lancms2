from django.shortcuts import render, get_object_or_404, redirect
from django.utils.translation import ugettext as _
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator

from django.core.exceptions import PermissionDenied

from django.contrib import messages

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

from django.contrib.auth.models import User
from event.models import Event, Organization
from event.forms import AddManagerForm

class EventListView(ListView):
    model = Event

class EventDetailView(DetailView):
    model = Event

class OrganizationDetailView(DetailView):
    model = Organization


class OrganizationCreateView(CreateView):
    model = Organization
    fields = ['name', 'slug' ]

    @method_decorator(permission_required('event.add_organization', raise_exception=True))
    def dispatch(self, *args, **kwargs):
            return super(OrganizationCreateView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(OrganizationCreateView, self).get_context_data(**kwargs)
        context['page_header'] = _('Create organization')
        return context


def organization_add_manager(request, slug):
    organization = get_object_or_404(Organization, slug=slug)

    if not request.user.has_perm('manage_organization', organization) and not request.user.has_perm('event.add_organization'):
        raise PermissionDenied

    c = {}
    c['organization'] = organization
    form = AddManagerForm()

    if request.method == 'POST':
        form = AddManagerForm(request.POST)
        if form.is_valid():
            if form.user_exists():
                form.save(organization, 'manage_organization')
                messages.add_message (request, messages.SUCCESS, _("User granted manager permissions")) 
                # FIXME: Should show a different message if user already
                # has manager rights. -- mboehn
                return redirect(organization)
            else:
                messages.add_message (request, messages.ERROR, _("User doesn't exist")) 

    c['form'] = form
    return render(request, 'event/organization_add_manager.html', c)

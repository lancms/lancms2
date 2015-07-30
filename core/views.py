from django.shortcuts import render, get_object_or_404

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.views.generic.detail import DetailView

from django.contrib.auth.models import User


class UserDetailView(DetailView):
    model = User

    def get_object(self):
        return get_object_or_404(User, pk=self.request.user.pk)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(UserDetailView, self).dispatch(*args, **kwargs)

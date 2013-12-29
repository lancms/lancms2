# Create your views here.
from django.shortcuts import render
from django.utils.translation import ugettext as _


def index(request):
   c = {}
   c['main'] = _('Main page of tickets')
   return render(request, "index.html", c)

